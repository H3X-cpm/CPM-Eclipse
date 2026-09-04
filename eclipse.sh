#!/data/data/com.termux/files/usr/bin/bash

# ============================================
# CPM ECLIPSE - Main Launcher
# Version: 4.8.2
# Author: H3X
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
UNDERLINE='\033[4m'
REVERSE='\033[7m'

# ===== RGB COLORS =====
RGB_RED='\033[38;2;255;0;0m'
RGB_GREEN='\033[38;2;0;255;0m'
RGB_BLUE='\033[38;2;0;0;255m'
RGB_YELLOW='\033[38;2;255;255;0m'
RGB_PURPLE='\033[38;2;255;0;255m'
RGB_CYAN='\033[38;2;0;255;255m'
RGB_ORANGE='\033[38;2;255;165;0m'
RGB_PINK='\033[38;2;255;105;180m'

# ===== LOAD CONFIG =====
if [ -f config.json ]; then
    ADMIN_USERNAME=$(grep -o '"admin_username":"[^"]*"' config.json | cut -d'"' -f4)
else
    ADMIN_USERNAME="@H3X_cpm"
fi

# ===== LOAD VERSION =====
if [ -f version.txt ]; then
    VERSION=$(grep "CPM Eclipse" version.txt | head -1 | cut -d'v' -f2)
else
    VERSION="4.8.2"
fi

# ============================================
# FUNCTIONS
# ============================================

# Rainbow Text
rainbow_text() {
    local text="$1"
    local colors=($RGB_RED $RGB_YELLOW $RGB_GREEN $RGB_CYAN $RGB_BLUE $RGB_PURPLE)
    local len=${#text}
    for ((i=0; i<len; i++)); do
        echo -ne "${colors[i % 6]}${text:$i:1}"
    done
    echo -e "${NC}"
}

# Typewriter Effect
typewriter() {
    local text="$1"
    local delay=${2:-0.03}
    for ((i=0; i<${#text}; i++)); do
        echo -n "${text:$i:1}"
        sleep $delay
    done
    echo ""
}

# Progress Bar
progress_bar() {
    local duration=$1
    local width=40
    local progress=0
    
    echo -ne "${CYAN}Loading: [${NC}"
    for ((i=0; i<width; i++)); do echo -ne " "; done
    echo -ne "${CYAN}] 0%${NC}\r"
    
    for ((i=1; i<=duration; i++)); do
        sleep 0.05
        progress=$((i * 100 / duration))
        filled=$((progress * width / 100))
        echo -ne "${CYAN}Loading: [${NC}"
        for ((j=0; j<filled; j++)); do echo -ne "${GREEN}#${NC}"; done
        for ((j=filled; j<width; j++)); do echo -ne " "; done
        echo -ne "${CYAN}] ${progress}%${NC}\r"
    done
    echo ""
}

# ===== BANNER =====
banner() {
    clear
    echo ""
    echo -e "${RGB_RED}╔══════════════════════════════════════════════════════════╗${NC}"
    echo -e "${RGB_YELLOW}║                                                          ║${NC}"
    echo -e "${RGB_GREEN}║    ██████╗ ██████╗ ███╗   ███╗    ███████╗ ██████╗     ║${NC}"
    echo -e "${RGB_CYAN}║   ██╔════╝██╔═══██╗████╗ ████║    ██╔════╝██╔════╝     ║${NC}"
    echo -e "${RGB_BLUE}║   ██║     ██║   ██║██╔████╔██║    █████╗  ██║          ║${NC}"
    echo -e "${RGB_PURPLE}║   ██║     ██║   ██║██║╚██╔╝██║    ██╔══╝  ██║          ║${NC}"
    echo -e "${RGB_RED}║   ╚██████╗╚██████╔╝██║ ╚═╝ ██║    ███████╗╚██████╗     ║${NC}"
    echo -e "${RGB_YELLOW}║    ╚═════╝ ╚═════╝ ╚═╝     ╚═╝    ╚══════╝ ╚═════╝     ║${NC}"
    echo -e "${RGB_GREEN}║                                                          ║${NC}"
    echo -e "${RGB_CYAN}║                 CAR PARKING MULTIPLAYER                  ║${NC}"
    echo -e "${RGB_BLUE}║                    ADVANCED TOOL                         ║${NC}"
    echo -e "${RGB_PURPLE}║                                                          ║${NC}"
    echo -e "${RGB_YELLOW}║                  Version $VERSION                       ║${NC}"
    echo -e "${RGB_PINK}║                  Support: $ADMIN_USERNAME                ║${NC}"
    echo -e "${RGB_RED}║                                                          ║${NC}"
    echo -e "${RGB_RED}╚══════════════════════════════════════════════════════════╝${NC}"
    echo ""
}

# ===== CHECK AUTH =====
check_auth() {
    echo -e "${CYAN}🔐 Checking authentication...${NC}"
    
    if [ -f ~/.cpm_eclipse_user ]; then
        USER_ID=$(cat ~/.cpm_eclipse_user)
        echo -e "${GREEN}✅ Welcome back! User ID: $USER_ID${NC}"
    else
        echo -e "${YELLOW}📝 First time use!${NC}"
        echo -e "${CYAN}Please enter your Telegram User ID:${NC}"
        read -r USER_ID
        echo "$USER_ID" > ~/.cpm_eclipse_user
        echo -e "${GREEN}✅ User ID saved!${NC}"
    fi
    sleep 1
}

# ===== RUN CHEAT =====
run_cheat() {
    local cheat_type=$1
    
    echo -e "${CYAN}🚀 Launching $cheat_type...${NC}"
    progress_bar 15
    
    python main.py --mode "$cheat_type" --user "$USER_ID"
    
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✅ $cheat_type applied successfully!${NC}"
        echo -e "${YELLOW}📱 Check your game!${NC}"
    else
        echo -e "${RED}❌ Failed to apply $cheat_type${NC}"
    fi
    sleep 2
}

# ===== MAIN MENU =====
main_menu() {
    while true; do
        banner
        
        echo -e "${CYAN}${BOLD}╔══════════════════════════════════════════════════════════╗${NC}"
        echo -e "${PURPLE}${BOLD}║                     MAIN MENU                          ║${NC}"
        echo -e "${CYAN}${BOLD}╠══════════════════════════════════════════════════════════╣${NC}"
        echo -e "${GREEN}${BOLD}║  1. 💰 Money Boost                       ║${NC}"
        echo -e "${YELLOW}${BOLD}║  2. ⭐ XP Boost                          ║${NC}"
        echo -e "${BLUE}${BOLD}║  3. 🚗 Vehicle Unlock                    ║${NC}"
        echo -e "${PURPLE}${BOLD}║  4. 🚗 Unlock All Cars                  ║${NC}"
        echo -e "${CYAN}${BOLD}║  5. 📊 Check Stats                       ║${NC}"
        echo -e "${RGB_PINK}${BOLD}║  6. 🔑 My Info                          ║${NC}"
        echo -e "${RGB_ORANGE}${BOLD}║  7. 🔄 Update Script                    ║${NC}"
        echo -e "${RGB_RED}${BOLD}║  8. ❌ Exit                               ║${NC}"
        echo -e "${CYAN}${BOLD}╚══════════════════════════════════════════════════════════╝${NC}"
        echo ""
        echo -ne "${GREEN}➜ Select option: ${NC}"
        read -r choice

        case $choice in
            1)
                clear
                run_cheat "money"
                ;;
            2)
                clear
                run_cheat "rank"
                ;;
            3)
                clear
                echo -e "${BLUE}${BOLD}🚗 Enter Car ID:${NC}"
                read -r car_id
                run_cheat "vehicle"
                ;;
            4)
                clear
                run_cheat "all_cars"
                ;;
            5)
                clear
                echo -e "${CYAN}📊 Fetching stats...${NC}"
                progress_bar 10
                python main.py --mode stats --user "$USER_ID"
                echo ""
                echo -e "${RGB_PINK}Press Enter to continue...${NC}"
                read -r
                ;;
            6)
                clear
                echo -e "${PURPLE}🔑 Your Info${NC}"
                echo -e "${CYAN}════════════════════════════════════════════${NC}"
                echo -e "${GREEN}User ID: $(cat ~/.cpm_eclipse_user 2>/dev/null || echo 'Not set')${NC}"
                echo -e "${YELLOW}Support: $ADMIN_USERNAME${NC}"
                echo -e "${CYAN}Version: $VERSION${NC}"
                echo -e "${CYAN}════════════════════════════════════════════${NC}"
                echo ""
                echo -e "${RGB_PINK}Press Enter to continue...${NC}"
                read -r
                ;;
            7)
                clear
                echo -e "${CYAN}🔄 Updating script...${NC}"
                progress_bar 20
                git pull 2>/dev/null || echo -e "${YELLOW}⚠️ Git not found, skipping update${NC}"
                echo -e "${GREEN}✅ Update complete!${NC}"
                sleep 1
                ;;
            8)
                clear
                echo -e "${GREEN}${BOLD}👋 Goodbye!${NC}"
                echo -e "${PURPLE}${BLINK}✦ Thanks for using CPM Eclipse ✦${NC}"
                exit 0
                ;;
            *)
                echo -e "${RED}❌ Invalid option!${NC}"
                sleep 1
                ;;
        esac
    done
}

# ============================================
# START
# ============================================

main() {
    clear
    banner
    echo -e "${CYAN}${BOLD}Initializing CPM Eclipse...${NC}"
    progress_bar 20
    
    # Check if Python is installed
    if ! command -v python &> /dev/null; then
        echo -e "${RED}❌ Python not found!${NC}"
        echo -e "${YELLOW}📦 Run ./install.sh first${NC}"
        exit 1
    fi
    
    # Check if main.py exists
    if [ ! -f main.py ]; then
        echo -e "${RED}❌ main.py not found!${NC}"
        echo -e "${YELLOW}📦 Run ./install.sh first${NC}"
        exit 1
    fi
    
    check_auth
    clear
    main_menu
}

# Run the script
main
