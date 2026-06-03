from pydantic import BaseModel
from typing import List, Dict

class UploadMetadataResponse(BaseModel):
    rows: int
    columns: List[str]
    dtypes: Dict[str, str]

class StatsResponse(BaseModel):
    summary: Dict[str, Dict[str, float]]