from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# Токен берём из переменной окружения (безопасно)
TOKEN = os.environ.get('BOT_TOKEN')

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = """
👋 Привет! Я бот *ДГТУ.комфорт*

Я помогу тебе ориентироваться в университете:
• Найти коворкинги для учёбы
• Узнать где поесть и что в меню
• Понять куда идти за справками
• Получить ответы на частые вопросы

Нажми /help чтобы увидеть все команды.
"""
    await update.message.reply_text(welcome_text, parse_mode='Markdown')

# Команда /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """
📋 *Список команд:*

/start — О боте
/help — Список команд
/coworking — Коворкинги ДГТУ
/food — Столовые и буфеты
/navigation — Куда идти за чем
/faq — Частые вопросы

Больше функций скоро! 🚀
"""
    await update.message.reply_text(help_text, parse_mode='Markdown')

# Запуск бота
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    print("Бот запущен...")
    app.run_polling()
