import requests
from app.db.session import SessionLocal
from app.models.market_prices import MarketPrice

COINGECKO_API_URL = "https://api.coingecko.com/api/v3/simple/price"

def fetch_market_price_from_api(currency: str) -> float:
    """
    Fetch the market price of a currency from the CoinGecko API.

    Args:
        currency (str): The currency for which to fetch the price (e.g., "moss-carbon-credit", "ethereum").

    Returns:
        float: The current price of the currency in USD.

    Raises:
        ValueError: If the API fails to fetch the price.
    """
    # Map local currency names to CoinGecko IDs
    currency_map = {
        "MCO2": "moss-carbon-credit",
        "ETH": "ethereum",
        "USD": "usd"  # USD doesn't require a fetch, it is a fixed value
    }

    if currency.upper() == "USD":
        return 1.0  # USD is a reference fixed value

    if currency.upper() not in currency_map:
        raise ValueError(f"Currency {currency} is not supported for API fetching.")

    try:
        response = requests.get(
            COINGECKO_API_URL,
            params={"ids": currency_map[currency.upper()], "vs_currencies": "usd"}
        )
        response.raise_for_status()
        data = response.json()
        return data[currency_map[currency.upper()]]["usd"]
    except Exception as e:
        raise ValueError(f"Failed to fetch {currency} price from API: {e}")

def store_scraped_price(currency: str):
    """
    Fetch and store the market price for a currency in the database.

    Args:
        currency (str): The currency for which to fetch and store the price (e.g., "MCO2", "ETH", "USD").
    """
    db = SessionLocal()
    try:
        price = fetch_market_price_from_api(currency)
        market_price = MarketPrice(currency=currency, price=price)
        db.add(market_price)
        db.commit()
        print(f"Successfully stored {currency} price: {price}")
    except Exception as e:
        print(f"Failed to store price for {currency}: {e}")
    finally:
        db.close()

# Example usage
if __name__ == "__main__":
    store_scraped_price("MCO2")
    store_scraped_price("ETH")
    store_scraped_price("USD")
