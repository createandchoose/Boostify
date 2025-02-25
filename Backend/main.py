# main.py
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal, engine
import models
import auth
import telegram_integration

# Инициализация FastAPI приложения
app = FastAPI()

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency для работы с базой данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Модели Pydantic для валидации
class UserCreate(BaseModel):
    telegram_id: int
    username: str
    role: str

class RatingUpdate(BaseModel):
    user_id: int
    points: int

# Эндпоинты для пользователей
@app.post("/users/register")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # Интеграция с Telegram для аутентификации
    if telegram_integration.validate_user(user.telegram_id):
        new_user = models.User(
            telegram_id=user.telegram_id, 
            username=user.username, 
            role=user.role
        )
        db.add(new_user)
        db.commit()
        return {"status": "success", "user_id": new_user.id}
    raise HTTPException(status_code=403, detail="Invalid Telegram authentication")

@app.post("/rating/update")
def update_user_rating(rating: RatingUpdate, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == rating.user_id).first()
    if user:
        user.points += rating.points
        db.commit()
        return {"status": "success", "new_points": user.points}
    raise HTTPException(status_code=404, detail="User not found")

# models.py - SQLAlchemy модели
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(Integer, unique=True)
    username = Column(String, index=True)
    role = Column(String)
    points = Column(Float, default=0)

# database.py - Конфигурация базы данных
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://user:password@localhost/telegram_app"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# telegram_integration.py
import telegram
from telegram.ext import Application

class TelegramIntegration:
    def __init__(self, bot_token):
        self.bot = telegram.Bot(token=bot_token)
    
    def validate_user(self, telegram_id):
        # Логика проверки пользователя в Telegram
        try:
            user = self.bot.get_chat_member(chat_id, telegram_id)
            return user is not None
        except Exception:
            return False
    
    def send_notification(self, user_id, message):
        self.bot.send_message(chat_id=user_id, text=message)

# auth.py - Авторизация и безопасность
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel

class Settings(BaseModel):
    authjwt_secret_key: str = "your-secret-key"

@AuthJWT.load_config
def get_config():
    return Settings()