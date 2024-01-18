from fastapi import FastAPI
from dotenv import load_dotenv
import requests
import httpx
import os

load_dotenv()

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Functions
async def fetch_data(crypto: str):
    url = f"https://rest.coinapi.io/v1/exchangerate/{crypto}/USD"
    headers = {
        "X-CoinAPI-Key": os.environ.get("COIN_API_KEY")
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        return response.json()
    
async def fetch_coin_to_coin_data(crypto1: str, crypto2: str):
    url = f"https://rest.coinapi.io/v1/exchangerate/{crypto1}/{crypto2}"
    headers = {
        "X-CoinAPI-Key": os.environ.get("COIN_API_KEY")
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        return response.json()

# Endpoints
@app.get("/btc")
async def exchange_rate():
    data = await fetch_data(crypto="BTC")
    if "rate" in data:
        rate = data["rate"]
        return {"message": f"1 BTC = {rate} USD"}
    else:
        return {"message": "Error fetching rate. Please try again later."}

@app.get("/ltc")
async def exchange_rate():
    data = await fetch_data(crypto="LTC")
    if "rate" in data:
        rate = data["rate"]
        return {"message": f"1 LTC = {rate} USD"}
    else:
        return {"message": "Error fetching rate. Please try again later."}

@app.get("/btc_to_eth")
async def exchange_rate():
    data = await fetch_coin_to_coin_data(crypto1="BTC", crypto2="ETH")
    if "rate" in data:
        rate = data["rate"]
        return {"message": f"1 BTC = {rate} ETH"}
    else:
        return {"message": "Error fetching rate. Please try again later."}

@app.get("/btc_to_ltc")
async def exchange_rate():
    data = await fetch_coin_to_coin_data(crypto1="BTC", crypto2="LTC")
    if "rate" in data:
        rate = data["rate"]
        return {"message": f"1 BTC = {rate} LTC"}
    else:
        return {"message": "Error fetching rate. Please try again later."}

    
@app.get("/eth")
async def exchange_rate():
    data = await fetch_data(crypto="ETH")
    if "rate" in data:
        rate = data["rate"]
        return {"message": f"1 ETH = {rate} USD"}
    else:
        return {"message": "Error fetching rate. Please try again later."}    


@app.get("/eth_to_ltc")
async def exchange_rate():
    data = await fetch_coin_to_coin_data(crypto1="ETH", crypto2="LTC")
    if "rate" in data:
        rate = data["rate"]
        return {"message": f"1 ETH = {rate} LTC"}
    else:
        return {"message": "Error fetching rate. Please try again later."}



