from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
# from app.services.market_prices import get_all_prices, get_latest_price, scrape_and_store_prices
from app.services.market_prices import get_latest_price, get_all_prices

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
    return {"prices": prices}


# @app.post("/scrape", response_model=dict)
# def scrape_and_store(db: Session = Depends(get_db)):
#     """Scrape les prix actuels et les stocke dans la base de données."""
#     results = scrape_and_store_prices(db)
#     return {"scrape_results": results}


