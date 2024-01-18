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

@app.get("/btc")
async def exchange_rate():
    data = await fetch_btc_data()
    if "rate" in data:
        rate = data["rate"]
        return {"message": f"1 BTC = {rate} USD"}
    else:
        return {"message": "Error fetching rate. Please try again later."}

@app.get("/ltc")
async def exchange_rate():
    data = await fetch_ltc_data()
    if "rate" in data:
        rate = data["rate"]
        return {"message": f"1 LTC = {rate} USD"}
    else:
        return {"message": "Error fetching rate. Please try again later."}

@app.get("/btc_to_eth")
async def exchange_rate():
    data = await fetch_btc_to_eth_data()
    if "rate" in data:
        rate = data["rate"]
        return {"message": f"1 BTC = {rate} ETH"}
    else:
        return {"message": "Error fetching rate. Please try again later."}

@app.get("/btc_to_ltc")
async def exchange_rate():
    data = await fetch_btc_to_ltc_data()
    if "rate" in data:
        rate = data["rate"]
        return {"message": f"1 BTC = {rate} LTC"}
    else:
        return {"message": "Error fetching rate. Please try again later."}

    
@app.get("/eth")
async def exchange_rate():
    data = await fetch_eth_data()
    if "rate" in data:
        rate = data["rate"]
        return {"message": f"1 ETH = {rate} USD"}
    else:
        return {"message": "Error fetching rate. Please try again later."}    

@app.get("/eth_to_ltc")
async def exchange_rate():
    data = await fetch_eth_to_ltc_data()
    if "rate" in data:
        rate = data["rate"]
        return {"message": f"1 ETH = {rate} LTC"}
    else:
        return {"message": "Error fetching rate. Please try again later."}


async def fetch_btc_data():
    url = "https://rest.coinapi.io/v1/exchangerate/BTC/USD"
    headers = {
        "X-CoinAPI-Key": os.environ.get("COIN_API_KEY")
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        return response.json()

async def fetch_eth_data():
    url = "https://rest.coinapi.io/v1/exchangerate/ETH/USD"
    headers = {
        "X-CoinAPI-Key": os.environ.get("COIN_API_KEY")
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        return response.json()
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        return response.json()

async def fetch_ltc_data():
    url = "https://rest.coinapi.io/v1/exchangerate/LTC/USD"
    headers = {
        "X-CoinAPI-Key": os.environ.get("COIN_API_KEY")
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        return response.json()
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        return response.json()
    
async def fetch_btc_to_eth_data():
    url = "https://rest.coinapi.io/v1/exchangerate/BTC/ETH"
    headers = {
        "X-CoinAPI-Key": os.environ.get("COIN_API_KEY")
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        return response.json()
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        return response.json()

async def fetch_btc_to_ltc_data():
    url = "https://rest.coinapi.io/v1/exchangerate/BTC/LTC"
    headers = {
        "X-CoinAPI-Key": os.environ.get("COIN_API_KEY")
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        return response.json()

async def fetch_eth_to_ltc_data():
    url = "https://rest.coinapi.io/v1/exchangerate/ETH/LTC"
    headers = {
        "X-CoinAPI-Key": os.environ.get("COIN_API_KEY")
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        return response.json()



