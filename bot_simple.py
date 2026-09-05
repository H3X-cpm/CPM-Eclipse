import asyncio
asyncio.set_event_loop(asyncio.new_event_loop())

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import json
import os
import datetime

BOT_TOKEN = "8964642365:AAEsqDeuBtgTnNf-bCB6PlcnIR09wu9h_tA"
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
            f"👤 User: @{username}\n"
            f"🆔 ID: `{user_id}`\n"
            f"⭐ Free Points: **100**\n\n"
            f"Contact @H3X_cpm to buy more points!",
            parse_mode="Markdown"
        )
    else:
        await update.message.reply_text(
            f"✅ Welcome back! 👋\n\n"
            f"👤 User: @{username}\n"
            f"🆔 ID: `{user_id}`\n"
            f"⭐ Points: **{users[user_id].get('points', 0)}**",
            parse_mode="Markdown"
        )

async def add_points(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    
    if user_id != ADMIN_ID:
        await update.message.reply_text("❌ Admin only command.")
        return
    
    if not context.args or len(context.args) < 2:
        await update.message.reply_text("📋 Usage: /addpoints USER_ID AMOUNT")
        return
    
    target_user_id = context.args[0]
    try:
        amount = int(context.args[1])
    except:
        await update.message.reply_text("❌ Invalid amount.")
        return
    
    users = load_users()
    
    if target_user_id not in users:
        await update.message.reply_text(f"❌ User {target_user_id} not found.")
        return
    
    users[target_user_id]['points'] = users[target_user_id].get('points', 0) + amount
    save_users(users)
    
    await update.message.reply_text(
        f"✅ Points Added!\n\n"
        f"👤 User: @{users[target_user_id]['username']}\n"
        f"📦 Added: +{amount} points\n"
        f"⭐ New Balance: {users[target_user_id]['points']}"
    )

async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    
    if user_id != ADMIN_ID:
        await update.message.reply_text("❌ Admin only command.")
        return
    
    if not context.args:
        await update.message.reply_text("📋 Usage: /balance USER_ID")
        return
    
    target_user_id = context.args[0]
    users = load_users()
    
    if target_user_id not in users:
        await update.message.reply_text(f"❌ User not found.")
        return
    
    data = users[target_user_id]
    await update.message.reply_text(
        f"📊 User Balance\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"👤 User: @{data['username']}\n"
        f"⭐ Points: {data.get('points', 0)}"
    )

async def list_users(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    
    if user_id != ADMIN_ID:
        await update.message.reply_text("❌ Admin only command.")
        return
    
    users = load_users()
    
    if not users:
        await update.message.reply_text("📊 No users yet.")
        return
    
    msg = "📊 Registered Users\n━━━━━━━━━━━━━━━━━━━━━━\n"
    for uid, data in users.items():
        msg += f"👤 @{data['username']} - ⭐{data.get('points', 0)} pts\n"
        msg += f"🆔 {uid}\n━━━━━━━━━━━━━━━━━━━━━━\n"
    
    await update.message.reply_text(msg)

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("addpoints", add_points))
    app.add_handler(CommandHandler("balance", balance))
    app.add_handler(CommandHandler("listusers", list_users))
    
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
