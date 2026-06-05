from app.chain.runnable import Runnable
from app.schemas import PromptBuilderInput, LLMRunnerInput, ResponseParserInput, AskResponse
from transformers import pipeline
import functools

@functools.lru_cache(maxsize=1)
def load_text_pipeline():
    print("Loading the SmolLM-model... Thank you for your patience, sigma")
    return pipeline(
        "text-generation", 
        model="HuggingFaceTB/SmolLM2-1.7B-Instruct",
        device="cpu",
        trust_remote_code=True
    )

class PromptBuilder(Runnable[PromptBuilderInput, LLMRunnerInput]):
    def invoke(self, input_data: PromptBuilderInput) -> LLMRunnerInput:
        prompt = (
            f"You are a helpful AI data analyst.\n"
            f"Here is the descriptive statistical summary of the dataset:\n"
            f"{input_data.stats_str}\n\n"
            f"User Question: {input_data.question}\n"
            f"Provide a clear and concise answer based strictly on the statistics provided."
        )
        return LLMRunnerInput(question=input_data.question, formatted_prompt=prompt)

class LLMRunner(Runnable[LLMRunnerInput, ResponseParserInput]):
    def invoke(self, input_data: LLMRunnerInput) -> ResponseParserInput:
        generator = load_text_pipeline()
        
        messages = [
            {"role": "system", "content": "You are a helpful AI data analyst."},
            {"role": "user", "content": input_data.formatted_prompt}
        ]
        
        outputs = generator(
            messages, 
            max_new_tokens=150,
            temperature=0.3, 
            do_sample=True,
            clean_up_tokenization_spaces=False
        )
        
        raw_text = outputs[0]["generated_text"][-1]["content"].strip()
        return ResponseParserInput(question=input_data.question, raw_output=raw_text)

class ResponseParser(Runnable[ResponseParserInput, AskResponse]):
    def invoke(self, input_data: ResponseParserInput) -> AskResponse:
        final_answer = input_data.raw_output if input_data.raw_output else "The Oracle is speechless! (Model returned an empty string, sorry brochaco)"
        return AskResponse(
            question=input_data.question,
            answer=final_answer,
            model="HuggingFaceTB/SmolLM2-1.7B-Instruct"
        )