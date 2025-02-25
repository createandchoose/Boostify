from database import engine
from models import Base

# Создаем все таблицы в базе данных
Base.metadata.create_all(bind=engine)

print("Таблицы созданы!")