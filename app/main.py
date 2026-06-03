from fastapi import FastAPI, UploadFile, File, HTTPException, status
import pandas as pd
import io
from app.data import save_dataframe, get_dataframe
from app.schemas import UploadMetadataResponse, StatsResponse

app = FastAPI(title="KK2 - Oracle")

@app.get("/health")
def health_check():
    return {"status": "Sigma"}


@app.post("/data/upload", response_model=UploadMetadataResponse)
async def upload_file(file: UploadFile = File(...)):
    if not file.filename.endswith('.csv'):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect fileformat, only CSV-files permitted"
        )
    
    try:
        contents = await file.read()
        df = pd.read_csv(io.BytesIO(contents))
        if df.empty:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="The upploaded file is in the correct csv-fileformat, however, why tf is it empty yo?"
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
            detail=f"Couldn't read CSV-file: {str(e)}"
        )


@app.get("/data/stats", response_model=StatsResponse)
def get_stats():
    df = get_dataframe()
    
    if df is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No data available, please upload a CSV file first."
        )
    
    stats_df = df.describe()
    
    stats_dict = stats_df.to_dict()
    
    return StatsResponse(summary=stats_dict)