from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from models import User
from database import SessionLocal


TOKEN = "7217254061:AAEzRMDI0CVS09eAydyRyGMbJjzAZqAGpg4"


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    user = update.message.from_user
    telegram_id = user.id
    username = user.username
    first_name = user.first_name
    last_name = user.last_name

   
    db = next(get_db())

    
    existing_user = db.query(User).filter(User.telegram_id == telegram_id).first()
    if existing_user:
        await update.message.reply_text(
            f"Привет, {first_name}! Ты уже зарегистрирован.\n"
            f"Твой ID: {existing_user.id}\n"
            f"Username: {existing_user.username}"
        )
        return

    
    new_user = User(
        telegram_id=telegram_id,
        username=username,
        first_name=first_name,
        last_name=last_name
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

   
    await update.message.reply_text(
        f"Привет, {first_name}! Ты успешно зарегистрирован.\n"
        f"Твой ID: {new_user.id}\n"
        f"Username: {new_user.username}"
    )


def main():
    application = Application.builder().token(TOKEN).build()

    
    application.add_handler(CommandHandler("start", start))

    
    application.run_polling()

if __name__ == "__main__":
    main()