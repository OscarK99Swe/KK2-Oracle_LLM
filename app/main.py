from fastapi import FastAPI, UploadFile, File, HTTPException, status
import pandas as pd
import io

from app.data import save_dataframe, get_dataframe
from app.schemas import UploadMetadataResponse, StatsResponse, AskRequest, AskResponse

from app.chain.pipeline import generate_ai_answer_via_chain

app = FastAPI(title="KK2 - Oracle")


@app.get("/health")
def health_check():
    return {"status": "Sigma"}


@app.post("/data/upload", response_model=UploadMetadataResponse)
async def upload_file(file: UploadFile = File(...)):
    if not file.filename.endswith('.csv'):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect fileformat, only CSV-files are accepted"
        )
    
    try:
        contents = await file.read()
        df = pd.read_csv(io.BytesIO(contents))
        
        if df.empty:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="It is a CSV-file... but why tf is it empty, yo?"
            )
            
        save_dataframe(df)
        formatted_dtypes = {col: str(dtype) for col, dtype in df.dtypes.items()}
        
        return UploadMetadataResponse(
            rows=len(df),
            columns=list(df.columns),
            dtypes=formatted_dtypes
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Could not interpret the CSV-File: {str(e)}"
        )


@app.get("/data/stats", response_model=StatsResponse)
def get_stats():
    df = get_dataframe()
    if df is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No statistics available. Please upload a valid CSV file first."
        )
    return StatsResponse(summary=df.describe().to_dict())


@app.post("/ai/ask", response_model=AskResponse)
def ask_oracle(payload: AskRequest):
    df = get_dataframe()
    
    if df is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No data found to ask questions to, please upload a CSV-file first."
        )
        
    try:
        stats_string = df.describe().to_string()
        
        chain_response = generate_ai_answer_via_chain(payload.question, stats_string)
        
        return chain_response
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error generating AI response via chain: {str(e)}"
        )