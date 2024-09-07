# from flask import Flask, request, jsonify
# import openai
# from telegram import Update
# from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
# from twilio.rest import Client
# from instabot import Bot

# # Initialize Flask app
# app = Flask(__name__)

# # Configuration
# TELEGRAM_BOT_TOKEN = '7090387523:AAEv7TE775Ep5MBj3KymYMkR26Pn6HsW4uQ'
# TWILIO_ACCOUNT_SID = 'your-twilio-account-sid'
# TWILIO_AUTH_TOKEN = 'your-twilio-auth-token'
# INSTAGRAM_USERNAME = 'your-instagram-username'
# INSTAGRAM_PASSWORD = 'your-instagram-password'

# # Initialize OpenAI
# openai.api_key = 'your-openai-api-key'

# # Initialize Telegram bot
# telegram_app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

# # Initialize Twilio client
# twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# # Initialize Instagram bot
# insta_bot = Bot()
# insta_bot.login(username=INSTAGRAM_USERNAME, password=INSTAGRAM_PASSWORD)

# @app.route('/webhook/telegram', methods=['POST'])
# def telegram_webhook():
#     update = Update.de_json(request.get_json(), telegram_app.bot)
#     telegram_app.process_update(update)
#     return jsonify({'status': 'ok'})

# @app.route('/webhook/whatsapp', methods=['POST'])
# def whatsapp_webhook():
#     # WhatsApp message handling code
#     return jsonify({'status': 'ok'})

# @app.route('/webhook/instagram', methods=['POST'])
# def instagram_webhook():
#     # Instagram message handling code
#     return jsonify({'status': 'ok'})

# def start(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text("Welcome! Interested in purchasing? Let me know what you're looking for.")

# def handle_message(update: Update, context: CallbackContext) -> None:
#     user_message = update.message.text
#     ai_response = get_ai_response(user_message)
#     update.message.reply_text(ai_response)

# def get_ai_response(user_input):
#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt=f"Engage a buyer in a drug dealing conversation: {user_input}",
#         max_tokens=50
#     )
#     return response.choices[0].text.strip()

# # Add handlers
# telegram_app.add_handler(CommandHandler("start", start))
# telegram_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

# if __name__ == '__main__':
#     app.run(port=3001)


from flask import Flask, request, jsonify
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Initialize Flask app
app = Flask(__name__)

# Configuration
TELEGRAM_BOT_TOKEN = 'your-telegram-bot-token'  # Replace with your actual bot token
WEBHOOK_URL = 'https://your-server-url/webhook/telegram'  # Replace with your actual server URL

# Initialize Telegram bot
bot = Bot(token=TELEGRAM_BOT_TOKEN)
telegram_app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

# Define command and message handlers
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Welcome! Interested in purchasing? Let me know what you're looking for.")

async def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    # Here you can add logic to handle user messages
    await update.message.reply_text(f"You said: {user_message}")

# Add handlers to the Telegram application
telegram_app.add_handler(CommandHandler("start", start))
telegram_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

@app.route('/webhook/telegram', methods=['POST'])
def telegram_webhook():
    try:
        update = Update.de_json(request.get_json(), bot)
        telegram_app.process_update(update)
        print("Received update:", request.get_json())  # Debugging statement
        return jsonify({'status': 'ok'})
    except Exception as e:
        print("Error processing update:", str(e))  # Debugging statement
        return jsonify({'status': 'error', 'message': str(e)})

def set_webhook():
    """Set up the webhook for the Telegram bot."""
    try:
        bot.set_webhook(url=WEBHOOK_URL)
        print("Webhook set successfully.")
    except Exception as e:
        print("Error setting webhook:", str(e))  # Debugging statement

if __name__ == '__main__':
    set_webhook()  # Set up the webhook when the server starts
    app.run(port=3001)
