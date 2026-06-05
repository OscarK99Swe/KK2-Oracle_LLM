from pydantic import BaseModel
from typing import List, Dict

class UploadMetadataResponse(BaseModel):
    rows: int
    columns: List[str]
    dtypes: Dict[str, str]

class StatsResponse(BaseModel):
    summary: Dict[str, Dict[str, float]]


class AskRequest(BaseModel):
    question: str

class AskResponse(BaseModel):
    question: str
    answer: str
    model: str

class PromptBuilderInput(BaseModel):
    question: str
    stats_str: str

class LLMRunnerInput(BaseModel):
    question: str
    formatted_prompt: str

class ResponseParserInput(BaseModel):
    question: str
    raw_output: str