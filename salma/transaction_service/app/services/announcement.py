from sqlalchemy.orm import Session
from app.models.announcements import Announcement
from app.schemas.announcement import AnnouncementCreate, AnnouncementUpdate
from app.utils.price_service_api import get_price

def create_announcement(db: Session, announcement_data: AnnouncementCreate):
    # Récupérer le prix actuel du marché pour MCO2 en USD
    market_price = get_price("MCO2")
    
    # Créer une annonce sans la colonne currency
    announcement = Announcement(
        seller_id=announcement_data.seller_id,
        credit_amount=announcement_data.credit_amount,
        market_price_at_creation=market_price,
        is_active=True  # Par défaut, l'annonce est active
    )
    db.add(announcement)
    db.commit()
    db.refresh(announcement)
    return announcement

def get_announcement_by_id(db: Session, announcement_id: int):
    return db.query(Announcement).filter(Announcement.id == announcement_id).first()

def get_active_announcements(db: Session):
    return db.query(Announcement).filter(Announcement.is_active == True).all()

def update_announcement(db: Session, announcement_id: int, update_data: AnnouncementUpdate):
    announcement = db.query(Announcement).filter(Announcement.id == announcement_id).first()
    if not announcement:
        raise ValueError("Announcement not found")
    for key, value in update_data.dict(exclude_unset=True).items():
        setattr(announcement, key, value)
    db.commit()
    db.refresh(announcement)
    return announcement

def delete_announcement(db: Session, announcement_id: int):
    announcement = db.query(Announcement).filter(Announcement.id == announcement_id).first()
    if announcement:
        db.delete(announcement)
        db.commit()
        return True
    return False
