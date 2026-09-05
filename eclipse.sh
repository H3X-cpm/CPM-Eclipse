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
# LOGIN FUNCTION
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
    else
        echo -e "${YELLOW}📝 Enter your Telegram User ID:${NC}"
        echo -e "${CYAN}💡 Get your ID from @ECLIPSE_BOT (send /start)${NC}"
        read -r USER_ID
        echo "$USER_ID" > "$USER_ID_FILE"
        echo -e "${GREEN}✅ User ID saved!${NC}"
    fi
    
    echo ""
    echo -e "${CYAN}🔐 Verifying...${NC}"
    sleep 1
    
    if [ -f "$LOGIN_FILE" ]; then
        echo -e "${GREEN}✅ Login successful!${NC}"
        sleep 1
        return 0
    else
        echo -e "${RED}❌ Login failed!${NC}"
        rm -f "$LOGIN_FILE"
        sleep 2
        return 1
    fi
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
            echo -e "${GREEN}${BOLD}║ 1. 🔐 Login                             ║${NC}"
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
            echo -e "${CYAN}${BOLD}╔══════════════════════════════════════════════════════════════════════════╗${NC}"
            echo -e "${PURPLE}${BOLD}║                          ECLIPSE MENU                                  ║${NC}"
            echo -e "${CYAN}${BOLD}╠══════════════════════════════════════════════════════════════════════════╣${NC}"
            echo -e "${GREEN}${BOLD}║  💰 MONEY & COINS                    │  🔓 UNLOCKABLES                  ║${NC}"
            echo -e "${CYAN}${BOLD}║────────────────────────────────────────┼──────────────────────────────────║${NC}"
            echo -e "${YELLOW}${BOLD}║  1. Set Money (10 pts)               │  9. Unlock All Cars (50 pts)    ║${NC}"
            echo -e "${YELLOW}${BOLD}║  2. Set Coins (10 pts)               │ 10. Unlock Lamborghinis (30)    ║${NC}"
            echo -e "${YELLOW}${BOLD}║                                     │ 11. Unlock Paid Cars (40 pts)   ║${NC}"
            echo -e "${YELLOW}${BOLD}║  👤 ACCOUNT                         │ 12. Unlock W16 Engine (25 pts)  ║${NC}"
            echo -e "${CYAN}${BOLD}║────────────────────────────────────────┼──────────────────────────────────║${NC}"
            echo -e "${YELLOW}${BOLD}║  3. Set Name (5 pts)                │ 13. Unlock All Horns (20 pts)   ║${NC}"
            echo -e "${YELLOW}${BOLD}║  4. Set ID (5 pts)                  │ 14. Unlock Houses (25 pts)      ║${NC}"
            echo -e "${YELLOW}${BOLD}║  5. Set King Rank (20 pts)          │ 15. Unlock Smoke (20 pts)       ║${NC}"
            echo -e "${YELLOW}${BOLD}║  6. Clone Account (70 pts)          │ 16. Unlock Wheels (20 pts)      ║${NC}"
            echo -e "${YELLOW}${BOLD}║  7. Change Email (10 pts)           │ 17. Unlock Animations (15 pts)  ║${NC}"
            echo -e "${YELLOW}${BOLD}║  8. Change Password (10 pts)        │ 18. Unlock Crown (15 pts)       ║${NC}"
            echo -e "${CYAN}${BOLD}║────────────────────────────────────────┼──────────────────────────────────║${NC}"
            echo -e "${YELLOW}${BOLD}║  🏁 RACING                          │ 19. Unlock CLS (25 pts)         ║${NC}"
            echo -e "${CYAN}${BOLD}║────────────────────────────────────────┼──────────────────────────────────║${NC}"
            echo -e "${YELLOW}${BOLD}║ 20. Set Race Wins (15 pts)          │ 21. Unlock Siren Cars (35 pts)  ║${NC}"
            echo -e "${YELLOW}${BOLD}║ 22. Set Race Loses (15 pts)         │                                 ║${NC}"
            echo -e "${CYAN}${BOLD}║────────────────────────────────────────┼──────────────────────────────────║${NC}"
            echo -e "${YELLOW}${BOLD}║  🚗 CAR MODS                        │ 🔧 CUSTOM CAR                   ║${NC}"
            echo -e "${CYAN}${BOLD}║────────────────────────────────────────┼──────────────────────────────────║${NC}"
            echo -e "${YELLOW}${BOLD}║ 23. Hack Car Speed (25 pts)         │ 30. Custom HP (15 pts)          ║${NC}"
            echo -e "${YELLOW}${BOLD}║ 24. Speed All Cars (50 pts)         │ 31. Custom Angle (10 pts)       ║${NC}"
            echo -e "${YELLOW}${BOLD}║ 25. Modify All Cars (75 pts)        │ 32. Custom Tire (10 pts)        ║${NC}"
            echo -e "${YELLOW}${BOLD}║ 26. Copy Livery (20 pts)            │ 33. Custom Mileage (10 pts)     ║${NC}"
            echo -e "${YELLOW}${BOLD}║ 27. Remove Bumpers (15 pts)         │ 34. Custom Brake (10 pts)       ║${NC}"
            echo -e "${YELLOW}${BOLD}║ 28. Stance Camber (10 pts)          │ 35. Rear Bumper (10 pts)        ║${NC}"
            echo -e "${CYAN}${BOLD}║────────────────────────────────────────┼──────────────────────────────────║${NC}"
            echo -e "${YELLOW}${BOLD}║  👕 CUSTOMIZATION                   │ 36. Front Bumper (10 pts)       ║${NC}"
            echo -e "${CYAN}${BOLD}║────────────────────────────────────────┼──────────────────────────────────║${NC}"
            echo -e "${YELLOW}${BOLD}║ 37. Male Equipment (15 pts)         │ 43. Delete Friends (5 pts)      ║${NC}"
            echo -e "${YELLOW}${BOLD}║ 38. Female Equipment (15 pts)       │ 44. Set Plates (10 pts)         ║${NC}"
            echo -e "${YELLOW}${BOLD}║ 39. Male Hats (10 pts)              │ 45. Delete Account (Free)       ║${NC}"
            echo -e "${YELLOW}${BOLD}║ 40. Male Tops (10 pts)              │ 46. Register Account (Free)     ║${NC}"
            echo -e "${YELLOW}${BOLD}║ 41. Female Tops (10 pts)            │ 47. Get Player Stats (Free)     ║${NC}"
            echo -e "${YELLOW}${BOLD}║ 42. Remove Male Head (10 pts)       │                                 ║${NC}"
            echo -e "${CYAN}${BOLD}╠══════════════════════════════════════════════════════════════════════════╣${NC}"
            echo -e "${RED}${BOLD}║ 0. Exit                                    │ 99. 🚪 Logout                 ║${NC}"
            echo -e "${CYAN}${BOLD}╚══════════════════════════════════════════════════════════════════════════╝${NC}"
            echo ""
            echo -ne "${GREEN}➜ Select option: ${NC}"
            read -r choice

            case $choice in
                1) clear; run_cheat "money" ;;
                2) clear; run_cheat "coins" ;;
                3) clear; run_cheat "name" ;;
                4) clear; run_cheat "id" ;;
                5) clear; run_cheat "rank" ;;
                6) clear; run_cheat "clone" ;;
                7) clear; run_cheat "change_email" ;;
                8) clear; run_cheat "change_password" ;;
                9) clear; run_cheat "all_cars" ;;
                10) clear; run_cheat "lamborghinis" ;;
                11) clear; run_cheat "paid_cars" ;;
                12) clear; run_cheat "w16" ;;
                13) clear; run_cheat "horns" ;;
                14) clear; run_cheat "houses" ;;
                15) clear; run_cheat "smoke" ;;
                16) clear; run_cheat "wheels" ;;
                17) clear; run_cheat "animations" ;;
                18) clear; run_cheat "crown" ;;
                19) clear; run_cheat "cls" ;;
                20) clear; run_cheat "wins" ;;
                21) clear; run_cheat "siren" ;;
                22) clear; run_cheat "loses" ;;
                23) clear; run_cheat "hack_speed" ;;
                24) clear; run_cheat "speed_all" ;;
                25) clear; run_cheat "modify_all" ;;
                26) clear; run_cheat "copy_livery" ;;
                27) clear; run_cheat "remove_bumpers" ;;
                28) clear; run_cheat "stance" ;;
                30) clear; run_cheat "max_max1" ;;
                31) clear; run_cheat "max_max2" ;;
                32) clear; run_cheat "millage" ;;
                33) clear; run_cheat "brake" ;;
                34) clear; run_cheat "rear_bumper" ;;
                35) clear; run_cheat "front_bumper" ;;
                36) clear; run_cheat "male_equip" ;;
                37) clear; run_cheat "female_equip" ;;
                38) clear; run_cheat "hat_m" ;;
                39) clear; run_cheat "top_m" ;;
                40) clear; run_cheat "top_f" ;;
                41) clear; run_cheat "rmhm" ;;
                42) clear; run_cheat "rmhfm" ;;
                43) clear; run_cheat "delete_friends" ;;
                44) clear; run_cheat "plates" ;;
                45) clear; run_cheat "delete" ;;
                46) clear; run_cheat "register" ;;
                47) clear; run_cheat "stats" ;;
                99) do_logout; clear; banner; echo -e "${GREEN}✅ Logged out!${NC}"; sleep 1 ;;
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