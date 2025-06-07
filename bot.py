import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет, Женя! Я готов. Используй команды:\n/kurs — курсы\n/profit — прибыль")

async def kurs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 Лучшие курсы:\nBinance: 39.10 → 39.80\nBybit: 39.00 → 39.75\n(данные пока статичны)"
    )

async def profit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💰 Прибыль за сегодня: +18.30$")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    token = os.environ.get("BOT_TOKEN")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("kurs", kurs))
    app.add_handler(CommandHandler("profit", profit))
    app.run_polling()