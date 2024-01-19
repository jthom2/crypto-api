from fastapi import FastAPI, HTTPException, Query
from dotenv import load_dotenv
from utils import fetch_data
import requests
import httpx
import os

load_dotenv()

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}



@app.get("/convert")
async def exchange_rate(crypto_from: str = Query(...), crypto_to: str = Query("USD")):
    data = await fetch_data(crypto_from.upper(), crypto_to.upper())
    if "error" in data:
        raise HTTPException(status_code=400, detail=data["error"])
    if "rate" in data:
        rate = data["rate"]
        return {"message": f"1 {crypto_from.upper()} = {rate} {crypto_to.upper()}"}
    else: 
        return {"message": "Error fetching data. Please try again later."}