from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from main import get_db, read_user

# Токен вашего бота
TOKEN = "7217254061:AAEzRMDI0CVS09eAydyRyGMbJjzAZqAGpg4"

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привет! Я твой бот.')

# Команда /get_user
async def get_user_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_id = int(context.args[0])
        db = next(get_db())
        user = read_user(user_id, db)
        if user:
            await update.message.reply_text(f"User: {user.username}, Email: {user.email}")
        else:
            await update.message.reply_text("User not found")
    except (IndexError, ValueError):
        await update.message.reply_text("Usage: /get_user <user_id>")

def main():
    # Создаем приложение и передаем токен
    application = Application.builder().token(TOKEN).build()

    # Регистрируем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("get_user", get_user_info))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()