from app.auth.bot.register import (
    receive_otp,
    start_register,
    receive_username,
    ASK_USERNAME,
    AUTHENTICATE_OTP,
    cancel,
)
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import (
    ContextTypes,
    MessageHandler,
    filters,
    CommandHandler,
    ConversationHandler,
)


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[KeyboardButton("/register")]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    if update.message == None:
        return

    await update.message.reply_text(
        f"Hello, Please register", reply_markup=reply_markup
    )


handlers = [
    CommandHandler("start", start_command),
    ConversationHandler(
        entry_points=[CommandHandler("register", start_register)],
        states={
            ASK_USERNAME: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, receive_username),
            ],
            AUTHENTICATE_OTP: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, receive_otp)
            ],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    ),
]
