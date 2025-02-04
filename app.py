from fastapi import FastAPI
from pydantic import BaseModel
from data import data

app = FastAPI()

@app.get("/name")
async def get_name():
    names = [person["name"] for person in data]
    return {"names": names}

@app.get("/occupation")
async def get_occupation():
    occupations = [person["occupation"] for person in data]
    return {"occupations": occupations}

@app.get("/address")
async def get_address():
    addresses = [person["address"] for person in data]
    return {"addresses": addresses}