from dotenv import load_dotenv
from typing import Optional
import requests
import httpx
import os


async def fetch_data(crypto_from: str, crypto_to: str = "USD"):
    url = f"https://rest.coinapi.io/v1/exchangerate/{crypto_from}/{crypto_to}"
    headers = {
        "X-CoinAPI-Key": os.environ.get("COIN_API_KEY")
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            return {"message": f"Error fetching rate: {e.response.status_code}"}
        except httpx.RequestError as e:
            return {"message": f"Error fetching rate: {e.request_error}"}
        except Exception as e:
            return {"message": f"Error fetching rate: {str(e)}"} 