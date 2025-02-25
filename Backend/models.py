from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(Integer, unique=True, index=True)  # Уникальный ID пользователя в Telegram
    username = Column(String, unique=True, index=True)     # Username из Telegram
    first_name = Column(String)                            # Имя пользователя
    last_name = Column(String, nullable=True)              # Фамилия пользователя (может быть пустой)