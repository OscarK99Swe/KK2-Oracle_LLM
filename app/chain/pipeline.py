from transformers import pipeline
import functools

@functools.lru_cache(maxsize=1)
def load_text_pipeline():
    print("Loading the SmolLM-model... Thank you for your patience, sigma")
    
    generator = pipeline(
        "text-generation", 
        model="HuggingFaceTB/SmolLM2-1.3B-Instruct",
        device="cpu"
    )
    return generator

def generate_ai_answer(prompt: str) -> str:
    generator = load_text_pipeline()
    
    outputs = generator(
        prompt, 
        max_new_tokens=150, 
        temperature=0.3, 
        do_sample=True
    )
    
    generated_text = outputs[0]["generated_text"]
    answer = generated_text.replace(prompt, "").strip()
    return answer