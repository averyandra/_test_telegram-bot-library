import asyncio
import logging
import sys
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import config as conf

# logging config
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

BOT_TOKEN = conf.bot_token

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """handling /start command"""
    user = update.effective_user
    await update.message.reply_text(f"Halo {user.first_name}! Bot running....")
    print(f"\n[SYSTEM] User {user.first_name} (@{user.username}) run bot. Chat ID: {update.effective_chat.id}")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user_name = update.effective_user.first_name
    text_received = update.message.text

    print(f"\n{'='*40}")
    print(f"incoming message from {user_name} (ID: {chat_id}):")
    print(f"👉 \"{text_received}\"")
    print(f"{'='*40}")
    def get_cli_input():
        return input("reply : ")

    reply_text = await asyncio.to_thread(get_cli_input)

    if reply_text.strip():
        await context.bot.send_message(chat_id=chat_id, text=reply_text)
        print(f"✅ Reply successfully sent to {user_name}.")
    else:
        print("⚠️ Empty input, no reply sent.")

def main():
    """running bot"""
    if BOT_TOKEN == "YOUR_BOT_TOKEN_HERE":
        print("Error: Please enter your valid BOT_TOKEN first!")
        sys.exit(1)

    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("The bot is running... Send a message to your bot on Telegram.")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()