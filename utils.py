from dotenv import load_dotenv
import requests
import httpx
import os


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

