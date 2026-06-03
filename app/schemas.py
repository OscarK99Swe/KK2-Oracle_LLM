from pydantic import BaseModel
from typing import List, Dict

class UploadMetadataResponse(BaseModel):
    rows: int
    columns: List[str]
    dtypes: Dict[str, str]