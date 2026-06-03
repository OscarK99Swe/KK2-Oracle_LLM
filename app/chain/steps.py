import pandas as pd

def create_ai_prompt(df: pd.DataFrame, question: str) -> str:
    data_string = df.to_markdown(index=False)
    prompt = (
        "You are a helpful AI data analyst.\n"
        "Here is the information in the uploaded data table:\n\n"
        f"{data_string}\n\n"
        f"User asks: {question}\n"
        "Answer briefly and directly in English based on the table above."
    )
    return prompt