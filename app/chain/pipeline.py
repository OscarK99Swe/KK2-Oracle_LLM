from app.chain.steps import PromptBuilder, LLMRunner, ResponseParser
from app.schemas import PromptBuilderInput, AskResponse

def generate_ai_answer_via_chain(question: str, stats_str: str) -> AskResponse:
    prompt_builder = PromptBuilder()
    llm_runner = LLMRunner()
    response_parser = ResponseParser()
    
    chain = prompt_builder | llm_runner | response_parser
    
    chain_input = PromptBuilderInput(question=question, stats_str=stats_str)
    return chain.invoke(chain_input)