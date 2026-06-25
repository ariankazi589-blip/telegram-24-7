import os
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("8946434748:AAG7bEF5LrYOPZ2digjA40bTZhvnFOR1ZoY")

if not TOKEN:
    print("বস ERROR: TOKEN পাই নাই!")
    exit(1)

JOKES = [
    "স্যার: বলো তো, পৃথিবী গোল কেন?\nছাত্র: স্যার, চারকোণা বানাইতে গিয়া কেউ পারে নাই 😂",
    "মা: পড়তে বস\nআমি: মা, WiFi নাই\nমা: বই পড়\nআমি: মা, চার্জ নাই 🔋",
    "বন্ধু: তোর GF কই?\nআমি: সার্ভারে আপলোড দিছি, লোডিং হইতেছে 😂",
    "টিচার: তুমি স্কুলে আসো না কেন?\nআমি: স্যার, রাস্তা হারায় যাই 😂"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("বস Bot চালু! /joke দাও 🔥")

async def joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(JOKES))

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("joke", joke))

print("Bot চালু হইছে বস...")
app.run_polling()mport
