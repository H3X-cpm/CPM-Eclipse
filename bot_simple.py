import asyncio
asyncio.set_event_loop(asyncio.new_event_loop())

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import json
import os
import datetime

BOT_TOKEN = "8964642365:AAH2U6Uyfd1oIAMVa4GsysrbrUlT558Y_N8"
ADMIN_ID = "6386858720"
DATA_FILE = "users.json"

def load_users():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(DATA_FILE, 'w') as f:
        json.dump(users, f, indent=2)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    username = update.effective_user.username or "Unknown"
    users = load_users()
    
    if user_id not in users:
        users[user_id] = {
            "username": username,
            "points": 100,
            "created": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        save_users(users)
        await update.message.reply_text(
            f"✅ Welcome to Eclipse! 🎉\n\n"
            f"User: @{username}\n"
            f"ID: {user_id}\n"
            f"Free Points: 100\n\n"
            f"Contact @H3X_cpm to buy more points!"
        )
    else:
        await update.message.reply_text(
            f"✅ Welcome back! 👋\n\n"
            f"User: @{username}\n"
            f"ID: {user_id}\n"
            f"Points: {users[user_id].get('points', 0)}"
        )

async def login_confirm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    code = query.data.replace("login_", "")
    
    # WRITE THE FILE SO TERMUX CAN SEE IT
    with open(f"/data/data/com.termux/files/home/tmp/login_{code}.confirmed", "w") as f:
        f.write("confirmed")
    
    await query.edit_message_text(
        "✅ Login Confirmed! 🎉\n\n"
        "You can now use Eclipse in Termux."
    )

async def login_deny(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("❌ Login Denied.")

async def add_points(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    if user_id != ADMIN_ID:
        await update.message.reply_text("Admin only.")
        return
    if not context.args or len(context.args) < 2:
        await update.message.reply_text("Usage: /addpoints USER_ID AMOUNT")
        return
    target = context.args[0]
    try:
        amount = int(context.args[1])
    except:
        await update.message.reply_text("Invalid amount.")
        return
    users = load_users()
    if target not in users:
        await update.message.reply_text("User not found.")
        return
    users[target]['points'] = users[target].get('points', 0) + amount
    save_users(users)
    await update.message.reply_text(f"✅ Added {amount} points!")

async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    if user_id != ADMIN_ID:
        await update.message.reply_text("Admin only.")
        return
    if not context.args:
        await update.message.reply_text("Usage: /balance USER_ID")
        return
    target = context.args[0]
    users = load_users()
    if target not in users:
        await update.message.reply_text("User not found.")
        return
    data = users[target]
    await update.message.reply_text(f"👤 @{data['username']} - ⭐ {data.get('points', 0)} points")

async def list_users(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    if user_id != ADMIN_ID:
        await update.message.reply_text("Admin only.")
        return
    users = load_users()
    if not users:
        await update.message.reply_text("No users.")
        return
    msg = "📊 Registered Users\n━━━━━━━━━━━━━━━━━━━━━━\n"
    for uid, data in users.items():
        msg += f"👤 @{data['username']} - ⭐{data.get('points', 0)} pts\n"
    await update.message.reply_text(msg)

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("addpoints", add_points))
    app.add_handler(CommandHandler("balance", balance))
    app.add_handler(CommandHandler("listusers", list_users))
    app.add_handler(CallbackQueryHandler(login_confirm, pattern="login_"))
    app.add_handler(CallbackQueryHandler(login_deny, pattern="login_deny_"))
    
    # Create tmp folder
    os.makedirs("/data/data/com.termux/files/home/tmp", exist_ok=True)
    
    print("🌙 Eclipse Bot is running!")
    print("📱 Open Telegram and send /start")
    print("━━━━━━━━━━━━━━━━━━━━━━")
    print("📋 Admin Commands:")
    print("  /addpoints USER_ID AMOUNT - Add points")
    print("  /balance USER_ID - Check balance")
    print("  /listusers - List all users")
    print("━━━━━━━━━━━━━━━━━━━━━━")
    app.run_polling()

if __name__ == "__main__":
    main()