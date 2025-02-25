from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from models import User
from database import SessionLocal

# Токен вашего бота
TOKEN = "7217254061:AAEzRMDI0CVS09eAydyRyGMbJjzAZqAGpg4"

# Функция для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Получаем данные о пользователе из Telegram
    user = update.message.from_user
    telegram_id = user.id
    username = user.username
    first_name = user.first_name
    last_name = user.last_name

    # Получаем сессию базы данных
    db = next(get_db())

    # Проверяем, зарегистрирован ли пользователь уже
    existing_user = db.query(User).filter(User.telegram_id == telegram_id).first()
    if existing_user:
        await update.message.reply_text(
            f"Привет, {first_name}! Ты уже зарегистрирован.\n"
            f"Твой ID: {existing_user.id}\n"
            f"Username: {existing_user.username}"
        )
        return

    # Создаем нового пользователя
    new_user = User(
        telegram_id=telegram_id,
        username=username,
        first_name=first_name,
        last_name=last_name
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Отправляем подтверждение
    await update.message.reply_text(
        f"Привет, {first_name}! Ты успешно зарегистрирован.\n"
        f"Твой ID: {new_user.id}\n"
        f"Username: {new_user.username}"
    )

# Запуск бота
def main():
    application = Application.builder().token(TOKEN).build()

    # Регистрируем команды
    application.add_handler(CommandHandler("start", start))

    # Запускаем бота
    application.run_polling()

if __name__ == "__main__":
    main()