import pytest
from unittest.mock import patch, MagicMock

from app.schemas import PromptBuilderInput, LLMRunnerInput, ResponseParserInput
from app.chain.steps import PromptBuilder, LLMRunner, ResponseParser

def test_prompt_builder_formatting():
    builder = PromptBuilder()
    input_data = PromptBuilderInput(
        question="Which city is the coldest?", 
        stats_str="Min temp: -1.50"
    )
    
    output = builder.invoke(input_data)
    
    assert "Which city is the coldest?" in output.formatted_prompt
    assert "Min temp: -1.50" in output.formatted_prompt
    assert output.question == "Which city is the coldest?"

def test_response_parser_normal_output():
    parser = ResponseParser()
    input_data = ResponseParserInput(
        question="Which city is the hottest?", 
        raw_output="Malmö is the hottest at 8.3°C."
    )
    
    output = parser.invoke(input_data)
    
    assert output.answer == "Malmö is the hottest at 8.3°C."
    assert output.model == "HuggingFaceTB/SmolLM2-1.7B-Instruct"

def test_response_parser_empty_fallback():
    parser = ResponseParser()
    input_data = ResponseParserInput(question="Test?", raw_output="")
    
    output = parser.invoke(input_data)
    
    assert "sorry brochaco" in output.answer 

@patch("app.chain.steps.load_text_pipeline")
def test_llm_runner_mocked(mock_load_pipeline):
    mock_generator = MagicMock()
    
    mock_generator.return_value = [{"generated_text": [{"content": "I am a mocked AI answer!"}]}]
    mock_load_pipeline.return_value = mock_generator
    
    runner = LLMRunner()
    input_data = LLMRunnerInput(question="Mock me?", formatted_prompt="Fake prompt")
    output = runner.invoke(input_data)
    
    assert output.raw_output == "I am a mocked AI answer!"
    assert output.question == "Mock me?"