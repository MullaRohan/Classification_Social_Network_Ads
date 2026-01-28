from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from typing import Annotated
import pandas as pd
import pickle

app = FastAPI()
templates = Jinja2Templates(directory="templates")

with open("ads_purchased.pkl", "rb") as file:
    model = pickle.load(file)


class CustomerPredict(BaseModel):
    age: int
    salary: int
    gender: str


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict")
def predict(data: CustomerPredict):
    df = pd.DataFrame([data.model_dump()])
    prediction = model.predict(df)[0]

    result = "Buy" if prediction == 1 else "Not Buy"
    return {"prediction": result}
