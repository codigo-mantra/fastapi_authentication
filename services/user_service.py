from sqlalchemy.orm import Session
import pyotp
from userapi import models
from resources import schemas
from settings.security import pwd_context


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.email == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.User(
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        hashed_password=hashed_password,
        otp_secret=pyotp.random_base32(),
        user_role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user_self(db: Session, current_user: schemas.User, user_update: schemas.UserUpdate):
    db_user = get_user(db, current_user.id)
    print(db_user, "iiiidddddddddddddd")
    db_user.email = user_update.email
    db_user.first_name = user_update.first_name
    db_user.last_name = user_update.last_name
    db_user.hashed_password = pwd_context.hash(user_update.password)
    db.commit()
    db.refresh(db_user)
    return db_user
