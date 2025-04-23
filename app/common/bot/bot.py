from telegram.ext import (
    ApplicationBuilder,
)
from .handlers import handlers
from app.env import BOT_TOKEN


class Bot:
    def __init__(self):
        self.app = ApplicationBuilder().token(BOT_TOKEN).build()

    def start(self):
        self.app.add_handlers(handlers)

        print("Bot is running...")
        self.app.run_polling()

    def stop(self):
        self.app.stop_running()


bot = Bot()
