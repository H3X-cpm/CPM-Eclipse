#!/data/data/com.termux/files/usr/bin/bash

# ============================================
# ECLIPSE - Main Launcher
# Version: 4.8.2
# ============================================

# ===== COLORS =====
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
NC='\033[0m'
BOLD='\033[1m'
BLINK='\033[5m'

# ===== RGB COLORS =====
RGB_RED='\033[38;2;255;0;0m'
RGB_GREEN='\033[38;2;0;255;0m'
RGB_BLUE='\033[38;2;0;0;255m'
RGB_YELLOW='\033[38;2;255;255;0m'
RGB_PURPLE='\033[38;2;255;0;255m'
RGB_CYAN='\033[38;2;0;255;255m'

# ===== LOAD VERSION =====
VERSION="4.8.2"

# ===== BOT TOKEN =====
BOT_TOKEN="8964642365:AAH2U6Uyfd1oIAMVa4GsysrbrUlT558Y_N8"

# ===== LOGIN STATUS =====
LOGIN_FILE="$HOME/.eclipse_login"
USER_ID_FILE="$HOME/.eclipse_user"

# ============================================
# CHECK IF LOGGED IN
# ============================================

is_logged_in() {
    if [ -f "$LOGIN_FILE" ]; then
        return 0
    else
        return 1
    fi
}

# ============================================
# TELEGRAM LOGIN FUNCTION
# ============================================

do_login() {
    clear
    echo -e "${CYAN}${BOLD}╔════════════════════════════════════════════╗${NC}"
    echo -e "${PURPLE}${BOLD}║              LOGIN REQUIRED               ║${NC}"
    echo -e "${CYAN}${BOLD}╚════════════════════════════════════════════╝${NC}"
    echo ""
    
    if [ -f "$USER_ID_FILE" ]; then
        USER_ID=$(cat "$USER_ID_FILE")
        echo -e "${GREEN}✅ User ID found: $USER_ID${NC}"
        echo -e "${YELLOW}Press Enter to continue, or type a new ID${NC}"
        echo -ne "${GREEN}➜ User ID [${USER_ID}]: ${NC}"
        read -r input_id
        if [ ! -z "$input_id" ]; then
            USER_ID="$input_id"
            echo "$USER_ID" > "$USER_ID_FILE"
        fi
    else
        echo -e "${YELLOW}📝 Enter your Telegram User ID:${NC}"
        echo -e "${CYAN}💡 Send /start to @CPM_Eclipse_Bot to get your ID${NC}"
        echo -ne "${GREEN}➜ User ID: ${NC}"
        read -r USER_ID
        echo "$USER_ID" > "$USER_ID_FILE"
        echo -e "${GREEN}✅ User ID saved!${NC}"
    fi
    
    echo ""
    echo -e "${CYAN}📤 Sending login request to Telegram...${NC}"
    
    # Generate a random login code
    LOGIN_CODE=$(date +%s | sha256sum | head -c 8)
    
    # Send login request via Telegram bot with inline keyboard
    python3 -c "
import requests

bot_token = '$BOT_TOKEN'
user_id = '$USER_ID'
login_code = '$LOGIN_CODE'

msg_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
msg_data = {
    'chat_id': user_id,
    'text': f'🔐 Login Request\\n\\nSomeone is trying to log in to Eclipse.\\n\\nClick the button below to confirm:',
    'reply_markup': {
        'inline_keyboard': [
            [
                {'text': '✅ Confirm Login', 'callback_data': f'login_{login_code}'},
                {'text': '❌ Deny', 'callback_data': f'login_deny_{login_code}'}
            ]
        ]
    }
}

response = requests.post(msg_url, data=msg_data)
result = response.json()

if result.get('ok'):
    print('SUCCESS')
else:
    print('FAILED: ' + str(result))
"
    
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✅ Login request sent!${NC}"
        echo -e "${YELLOW}💡 Check your Telegram for a login confirmation!${NC}"
        echo ""
        echo -e "${CYAN}⏳ Waiting for confirmation...${NC}"
        
        # Wait for user to confirm on Telegram
        for i in {1..30}; do
            sleep 1
            if [ -f "/tmp/login_$LOGIN_CODE.confirmed" ]; then
                echo -e "${GREEN}✅ Login confirmed via Telegram!${NC}"
                rm -f "/tmp/login_$LOGIN_CODE.confirmed"
                echo "$USER_ID" > "$USER_ID_FILE"
                echo '{"logged_in": true}' > "$LOGIN_FILE"
                return 0
            fi
            echo -ne "${CYAN}.${NC}"
        done
        
        echo ""
        echo -e "${RED}❌ Login timeout! Please try again.${NC}"
    else
        echo -e "${RED}❌ Failed to send login request.${NC}"
        echo -e "${YELLOW}💡 Make sure the bot is running.${NC}"
    fi
    
    return 1
}

# ============================================
# LOGOUT FUNCTION
# ============================================

do_logout() {
    rm -f "$LOGIN_FILE"
    echo -e "${GREEN}✅ Logged out successfully!${NC}"
    sleep 1
}

# ============================================
# BANNER
# ============================================

banner() {
    clear
    echo ""
    echo -e "${CYAN}╔════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║            🌙 ECLIPSE v${VERSION}              ║${NC}"
    echo -e "${CYAN}║    Advanced Car Parking Tool            ║${NC}"
    echo -e "${PURPLE}║    Support: @H3X_cpm                     ║${NC}"
    
    if is_logged_in; then
        echo -e "${GREEN}║    Status: ✅ Logged In                  ║${NC}"
    else
        echo -e "${RED}║    Status: ❌ Not Logged In              ║${NC}"
    fi
    
    echo -e "${CYAN}╚════════════════════════════════════════════╝${NC}"
    echo ""
}

# ============================================
# RUN CHEAT
# ============================================

run_cheat() {
    local cheat_type=$1
    
    if ! is_logged_in; then
        echo -e "${RED}❌ Please login first!${NC}"
        sleep 1
        return
    fi
    
    echo -e "${CYAN}🚀 Launching $cheat_type...${NC}"
    
    python main.py --mode "$cheat_type"
    
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✅ $cheat_type applied successfully!${NC}"
        echo -e "${YELLOW}📱 Check your game!${NC}"
    else
        echo -e "${RED}❌ Failed to apply $cheat_type${NC}"
    fi
    sleep 2
}

# ============================================
# MAIN MENU
# ============================================

main_menu() {
    while true; do
        banner
        
        if ! is_logged_in; then
            echo -e "${CYAN}${BOLD}╔════════════════════════════════════════════╗${NC}"
            echo -e "${PURPLE}${BOLD}║            MAIN MENU                      ║${NC}"
            echo -e "${CYAN}${BOLD}╠════════════════════════════════════════════╣${NC}"
            echo -e "${GREEN}${BOLD}║ 1. 🔐 Login via Telegram                ║${NC}"
            echo -e "${RED}${BOLD}║ 2. ❌ Exit                               ║${NC}"
            echo -e "${CYAN}${BOLD}╚════════════════════════════════════════════╝${NC}"
            echo ""
            echo -ne "${GREEN}➜ Select option: ${NC}"
            read -r choice
            case $choice in
                1) do_login ;;
                2) clear; echo -e "${GREEN}👋 Goodbye!${NC}"; exit 0 ;;
                *) echo -e "${RED}❌ Invalid option!${NC}"; sleep 1 ;;
            esac
        else
            echo -e "${CYAN}${BOLD}╔════════════════════════════════════════════╗${NC}"
            echo -e "${PURPLE}${BOLD}║            ECLIPSE MENU                  ║${NC}"
            echo -e "${CYAN}${BOLD}╠════════════════════════════════════════════╣${NC}"
            echo -e "${GREEN}${BOLD}║ 1. 💰 Set Money (10 pts)                ║${NC}"
            echo -e "${YELLOW}${BOLD}║ 2. ⭐ Set Coins (10 pts)                ║${NC}"
            echo -e "${BLUE}${BOLD}║ 3. 👤 Set Name (5 pts)                 ║${NC}"
            echo -e "${PURPLE}${BOLD}║ 4. 🔓 Unlock All Cars (50 pts)         ║${NC}"
            echo -e "${CYAN}${BOLD}║ 5. 📊 Get Player Stats (Free)          ║${NC}"
            echo -e "${RED}${BOLD}║ 0. Exit                               ║${NC}"
            echo -e "${CYAN}${BOLD}╚════════════════════════════════════════════╝${NC}"
            echo ""
            echo -ne "${GREEN}➜ Select option: ${NC}"
            read -r choice

            case $choice in
                1) clear; run_cheat "money" ;;
                2) clear; run_cheat "coins" ;;
                3) clear; run_cheat "name" ;;
                4) clear; run_cheat "all_cars" ;;
                5) clear; python main.py --mode stats; echo ""; echo -e "${PURPLE}Press Enter...${NC}"; read -r ;;
                0) clear; echo -e "${GREEN}👋 Goodbye!${NC}"; exit 0 ;;
                *) echo -e "${RED}❌ Invalid option!${NC}"; sleep 1 ;;
            esac
        fi
    done
}

# ============================================
# START
# ============================================

main() {
    clear
    banner
    echo -e "${CYAN}Initializing Eclipse...${NC}"
    sleep 1
    clear
    main_menu
}

main