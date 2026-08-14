from fastapi import FastAPI
import json

def load_data():
    with open('patient.json', 'r') as f:
        data = json.load(f)
    return data


app = FastAPI()

@app.get('/')
def home():
    return {'message':'Hello this is practice program'}


@app.get('/view')
def view():
    data = load_data()
    return data
