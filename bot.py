import logging
import random
from telegram import Update
# CommandHandler ko import list mein add kiya hai
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, CommandHandler, filters
from config import TOKEN

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

RANDOM_REPLIES = [
    "Hello",
    "Kese ho aap?",
    "Hey",
    "Namaste!",
    "Hi there"
]

# 1. Yeh naya Start function hai
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Yahan aap bot ki information likh sakte hain
    bot_info = (
        "👋 **Namaste! Main ek Simple Random Bot hoon.**\n\n"
        "🤖 **Bot Info:**\n"
        "• Language: Python\n"
        "• Library: python-telegram-bot\n"
        "• Developer: Full Stack Dev\n\n"
        "💬 **Kaise use karein:**\n"
        "Bas mujhe koi bhi message bhejo (e.g. 'Hi'), aur main random reply karunga!"
    )
    # Markdown parse_mode use kar rahe hain taaki bold text dikhe
    await update.message.reply_text(bot_info, parse_mode='Markdown')

# 2. Random reply function (Same as before)
async def random_reply_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_text = random.choice(RANDOM_REPLIES)
    await update.message.reply_text(reply_text)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    # 3. Start Handler ko add kiya
    # Jab koi /start bhejege toh 'start' function chalega
    start_handler = CommandHandler('start', start)
    app.add_handler(start_handler)

    # Text Handler (Yeh normal messages ke liye hai)
    text_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), random_reply_handler)
    app.add_handler(text_handler)

    print("Bot start ho gaya hai...")
    app.run_polling()
    
