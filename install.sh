#!/data/data/com.termux/files/usr/bin/bash

# ============================================
# CPM ECLIPSE - Installation Script
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

# ===== BANNER =====
clear
echo -e "${CYAN}${BOLD}"
echo "╔══════════════════════════════════════════════════════════╗"
echo "║                                                          ║"
echo "║    ██████╗ ██████╗ ███╗   ███╗    ███████╗ ██████╗     ║"
echo "║   ██╔════╝██╔═══██╗████╗ ████║    ██╔════╝██╔════╝     ║"
echo "║   ██║     ██║   ██║██╔████╔██║    █████╗  ██║          ║"
echo "║   ██║     ██║   ██║██║╚██╔╝██║    ██╔══╝  ██║          ║"
echo "║   ╚██████╗╚██████╔╝██║ ╚═╝ ██║    ███████╗╚██████╗     ║"
echo "║    ╚═════╝ ╚═════╝ ╚═╝     ╚═╝    ╚══════╝ ╚═════╝     ║"
echo "║                                                          ║"
echo "║                 INSTALLATION SCRIPT                      ║"
echo "║                      v4.8.2                             ║"
echo "║                                                          ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo -e "${NC}"

# ===== CHECK TERMUX =====
echo -e "${CYAN}🔍 Checking Termux environment...${NC}"

# Check if running in Termux
if [ ! -d "/data/data/com.termux" ]; then
    echo -e "${RED}❌ This script must be run in Termux!${NC}"
    echo -e "${YELLOW}📱 Please install Termux from F-Droid:${NC}"
    echo -e "${BLUE}   https://f-droid.org/en/packages/com.termux/${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Termux detected!${NC}"
sleep 1

# ===== UPDATE PACKAGES =====
echo -e "${CYAN}📦 Updating package lists...${NC}"
pkg update -y || {
    echo -e "${RED}❌ Failed to update packages!${NC}"
    echo -e "${YELLOW}💡 Check your internet connection${NC}"
    exit 1
}

echo -e "${GREEN}✅ Package lists updated!${NC}"
sleep 1

# ===== INSTALL DEPENDENCIES =====
echo -e "${CYAN}📦 Installing dependencies...${NC}"

# List of packages to install
packages=(
    "python"
    "python-pip"
    "git"
    "nano"
    "curl"
    "wget"
    "unzip"
    "openssh"
)

for pkg in "${packages[@]}"; do
    echo -e "${YELLOW}📥 Installing $pkg...${NC}"
    pkg install $pkg -y 2>/dev/null || {
        echo -e "${RED}⚠️ Failed to install $pkg, continuing...${NC}"
    }
done

echo -e "${GREEN}✅ All packages installed!${NC}"
sleep 1

# ===== INSTALL PYTHON PACKAGES =====
echo -e "${CYAN}🐍 Installing Python packages...${NC}"

python_packages=(
    "colorama"
    "requests"
    "pystyle"
    "rich"
    "python-telegram-bot"
    "flask"
    "flask-cors"
)

for pkg in "${python_packages[@]}"; do
    echo -e "${YELLOW}📥 Installing $pkg...${NC}"
    pip install $pkg 2>/dev/null || {
        echo -e "${RED}⚠️ Failed to install $pkg, continuing...${NC}"
    }
done

echo -e "${GREEN}✅ Python packages installed!${NC}"
sleep 1

# ===== CHECK FILES =====
echo -e "${CYAN}📂 Checking files...${NC}"

required_files=(
    "main.py"
    "cpmeclipse.py"
    "car_ids.json"
    "eclipse.sh"
    "config.example.json"
    "requirements.txt"
    "version.txt"
)

missing_files=()
for file in "${required_files[@]}"; do
    if [ ! -f "$file" ]; then
        missing_files+=("$file")
    fi
done

if [ ${#missing_files[@]} -gt 0 ]; then
    echo -e "${YELLOW}⚠️ Missing files:${NC}"
    for file in "${missing_files[@]}"; do
        echo -e "   - $file"
    done
    echo -e "${YELLOW}💡 Make sure you're in the correct folder${NC}"
else
    echo -e "${GREEN}✅ All files present!${NC}"
fi
sleep 1

# ===== CREATE CONFIG =====
echo -e "${CYAN}⚙️ Setting up configuration...${NC}"

if [ ! -f "config.json" ]; then
    cp config.example.json config.json
    echo -e "${GREEN}✅ config.json created from template!${NC}"
    echo -e "${YELLOW}📝 Please edit config.json with your details:${NC}"
    echo -e "${BLUE}   nano config.json${NC}"
else
    echo -e "${GREEN}✅ config.json already exists!${NC}"
fi
sleep 1

# ===== MAKE SCRIPTS EXECUTABLE =====
echo -e "${CYAN}🔧 Making scripts executable...${NC}"

chmod +x *.sh 2>/dev/null
chmod +x *.py 2>/dev/null

echo -e "${GREEN}✅ Scripts are now executable!${NC}"
sleep 1

# ===== CREATE USER FILE =====
echo -e "${CYAN}👤 Setting up user...${NC}"

if [ ! -f ~/.cpm_eclipse_user ]; then
    echo -e "${YELLOW}📝 First time setup!${NC}"
    echo -e "${CYAN}Please enter your Telegram User ID:${NC}"
    read -r user_id
    echo "$user_id" > ~/.cpm_eclipse_user
    echo -e "${GREEN}✅ User ID saved!${NC}"
else
    echo -e "${GREEN}✅ User already configured!${NC}"
fi
sleep 1

# ===== CHECK CAR_IDS.JSON =====
echo -e "${CYAN}🚗 Checking car_ids.json...${NC}"

if [ -f "car_ids.json" ]; then
    car_count=$(cat car_ids.json | grep -o "," | wc -l)
    echo -e "${GREEN}✅ car_ids.json loaded! ($car_count cars)${NC}"
else
    echo -e "${YELLOW}⚠️ car_ids.json not found!${NC}"
    echo -e "${BLUE}   Creating default...${NC}"
    echo '[]' > car_ids.json
fi
sleep 1

# ===== VERSION CHECK =====
echo -e "${CYAN}📌 Checking version...${NC}"

if [ -f "version.txt" ]; then
    version=$(grep "CPM Eclipse" version.txt | head -1 | cut -d'v' -f2)
    echo -e "${GREEN}✅ Version: $version${NC}"
else
    echo -e "${YELLOW}⚠️ version.txt not found${NC}"
fi
sleep 1

# ===== CHECK INTERNET =====
echo -e "${CYAN}🌐 Checking internet connection...${NC}"

if ping -c 1 google.com >/dev/null 2>&1; then
    echo -e "${GREEN}✅ Internet connection detected!${NC}"
else
    echo -e "${YELLOW}⚠️ No internet connection!${NC}"
    echo -e "${YELLOW}💡 Some features may not work${NC}"
fi
sleep 1

# ===== COMPLETE =====
clear
echo -e "${GREEN}${BOLD}"
echo "╔══════════════════════════════════════════════════════════╗"
echo "║                                                          ║"
echo "║              ✅ INSTALLATION COMPLETE!                   ║"
echo "║                                                          ║"
echo "║   🌙 CPM Eclipse v$version is ready to use!              ║"
echo "║                                                          ║"
echo "║   📋 What to do next:                                   ║"
echo "║                                                          ║"
echo "║   1. Edit config.json:                                   ║"
echo "║      nano config.json                                   ║"
echo "║                                                          ║"
echo "║   2. Run the tool:                                      ║"
echo "║      ./eclipse.sh                                       ║"
echo "║                                                          ║"
echo "║   3. Or run Python directly:                            ║"
echo "║      python main.py                                     ║"
echo "║                                                          ║"
echo "║   📱 Support: @H3X_cpm                                  ║"
echo "║                                                          ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo -e "${NC}"

# ===== ASK TO RUN =====
echo -e "${CYAN}🚀 Do you want to run CPM Eclipse now?${NC}"
echo -e "${YELLOW}[y/N]${NC} "
read -r run_now

if [[ "$run_now" == "y" || "$run_now" == "Y" ]]; then
    echo -e "${GREEN}🚀 Starting CPM Eclipse...${NC}"
    sleep 1
    ./eclipse.sh
else
    echo -e "${GREEN}👋 Installation complete! Run ./eclipse.sh when ready.${NC}"
fi
