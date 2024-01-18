![DALL·E 2024-01-16 20 15 30 - Design a sleek and modern landscape logo for a cryptocurrency exchange rate application  The logo should include elements that symbolize digital curre-modified](https://github.com/jthom2/crypto-api/assets/134821369/fc4765de-b914-4d18-980a-5bccd12898f8)
# Cryptocurrency Exchange Rate API

## Introduction
This project is a web application built with FastAPI. It provides exchange rates for various cryptocurrencies including Bitcoin (BTC), Litecoin (LTC), and Ethereum (ETH) in USD. The application has dedicated endpoints for each cryptocurrency to fetch and display the current exchange rates.

## Installation
To set up this project locally, you need to have Python installed on your system. Follow these steps:

1. Clone the repository:
    `git clone https://github.com/jthom2/crypto-api`

2. Navigate to the project directory:
    `cd crypto-api`

3. Install the required dependencies:
    `pip install -r requirements.txt`

## Usage
To run the application, use the following command in the project directory:
    `uvicorn main:app --reload`
    
The application will start running on `http://127.0.0.1:8000`. You can access the following endpoints:
- `/` - Basic welcome message.
- `/btc` - Fetches and displays the exchange rate for Bitcoin (BTC) in USD.
- `/ltc` - Fetches and displays the exchange rate for Litecoin (LTC) in USD.
- `/eth` - Fetches and displays the exchange rate for Ethereum (ETH) in USD.
- `/btc_to_eth` - Converts and displays the exchange rate from Bitcoin (BTC) to Ethereum (ETH).
- `/btc_to_ltc` - Converts and displays the exchange rate from Bitcoin (BTC) to Litecoin (LTC).
- `/eth_to_ltc` - Converts and displays the exchange rate from Ethereum (ETH) to Litecoin (LTC).

## Dependencies
- FastAPI: A modern, fast (high-performance) web framework for building APIs.
- Uvicorn: An ASGI server for hosting the application.
- HTTPX: A fully featured HTTP client for Python.
- Requests: A simple HTTP library for Python.
- Python-Dotenv: A Python module to read key-value pairs from a `.env` file and set them as environment variables.

---

Powered by https://www.coinapi.io/
