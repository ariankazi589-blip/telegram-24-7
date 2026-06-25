import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import asyncio

TOKEN = "8946434748:AAG7bEF5LrYOPZ2digjA40bTZhvnFOR1ZoY"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('বস আমি জেগে আছি! 24/7 🔥')

async def joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('কি খবর বস? TECNO রে হারায় দিছি 😎')

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("joke", joke))
    print("Bot চালু হইছে বস...")
    await app.run_polling()

if __name__ == '__main__':
    asyncio.run(main())