from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from services.market_prices import get_latest_price, get_all_prices
from datetime import datetime

app = FastAPI(title="Price Service API")

@app.get("/last_price/{currency}", response_model=dict)
def fetch_latest_price(currency: str, db: Session = Depends(get_db)):
    """Récupère le dernier prix pour une devise spécifique (EUR ou ETH)."""
    if currency not in ["EUR", "ETH"]:
        raise HTTPException(status_code=400, detail="Invalid currency. Use 'EUR' or 'ETH'.")

    price = get_latest_price(db)
    if not price:
        raise HTTPException(status_code=404, detail=f"No price data available for {currency}.")

    if currency == "EUR":
        return {
            "currency": "EUR",
            "price": price.price,
            "timestamp": price.timestamp
        }
    elif currency == "ETH":
        return {
            "currency": "ETH",
            "price": price.price_eth,
            "timestamp": price.timestamp
        }

@app.get("/prices")
def fetch_all_prices(db: Session = Depends(get_db)):
    prices = get_all_prices(db)
    
    if not prices:
        raise HTTPException(status_code=404, detail="No price data available")

    # Extraire les dates au format 'YYYY-MM-DD', les prix EUR et ETH
    dates = [price['timestamp'].strftime('%Y-%m-%d') for price in prices]  # Changer le format ici
    eur_prices = [price['price'] for price in prices]
    eth_prices = [price['price_eth'] for price in prices]
    
    return {
        "dates": dates,
        "eurPrices": eur_prices,
        "ethPrices": eth_prices
    }
