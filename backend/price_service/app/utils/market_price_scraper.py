import requests
from app.db.session import SessionLocal
from app.models.market_prices import MarketPrice

COINGECKO_API_URL = "https://api.coingecko.com/api/v3/simple/price"

def fetch_market_price_from_api(currency: str) -> float:
    """Fetch market price for a currency."""
    currency_map = {
        "MCO2": "moss-carbon-credit",
        "ETH": "ethereum",
        "USD": "usd"
    }

    if currency.upper() == "USD":
        return 1.0

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

def scrape_and_store_prices(db: SessionLocal):
    """Fetch and store prices."""
    currencies = ["MCO2", "ETH", "USD"]
    results = []

    for currency in currencies:
        try:
            price = fetch_market_price_from_api(currency)
            market_price = MarketPrice(currency=currency, price=price)
            db.add(market_price)
            db.commit()
            results.append({"currency": currency, "price": price, "status": "success"})
        except Exception as e:
            results.append({"currency": currency, "error": str(e), "status": "failed"})

    return results
