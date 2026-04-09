from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: str
    age: int = Field(gt = 0,lt =120)
    email : EmailStr
    linkedin : AnyUrl
    weight: float = Field(gt=0)
    married: bool
    allergies : Optional[List[str]] = None
    contact_info : Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com','icici.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError('Not a valid Domain')
        
        return value
    
    @field_validator('name')
    @classmethod
    def transform(cls,name):
        return name.upper()

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