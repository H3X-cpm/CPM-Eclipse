#!/usr/bin/env python3
# bot.py - ECLIPSE Telegram Bot
# Version: 4.8.2

import json
import os
import datetime
import secrets
import time
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# ===== CONFIGURATION =====
BOT_TOKEN = "8964642365:AAEsqDeuBtgTnNf-bCB6PlcnIR09wu9h_tA"
ADMIN_ID = "6386858720"
DATA_FILE = "users.json"

# ===== DATABASE =====
def load_users():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(DATA_FILE, 'w') as f:
        json.dump(users, f, indent=2)

# ===== LOGIN REQUESTS =====
login_requests = {}

# ============================================
# ADMIN COMMANDS
# ============================================

async def add_points(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Admin: /addpoints USER_ID AMOUNT"""
    user_id = str(update.effective_user.id)
    
    if user_id != ADMIN_ID:
        await update.message.reply_text("❌ Admin only command.")
        return
    
    if not context.args or len(context.args) < 2:
        await update.message.reply_text(
            "📋 Usage: /addpoints USER_ID AMOUNT\n\n"
            "Example: /addpoints 6386858720 100"
        )
        return
    
    target_user_id = context.args[0]
    try:
        amount = int(context.args[1])
    except ValueError:
        await update.message.reply_text("❌ Please enter a valid number.")
        return
    
    users = load_users()
    
    if target_user_id not in users:
        await update.message.reply_text(f"❌ User ID {target_user_id} not found.")
        return
    
    users[target_user_id]['points'] = users[target_user_id].get('points', 0) + amount
    save_users(users)
    
    try:
        await update.get_bot().send_message(
            chat_id=target_user_id,
            text=f"✅ Points Added! 🎉\n\n"
                 f"📦 +{amount} points added to your account!\n"
                 f"⭐ New Balance: **{users[target_user_id]['points']}** points\n\n"
                 f"Use /menu to start using your points!",
            parse_mode="Markdown"
        )
    except:
        pass
    
    await update.message.reply_text(
        f"✅ Points Added!\n\n"
        f"👤 User: @{users[target_user_id]['username']}\n"
        f"🆔 ID: {target_user_id}\n"
        f"📦 Added: +{amount} points\n"
        f"⭐ New Balance: {users[target_user_id]['points']} points"
    )

async def deduct_points(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Admin: /deductpoints USER_ID AMOUNT"""
    user_id = str(update.effective_user.id)
    
    if user_id != ADMIN_ID:
        await update.message.reply_text("❌ Admin only command.")
        return
    
    if not context.args or len(context.args) < 2:
        await update.message.reply_text(
            "📋 Usage: /deductpoints USER_ID AMOUNT\n\n"
            "Example: /deductpoints 6386858720 50"
        )
        return
    
    target_user_id = context.args[0]
    try:
        amount = int(context.args[1])
    except ValueError:
        await update.message.reply_text("❌ Please enter a valid number.")
        return
    
    users = load_users()
    
    if target_user_id not in users:
        await update.message.reply_text(f"❌ User ID {target_user_id} not found.")
        return
    
    current = users[target_user_id].get('points', 0)
    if current < amount:
        await update.message.reply_text(f"❌ Insufficient points! User has {current}, trying to deduct {amount}")
        return
    
    users[target_user_id]['points'] = current - amount
    save_users(users)
    
    try:
        await update.get_bot().send_message(
            chat_id=target_user_id,
            text=f"📤 Points Deducted\n\n"
                 f"📦 -{amount} points deducted from your account.\n"
                 f"⭐ New Balance: **{users[target_user_id]['points']}** points",
            parse_mode="Markdown"
        )
    except:
        pass
    
    await update.message.reply_text(
        f"✅ Points Deducted!\n\n"
        f"👤 User: @{users[target_user_id]['username']}\n"
        f"🆔 ID: {target_user_id}\n"
        f"📦 Deducted: -{amount} points\n"
        f"⭐ New Balance: {users[target_user_id]['points']} points"
    )

async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Admin: /balance USER_ID"""
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
        await update.message.reply_text(f"❌ User {target_user_id} not found.")
        return
    
    data = users[target_user_id]
    await update.message.reply_text(
        f"📊 User Balance\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"👤 User: @{data['username']}\n"
        f"🆔 ID: {target_user_id}\n"
        f"⭐ Points: **{data.get('points', 0)}**\n"
        f"📅 Joined: {data.get('created', 'Unknown')}"
    )

async def list_users(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Admin: /listusers"""
    user_id = str(update.effective_user.id)
    
    if user_id != ADMIN_ID:
        await update.message.reply_text("❌ Admin only command.")
        return
    
    users = load_users()
    
    if not users:
        await update.message.reply_text("📊 No users registered yet.")
        return
    
    msg = "📊 **Registered Users**\n━━━━━━━━━━━━━━━━━━━━━━\n"
    for uid, data in users.items():
        msg += f"👤 @{data['username']} - ⭐{data.get('points', 0)} pts\n"
        msg += f"🆔 `{uid}`\n━━━━━━━━━━━━━━━━━━━━━━\n"
    
    await update.message.reply_text(msg, parse_mode="Markdown")

# ============================================
# LOGIN SYSTEM
# ============================================

async def login_confirm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle login confirmation button"""
    query = update.callback_query
    await query.answer()
    
    user_id = str(query.from_user.id)
    code = query.data.replace("login_", "")
    
    # Check if this login request exists
    if code in login_requests and login_requests[code]['user_id'] == user_id:
        # Create login session file for Termux to detect
        with open(f"/tmp/login_{code}.confirmed", "w") as f:
            f.write(user_id)
        
        await query.edit_message_text(
            "✅ **Login Confirmed!** 🎉\n\n"
            "You have successfully logged in to Eclipse.\n"
            "🔐 Your session is now active.\n\n"
            "You can now use the tool in Termux."
        )
    else:
        await query.edit_message_text(
            "❌ **Login Failed**\n\n"
            "This login request has expired or is invalid.\n"
            "Please try again from Termux."
        )

async def login_deny(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle login denial"""
    query = update.callback_query
    await query.answer()
    
    code = query.data.replace("login_deny_", "")
    
    # Remove the login request
    if code in login_requests:
        del login_requests[code]
    
    await query.edit_message_text(
        "❌ **Login Denied**\n\n"
        "If this wasn't you, your account is safe.\n"
        "Please ignore this request."
    )

# ============================================
# USER COMMANDS
# ============================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start command"""
    user_id = str(update.effective_user.id)
    username = update.effective_user.username or "Unknown"
    
    users = load_users()
    
    if user_id not in users:
        # Create user
        users[user_id] = {
            "username": username,
            "points": 0,
            "created": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "tier": "free"
        }
        save_users(users)
        
        await update.message.reply_text(
            f"✅ **Welcome to Eclipse!** 🎉\n\n"
            f"👤 User: @{username}\n"
            f"🆔 ID: `{user_id}`\n"
            f"⭐ Points: 0\n\n"
            f"📋 To get started:\n"
            f"1️⃣ Contact @H3X_cpm to buy points\n"
            f"2️⃣ Run Eclipse in Termux\n"
            f"3️⃣ Login with your User ID\n\n"
            f"🔗 Channel: @cpmeclipse\n"
            f"💬 Community: @cpmeclipse_chat",
            parse_mode="Markdown"
        )
    else:
        await update.message.reply_text(
            f"✅ **Welcome back!** 👋\n\n"
            f"👤 User: @{username}\n"
            f"🆔 ID: `{user_id}`\n"
            f"⭐ Points: **{users[user_id].get('points', 0)}**\n\n"
            f"Run Eclipse in Termux to start using your points!",
            parse_mode="Markdown"
        )

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show main menu"""
    user_id = str(update.effective_user.id)
    users = load_users()
    
    if user_id not in users:
        await update.message.reply_text("❌ Please use /start first.")
        return
    
    data = users[user_id]
    
    keyboard = [
        [InlineKeyboardButton("👤 My Profile", callback_data="profile")],
        [InlineKeyboardButton("💰 Buy Points", callback_data="buy")],
        [InlineKeyboardButton("📊 My Stats", callback_data="stats")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        f"🌙 **Eclipse Menu**\n\n"
        f"👤 User: @{data['username']}\n"
        f"⭐ Points: **{data.get('points', 0)}**\n\n"
        f"Select an option:",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show user profile"""
    query = update.callback_query
    await query.answer()
    
    user_id = str(query.from_user.id)
    users = load_users()
    
    if user_id not in users:
        await query.edit_message_text("❌ User not found.")
        return
    
    data = users[user_id]
    
    await query.edit_message_text(
        f"👤 **Your Profile**\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"👤 Username: @{data['username']}\n"
        f"🆔 ID: `{user_id}`\n"
        f"⭐ Points: **{data.get('points', 0)}**\n"
        f"📅 Joined: {data.get('created', 'Unknown')}\n"
        f"🏷️ Tier: {data.get('tier', 'free').upper()}\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"📩 Support: @H3X_cpm",
        parse_mode="Markdown"
    )

async def buy_points(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Buy points menu"""
    query = update.callback_query
    await query.answer()
    
    keyboard = [
        [InlineKeyboardButton("💳 PayPal", url="https://paypal.me/Th141206")],
        [InlineKeyboardButton("🔙 Back", callback_data="menu")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        f"💰 **Buy Points**\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"**Tiers:**\n"
        f"🥉 Bronze - £1.99 (200 pts/month)\n"
        f"🥈 Silver - £3.99 (400 pts/month)\n"
        f"🥇 Gold - £5.99 (600 pts/month)\n"
        f"💎 Platinum - £14.99 (2000 pts/month)\n\n"
        f"💳 **Payment:** PayPal\n"
        f"📩 **Contact:** @H3X_cpm\n\n"
        f"⚠️ Points added within 24 hours\n"
        f"❌ No refunds after points added",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show stats"""
    query = update.callback_query
    await query.answer()
    
    user_id = str(query.from_user.id)
    users = load_users()
    
    if user_id not in users:
        await query.edit_message_text("❌ User not found.")
        return
    
    data = users[user_id]
    
    await query.edit_message_text(
        f"📊 **Your Stats**\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"⭐ Points: **{data.get('points', 0)}**\n"
        f"🏷️ Tier: {data.get('tier', 'free').upper()}\n"
        f"📅 Joined: {data.get('created', 'Unknown')}\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"💡 Use points in Eclipse!\n"
        f"🔙 Use /menu to go back",
        parse_mode="Markdown"
    )

# ============================================
# MAIN
# ============================================

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    
    # Commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", menu))
    app.add_handler(CommandHandler("addpoints", add_points))
    app.add_handler(CommandHandler("deductpoints", deduct_points))
    app.add_handler(CommandHandler("balance", balance))
    app.add_handler(CommandHandler("listusers", list_users))
    
    # Callbacks
    app.add_handler(CallbackQueryHandler(profile, pattern="profile"))
    app.add_handler(CallbackQueryHandler(buy_points, pattern="buy"))
    app.add_handler(CallbackQueryHandler(stats, pattern="stats"))
    app.add_handler(CallbackQueryHandler(menu, pattern="menu"))
    app.add_handler(CallbackQueryHandler(login_confirm, pattern="login_"))
    app.add_handler(CallbackQueryHandler(login_deny, pattern="login_deny_"))
    
    print("🌙 Eclipse Bot is running!")
    print("📱 Open Telegram and send /start")
    print("━━━━━━━━━━━━━━━━━━━━━━")
    print("📋 Admin Commands:")
    print("  /addpoints USER_ID AMOUNT - Add points")
    print("  /deductpoints USER_ID AMOUNT - Deduct points")
    print("  /balance USER_ID - Check balance")
    print("  /listusers - List all users")
    print("━━━━━━━━━━━━━━━━━━━━━━")
    app.run_polling()

if __name__ == "__main__":
    main()
