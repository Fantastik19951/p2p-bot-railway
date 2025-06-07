
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет, Женя! Я готов фиксировать сделки и показывать курсы. Введи /курс или /сделка.")

async def kurs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📊 Лучшие курсы:
Binance: 39.10 → 39.80
Bybit: 39.00 → 39.75
(данные статичны, подключим API позже)")

async def profit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💰 Прибыль за сегодня: +18.30$
За неделю: +54.20$")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app = ApplicationBuilder().token("PASTE_YOUR_TOKEN_HERE").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("курс", kurs))
    app.add_handler(CommandHandler("профит", profit))
    app.run_polling()
