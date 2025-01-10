from fastapi import HTTPException  # Importer depuis fastapi
import subprocess
from utils.scrapp import get_eth_price_on_date
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from db.session import get_db  # Importing get_db from session.py
from models.market_prices import CarbonEmissionsData, MarketPrice
from schemas.market_price import MarketPriceCreate,MarketPriceResponse
from utils.scrapp import scrape_and_insert_data


# def create_market_price(db: Session, price: float):
#     """Créer une nouvelle entrée de prix dans la base de données."""
#     try:
#         market_price = MarketPrice(
#             currency=currency.upper(),
#             price=price
#         )
#         db.add(market_price)
#         db.commit()
#         db.refresh(market_price)
#         return market_price
#     except SQLAlchemyError as e:
#         db.rollback()
#         raise ValueError(f"Failed to create market price entry: {e}")


def get_latest_price(db: Session):

    scrape_and_insert_data()
    """
    Récupère la dernière donnée de prix pour les émissions de carbone.
    """
    return (
        db.query(CarbonEmissionsData)
        .order_by(CarbonEmissionsData.timestamp.desc())
        .first()
    )


def get_all_prices(db: Session):
    
    scrape_and_insert_data()
    """
    Récupère tous les prix disponibles triés par date.
    """
    prices = db.query(CarbonEmissionsData).order_by(CarbonEmissionsData.timestamp.desc()).all()
    return [
        {
            "date": price.date,
            "price": price.price,
            "change_percent": price.change_percent,
            "price_eth": price.price_eth,
            "timestamp": price.timestamp
        }
        for price in prices
    ]

