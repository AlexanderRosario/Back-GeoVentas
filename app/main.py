from typing import Union
from app.models.item_model import Item
from fastapi import FastAPI
import pandas as pd

from app.services.population_service import get_filtered_population  # Add pandas import

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "klk"}


@app.get("/population/")
def get_population(provincia: Union[str, None] = None, municipio: Union[str, None] = None, barrio: Union[str, None] = None):
    return get_filtered_population(provincia, municipio, barrio)
