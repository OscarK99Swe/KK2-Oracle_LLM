from fastapi import FastAPI

app = FastAPI(title="KK2 - Oraklet")

@app.get("/health")
def health_check():
    return {"status": "Sigma"}