from fastapi import FastAPI
import random
from TGPT.TGPT import generate_response


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from stupid-api! this is the updated version 3."}

@app.post("/echo")
def echo_string(text: str):
    return {"received": text, "response": f"You said: {text}"}

@app.post("/sarcastic")
def sarcastic_response(text: str):
    return ''.join(
        char.upper() if char.isalpha() and random.random() < 0.5 else char.lower()
        for char in text
    )

@app.post("/TGPT")
def get_tgpt_response(user_input: str):
    response = generate_response(user_input)
    return {"response": response}