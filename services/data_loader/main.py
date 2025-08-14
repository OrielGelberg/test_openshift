 # main.py
# fast_api_app/app/main.py
from fastapi import FastAPI
from .dal import DAL
from unicorn import unicorn

app = FastAPI()
dal = DAL()

@app.get("/data")
def get_all_data():
    data = dal.get_data()
    if data is None:
        return {"error": "Failed to retrieve data from database"}
    return {"data": data}