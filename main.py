from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from stupid-api! this is the updated version 2."}

@app.post("/echo")
def echo_string(text: str):
    return {"received": text, "response": f"You said: {text}"}

@app.post("/sarcastic")
def sarcastic_response(text: str):
    return ''.join(
        char.upper() if char.isalpha() and random.random() < 0.5 else char.lower()
        for char in text
    )