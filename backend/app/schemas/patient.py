from fastapi import FastAPI
from pydantic import BaseModel


class Patient(BaseModel):
    firstname: str
    lastname: str
    age: int
    sex: str(1)
    email: str
    mobile: str
    DOB: str
    state: str
    city: str
    pin: int
