from fastapi import FastAPI
from DALL import DAL
import os

app = FastAPI()

dal = DAL(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    database=os.getenv("DB_NAME")
)


@app.get("/data")
def get_data():
    return dal.get_data()
