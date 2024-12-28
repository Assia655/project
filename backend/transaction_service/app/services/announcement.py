from sqlalchemy.orm import Session
from app.models.announcements import Announcement
from app.schemas.announcement import AnnouncementCreate, AnnouncementUpdate
from price_service.app.utils.market_price_scraper import scrape_market_price

def create_announcement(db: Session, announcement_data: AnnouncementCreate):
    """Créer une nouvelle annonce."""
    market_price = scrape_market_price("CARBON")
    announcement = Announcement(
        seller_id=announcement_data.seller_id,
        credit_amount=announcement_data.credit_amount,
        market_price_at_creation=market_price,
        currency="USD",
    )
    db.add(announcement)
    db.commit()
    db.refresh(announcement)
    return announcement

def update_announcement(db: Session, announcement_id: int, update_data: AnnouncementUpdate):
    """Mettre à jour une annonce."""
    announcement = db.query(Announcement).filter(Announcement.id == announcement_id).first()
    if not announcement:
        raise ValueError("Announcement not found")

    for key, value in update_data.dict(exclude_unset=True).items():
        setattr(announcement, key, value)

    db.commit()
    db.refresh(announcement)
    return announcement

def get_active_announcements(db: Session):
    """Récupérer toutes les annonces actives."""
    return db.query(Announcement).filter(Announcement.is_active == True).all()

def delete_announcement(db: Session, announcement_id: int):
    """Supprimer une annonce."""
    announcement = db.query(Announcement).filter(Announcement.id == announcement_id).first()
    if announcement:
        db.delete(announcement)
        db.commit()
        return True
    return False
