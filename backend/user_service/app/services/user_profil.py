from sqlalchemy.orm import Session
from app.models.user import UserProfile
from app.schemas import UserProfileCreate

def create_user_profile_service(db: Session, profile_data: UserProfileCreate):
    profile = UserProfile(
        user_id=profile_data.user_id,
        is_seller=profile_data.is_seller,
        is_buyer=profile_data.is_buyer
    )
    db.add(profile)
    db.commit()
    db.refresh(profile)
    return profile

def get_user_profile_service(db: Session, user_id: int):
    return db.query(UserProfile).filter(UserProfile.user_id == user_id).first()

def update_user_profile_service(db: Session, profile_id: int, is_seller: bool, is_buyer: bool):
    profile = db.query(UserProfile).filter(UserProfile.id == profile_id).first()
    if not profile:
        return None
    profile.is_seller = is_seller
    profile.is_buyer = is_buyer
    db.commit()
    db.refresh(profile)
    return profile

def delete_user_profile_service(db: Session, profile_id: int):
    profile = db.query(UserProfile).filter(UserProfile.id == profile_id).first()
    if profile:
        db.delete(profile)
        db.commit()
        return True
    return False
