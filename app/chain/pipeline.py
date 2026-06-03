from transformers import pipeline
import functools

@functools.lru_cache(maxsize=1)
def load_text_pipeline():
    print("Loading the SmolLM-model... Thank you for your patience, sigma")
    
    generator = pipeline(
        "text-generation", 
        model="HuggingFaceTB/SmolLM2-1.7B-Instruct",
        device="cpu",
        trust_remote_code=True
    )
    return generator

def generate_ai_answer(prompt: str) -> str:
    generator = load_text_pipeline()
    
    messages = [
        {"role": "system", "content": "You are a helpful AI data analyst."},
        {"role": "user", "content": prompt}
    ]
    
    outputs = generator(
        messages, 
        max_new_tokens=150,
        temperature=0.3, 
        do_sample=True,
        clean_up_tokenization_spaces=False
    )
    
    answer = outputs[0]["generated_text"][-1]["content"].strip()
    
    if not answer:
        return "The Oracle is speechless! (Model returned an empty string, sorry brochaco)"
        
    return answer