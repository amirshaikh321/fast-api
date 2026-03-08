from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return { "message": "Hello world",
             "title": "firt program of fastapi"}
