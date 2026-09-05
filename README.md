<div align="center">

# 🌙 CPM Eclipse

### Advanced Car Parking Multiplayer Tool with Telegram Integration

[![Version](https://img.shields.io/badge/version-4.8.2-blue.svg)](https://github.com/H3X-cpm/CPM-Eclipse)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10+-yellow.svg)](https://python.org)
[![Termux](https://img.shields.io/badge/Termux-F5D04E?style=flat&logo=android&logoColor=black)](https://termux.com)
[![GitHub stars](https://img.shields.io/github/stars/HEX-cpm/CPM-Eclipse.svg?style=social)](https://github.com/H3X-cpm/CPM-Eclipse)
[![Telegram](https://img.shields.io/badge/Telegram-@H3X_cpm-blue.svg)](https://t.me/H3X_cpm)

</div>

---

## 👨‍💻 Developers

| Role | Name | Contact |
|------|------|---------|
| **Lead Developer** | H3X | [@H3X_cpm](https://t.me/H3X_cpm) |
| **Co-Developer** | Sami | [@Sami](Sami) |
support me on Ko Fi
[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/U2I826F6MQ)

---

## 📸 Demo

<div align="center">
  
### 🎬 CPM Eclipse Banner

![CPM Eclipse Banner](images/gemini-image-2_Professional_graphic_design_3D_render_make_me_a_car_parking_multiplayer_banner_i-0.jpg)

*Professional banner for CPM Eclipse tool*

</div>

---

## ✨ Features

### 🎮 Current Functions (47+)

#### 💰 Money & Coins
| # | Function | Cost |
|---|----------|------|
| 1 | Set Money | 10 pts |
| 2 | Set Coins | 10 pts |

#### 👤 Account Management
| # | Function | Cost |
|---|----------|------|
| 3 | Set Player Name | 5 pts |
| 4 | Set Player ID | 5 pts |
| 5 | Set King Rank | 20 pts |
| 6 | Clone Account | 70 pts |
| 7 | Change Email | 10 pts |
| 8 | Change Password | 10 pts |

#### 🔓 Unlockables
| # | Function | Cost |
|---|----------|------|
| 9 | Unlock All Cars | 50 pts |
| 10 | Unlock All Lamborghinis | 30 pts |
| 11 | Unlock Paid Cars | 40 pts |
| 12 | Unlock W16 Engine | 25 pts |
| 13 | Unlock All Horns | 20 pts |
| 14 | Unlock Houses | 25 pts |
| 15 | Unlock Smoke | 20 pts |
| 16 | Unlock Wheels | 20 pts |
| 17 | Unlock Animations | 15 pts |
| 18 | Unlock Crown | 15 pts |
| 19 | Unlock CLS | 25 pts |
| 20 | Unlock Siren Cars | 35 pts |

#### 🏁 Racing
| # | Function | Cost |
|---|----------|------|
| 21 | Set Race Wins | 15 pts |
| 22 | Set Race Loses | 15 pts |

#### 🚗 Car Modifications
| # | Function | Cost |
|---|----------|------|
| 23 | Hack Car Speed | 25 pts |
| 24 | Speed All Cars | 50 pts |
| 25 | Modify All Cars | 75 pts |
| 26 | Copy Livery | 20 pts |
| 27 | Remove Bumpers | 15 pts |
| 28 | Stance Camber | 10 pts |

#### 🔧 Custom Car
| # | Function | Cost |
|---|----------|------|
| 29 | Custom HP | 15 pts |
| 30 | Custom Angle | 10 pts |
| 31 | Custom Tire | 10 pts |
| 32 | Custom Mileage | 10 pts |
| 33 | Custom Brake | 10 pts |
| 34 | Rear Bumper | 10 pts |
| 35 | Front Bumper | 10 pts |

#### 👕 Customization
| # | Function | Cost |
|---|----------|------|
| 36 | Male Equipment | 15 pts |
| 37 | Female Equipment | 15 pts |
| 38 | Male Hats | 10 pts |
| 39 | Male Tops | 10 pts |
| 40 | Female Tops | 10 pts |
| 41 | Remove Male Head | 10 pts |
| 42 | Remove Female Head | 10 pts |

#### 👥 Other
| # | Function | Cost |
|---|----------|------|
| 43 | Delete Friends | 5 pts |
| 44 | Set Plates | 10 pts |
| 45 | Delete Account | Free |
| 46 | Register Account | Free |
| 47 | Get Player Stats | Free |

---

## 🚀 Coming Soon (Next Updates)

| Feature | Status | Expected |
|---------|--------|----------|
| **Bulk Clone Accounts** | ⏳ In Development | v4.8.3 |
| **Bulk Money** | ⏳ Planned | v4.8.3 |
| **Bulk Unlock Cars** | ⏳ Planned | v4.8.3 |
| **Premium Unlock** | 📋 Planned | v5.0 |
| **Auto-Backup** | 📋 Planned | v5.0 |
| **Account Compare** | 📋 Planned | v5.0 |

---

## 📋 Requirements

| Requirement | Version |
|-------------|---------|
| **Termux** | F-Droid version |
| **Python** | 3.10 or higher |
| **Internet** | Required for API calls |
| **Telegram** | Account for authentication |
| **Storage** | 50MB free space |

---

## 🚀 Installation

### Method 1: Quick Install (Recommended)

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/CPM-Eclipse.git

# Navigate to folder
cd CPM-Eclipse

# Run install script
chmod +x install.sh
./install.sh

# Edit config with your details
nano config.json

# Run the tool
./eclipse.sh
```

### Method 2: Manual Install

```bash
# Install dependencies
pkg update && pkg upgrade
pkg install python git -y
pip install -r requirements.txt

# Clone and run
git clone https://github.com/YOUR_USERNAME/CPM-Eclipse.git
cd CPM-Eclipse
chmod +x eclipse.sh
./eclipse.sh
```

### Method 3: One-Line Install

```bash
git clone https://github.com/YOUR_USERNAME/CPM-Eclipse.git && cd CPM-Eclipse && chmod +x install.sh && ./install.sh && ./eclipse.sh
```

---

## ⚙️ Configuration

### Step 1: Create Config File

```bash
cp config.example.json config.json
```

### Step 2: Edit Config

```bash
nano config.json
```

### Step 3: Add Your Details

```json
{
    "bot_token": "YOUR_BOT_TOKEN_HERE",
    "admin_id": "YOUR_ADMIN_ID_HERE",
    "admin_username": "@H3X_cpm",
    "admin_secret_key": "YOUR_SECRET_KEY",
    "api_url": "https://cpm-eclipse.onrender.com",
    "version": "4.8.2"
}
```

---

## 📱 Usage

### Launch the Tool

```bash
./eclipse.sh
```

### Main Menu Interface

```
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║    ██████╗ ██████╗ ███╗   ███╗    ███████╗ ██████╗     ║
║   ██╔════╝██╔═══██╗████╗ ████║    ██╔════╝██╔════╝     ║
║   ██║     ██║   ██║██╔████╔██║    █████╗  ██║          ║
║   ██║     ██║   ██║██║╚██╔╝██║    ██╔══╝  ██║          ║
║   ╚██████╗╚██████╔╝██║ ╚═╝ ██║    ███████╗╚██████╗     ║
║    ╚═════╝ ╚═════╝ ╚═╝     ╚═╝    ╚══════╝ ╚═════╝     ║
║                                                          ║
║                 CAR PARKING MULTIPLAYER                  ║
║                    ADVANCED TOOL                         ║
║                                                          ║
║                  Version 4.8.2                           ║
║                  Powered by H3X & Sami                  ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝

╔════════════════════════════════════════════╗
║            CPM ECLIPSE MENU               ║
╠════════════════════════════════════════════╣
║  1. 💰 Set Money (10 pts)                ║
║  2. ⭐ Set Coins (10 pts)                ║
║  3. 👤 Set Name (5 pts)                 ║
║  ...                                     ║
║  47. 📊 Get Player Stats (Free)          ║
║  0. Exit                                  ║
╚════════════════════════════════════════════╝
```

---

## 💰 Point System

### How to Get Points
1. **DM @H3X_cpm** on Telegram
2. Choose your package
3. Send payment (PayPal/Crypto)
4. Points added to your account

### Point Costs

| Action | Cost |
|--------|------|
| Set Money/Coins | 10 pts |
| Set Name/ID | 5 pts |
| Set King Rank | 20 pts |
| Clone Account | 70 pts |
| Unlock All Cars | 50 pts |
| Hack Car Speed | 25 pts |
| Modify All Cars | 75 pts |
| Bulk Clone | 100 pts/clone |
| Delete Account | Free |
| Register Account | Free |

---

## 🔧 Troubleshooting

<details>
<summary><b>❌ "config.json not found"</b></summary>

```bash
cp config.example.json config.json
nano config.json
# Add your configuration
```
</details>

<details>
<summary><b>❌ "Permission denied"</b></summary>

```bash
chmod +x *.sh
```
</details>

<details>
<summary><b>❌ "python: command not found"</b></summary>

```bash
pkg install python
```
</details>

<details>
<summary><b>❌ "Module not found"</b></summary>

```bash
pip install -r requirements.txt
```
</details>

---

---

## 📞 Support

<div align="center">

| Contact | Method |
|---------|--------|
| 💬 **Telegram** | [@H3X_cpm](https://t.me/H3X_cpm) |
| 📢 **Updates Channel** | [@cpmeclipse](https://t.me/cpmeclipseupdates) |
| 💬 **Community** | [@cpmeclipse_chat](https://t.me/cpmeclipse) |
| 🐛 **Issues** | [GitHub Issues](https://github.com/H3X-cpm/CPM-Eclipse/issues) |

</div>

---

---

## ⚠️ Disclaimer

> **🚨 IMPORTANT NOTICE**
> 
> This tool is for **educational and research purposes only**.
> 
> - ✅ Use at your own risk
> - ❌ We are not responsible for account bans
> - ❌ Do not use for illegal activities
> - ✅ Respect the game's terms of service

---

## 📜 License
Don't steal the code as it's not allowed if we catch you, you will be banned.
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Credits

<div align="center">

| Role | Name |
|------|------|
| 👨‍💻 **Lead Developer** | H3X |
| 👨‍💻 **Co-Developer** | Sami |
| 🤝 **Contributors** | Community |
| ⭐ **Special Thanks** | All supporters |

</div>

---

## ⭐ Star Us!

<div align="center">

### If you like this project, give it a ⭐ on GitHub!

[![GitHub stars](https://img.shields.io/github/stars/H3X-cpm/CPM-Eclipse.svg?style=social)](https://github.com/H3X-cpm/CPM-Eclipse)
[![GitHub forks](https://img.shields.io/github/forks/H3X-cpm/CPM-Eclipse.svg?style=social)](https://github.com/H3X-cpm/CPM-Eclipse)

---

**Made with ❤️ by H3X & Sami**

</div>

---

## 🎯 Quick Links

- [GitHub Repository](https://github.com/H3X-cpm/CPM-Eclipse)
- [Issue Tracker](https://github.com/H3X-cpm/CPM-Eclipse/issues)
- [Changelog](CHANGELOG.md)
- [License](LICENSE)

---

<div align="center">

### 🚀 Happy Hacking!

</div>
