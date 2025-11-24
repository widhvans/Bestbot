import logging
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from config import TOKEN

# Logging setup (Error tracking ke liye)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Yeh wo list hai jisme se bot random reply choose karega
RANDOM_REPLIES = [
    "Hello",
    "Kese ho aap?",
    "Hey",
    "Namaste!",
    "Hi there"
]

# Function: Jo user ke message ka reply karega
async def random_reply_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # User ka message aate hi random text choose karega
    reply_text = random.choice(RANDOM_REPLIES)
    
    # User ko wapas reply send karega
    await update.message.reply_text(reply_text)

if __name__ == '__main__':
    # Application build kar rahe hain config file ke token se
    app = ApplicationBuilder().token(TOKEN).build()

    # Message Handler: Yeh sirf text messages ko sunega (Commands ko ignore karega)
    # filters.TEXT & (~filters.COMMAND) ka matlab hai sirf normal text messages
    text_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), random_reply_handler)
    
    app.add_handler(text_handler)

    print("Bot start ho gaya hai...")
    # Bot ko run karna
    app.run_polling()
  
