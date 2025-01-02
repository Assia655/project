from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.market_prices import get_all_prices, get_latest_price, scrape_and_store_prices

app = FastAPI(title="Price Service API")

@app.get("/prices/{currency}", response_model=dict)
def fetch_latest_price(currency: str, db: Session = Depends(get_db)):
    """Récupère le dernier prix pour une devise spécifique."""
    price = get_latest_price(db, currency)
    if not price:
        raise HTTPException(status_code=404, detail=f"No price found for {currency}")
    return {"currency": price.currency, "price": price.price, "timestamp": price.timestamp}

@app.get("/prices", response_model=list)
def fetch_all_prices(db: Session = Depends(get_db)):
    """Récupère tous les derniers prix disponibles."""
    prices = get_all_prices(db)
    return prices

@app.post("/scrape", response_model=dict)
def scrape_and_store(db: Session = Depends(get_db)):
    """Scrape les prix actuels et les stocke dans la base de données."""
    results = scrape_and_store_prices(db)
    return {"scrape_results": results}
