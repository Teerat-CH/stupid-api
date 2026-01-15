from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from stupid-api! this is the updated version."}

@app.post("/echo")
def echo_string(text: str):
    return {"received": text, "response": f"You said: {text}"}