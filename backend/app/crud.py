from sqlalchemy.orm import Session
from . import models, schemas, auth

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user or not auth.verify_password(password, user.hashed_password):
        return False
    return user

def create_chat(db: Session, user_id: int, analysis: dict):
    chat = models.Chat(user_id=user_id, analysis=analysis)
    db.add(chat)
    db.commit()
    db.refresh(chat)
    return chat

def get_chats(db: Session, user_id: int):
    return db.query(models.Chat).filter(models.Chat.user_id == user_id).all()

def get_chat(db: Session, chat_id: int):
    return db.query(models.Chat).filter(models.Chat.id == chat_id).first()

def delete_chat(db: Session, chat_id: int):
    chat = db.query(models.Chat).filter(models.Chat.id == chat_id).first()
    if chat:
        db.delete(chat)
        db.commit()
