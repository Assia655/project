from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.db.session import get_db  # Importing get_db from session.py
from app.models.market_prices import MarketPrice
from app.utils.market_price_scraper import fetch_market_price_from_api
from app.schemas.market_price import MarketPriceCreate,MarketPriceResponse


def create_market_price(db: Session, currency: str, price: float):
    """Créer une nouvelle entrée de prix dans la base de données."""
    try:
        market_price = MarketPrice(
            currency=currency.upper(),
            price=price
        )
        db.add(market_price)
        db.commit()
        db.refresh(market_price)
        return market_price
    except SQLAlchemyError as e:
        db.rollback()
        raise ValueError(f"Failed to create market price entry: {e}")


def get_latest_price(db: Session, currency: str):
    """
    Récupère le dernier prix de marché pour une devise spécifique.
    """
    try:
        return (
            db.query(MarketPrice)
            .filter(MarketPrice.currency == currency.upper())
            .order_by(MarketPrice.timestamp.desc())
            .first()
        )
    except SQLAlchemyError as e:
        raise ValueError(f"Failed to fetch latest price for {currency}: {e}")


def get_all_prices(db: Session):
    """
    Récupère les derniers prix de toutes les devises disponibles.
    """
    prices = db.query(MarketPrice).order_by(MarketPrice.timestamp.desc()).all()
    # Transforme les objets SQLAlchemy en dictionnaires via Pydantic
    return [MarketPriceResponse.from_orm(price).dict() for price in prices]


def scrape_and_store_prices(db: Session):
    """
    Scrape les prix pour les devises supportées (MCO2, ETH, USD) et les stocke dans la base de données.
    """
    currencies = ["MCO2", "ETH", "USD"]
    results = []

    for currency in currencies:
        try:
            # Récupérer le prix à l'aide de l'API officielle
            price = fetch_market_price_from_api(currency)

            # Créer une nouvelle entrée dans la base de données
            create_market_price(db, currency, price)

            results.append({"currency": currency, "price": price, "status": "success"})
        except Exception as e:
            results.append({"currency": currency, "error": str(e), "status": "failed"})

    return results
