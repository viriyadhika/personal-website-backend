from telegram import Update
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
)

from app.auth.services.otp import check_otp
from app.auth.services.signup import register_telegram

ASK_USERNAME = 0
AUTHENTICATE_OTP = 1


# Step 1: /register command
async def start_register(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message == None:
        return
    await update.message.reply_text("Please enter your username:")
    return ASK_USERNAME


# Step 2: Receive username
async def receive_username(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message == None:
        return
    username = update.message.text

    if context.user_data == None:
        return
    context.user_data["username"] = username
    await update.message.reply_text(f"Generate OTP from the main website: {username}")
    return AUTHENTICATE_OTP


# Step 3: Receive OTP
async def receive_otp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if (
        update.message == None
        or context.user_data == None
        or update.effective_user == None
    ):
        return

    otp = update.message.text
    if otp == None:
        return

    username = context.user_data.get("username")
    if username == None:
        return

    is_valid_otp = check_otp(username, otp)
    if is_valid_otp:
        register_telegram(username, update.effective_user.id)
        await update.message.reply_text(
            f"Registered this account with user: {username}"
        )
        return ConversationHandler.END
    else:
        await update.message.reply_text("OTP is wrong")
        return ConversationHandler.END


# Optional: cancel registration
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message == None:
        return
    await update.message.reply_text("Registration cancelled.")
    return ConversationHandler.END
