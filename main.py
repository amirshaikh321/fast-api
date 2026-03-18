from fastapi import FastAPI, Path,HTTPException
import json

app = FastAPI()

def load_data():
    with open('patient.json','r') as f:
        data  = json.load(f)
    return data

@app.get("/")
def hello():
    return { "message": "Hello world"}

@app.get("/about")
def about():
    return {"message": "this is about page"}

@app.get('/view')
def view():
    data = load_data()
    return data

@app.get('/patient/{patient_id}')
def view_patient(patient_id:str =  Path(...,description='Id of the patient in DB', example='P001`')):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404,detail='Patient not found')
