from fastapi import FastAPI, Path,HTTPException, Query
import json
from pydantic import BaseModel, Field
from typing import Annotated, Literal

class Patient(BaseModel):

    id = Annotated[str, Field(..., description='ID of the Patient', examples=['P001'])]
    name =Annotated[str, Field(..., description='Name of the patient')]
    city = Annotated[str, Field(..., description='City is where the patient is living')]
    age = Annotated[int, Field(..., gt= 0, lt= 120, description='Age of the Patient')]
    gender = Annotated[Literal['male','female','other'], Field(..., description='Gender of the patient')]
    height = Annotated[float, Field(..., gt = 0, description='Height of the patient in mtrs')]
    weight = Annotated[float, Field(..., gt = 0, description='weight of the patient in kgs')]

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

@app.get('/sort')
def sort_patient(sort_by:str = Query(...,description='sort on the basis of height, weight or bmi'),
                 order:str = Query('asc',description='sort in asc or desc order')):
    
    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException('400',detail=f'Invalid field selct from {valid_fields}')
    if order not in ['asc','desc']:
        raise HTTPException('400',detail=f'Invalid field selct between asc and desc')
    
    data = load_data()
    direction = True if order == 'desc' else False
    sorted_data = sorted(data.values(),key=lambda x: x.get(sort_by,0), reverse=direction)
    return sorted_data