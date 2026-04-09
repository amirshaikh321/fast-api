from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(title='Name of the Patient',description='Give the name of the patient in less than 50 characters',examples=['Karishma','Max'])]
    age: Annotated[int, Field(gt=0,lt =120,description='give the patient age')]
    email : EmailStr
    linkedin : AnyUrl
    weight: float = Field(gt=0)
    married: bool
    allergies : Optional[List[str]] = None
    contact_info : Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age >60 and 'emergency' not in model.contact_info:
            raise ValueError("Patient older than 60 must have emergency contact")
        return model
    
def insert_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.linkedin)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_info)
    print("inserted")

patient_info = {"name":"Aman",
    "age":87,
    "email":'amirshaikh1594@hdfc.com',
    "linkedin":'https://www.linkedin.com/in/amir-shaikh-75aaa1251',
    "weight":65.5,
    "married":False,
    "allergies":['pollen','dust'],
    "contact_info":{'Phone':'8421652597','emergency':'56886539'}}

patient1 = Patient(**patient_info)

insert_data(patient1)