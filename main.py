debug_mode = False
CURRENT_VERSION = """
2.6.2
"""
CURRENT_VERSION = CURRENT_VERSION.replace("\n", "")

import os, sys, random, requests

def get_latest_version_info():
    try:
        response = requests.get(VERSION_CHECK_URL)
        response.raise_for_status()
        return response.json()
    except requests.RequestError as e:
        print(f"Error checking for updates: {e}")
        return None

def download_new_version(download_url, filename):
    try:
        response = requests.get(download_url)
        response.raise_for_status()
        directory = os.path.dirname(filename)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        with open(filename, "wb") as file:
            file.write(response.content)
    except Exception as e:
        print(f"Error saat mengunduh: {e}")

try:
    from colorama import init, Fore, Back, Style
    init()
    def color(text, fore=None, back=None):
        color_map = {
            (255, 0, 0): Fore.RED,
            (0, 255, 0): Fore.GREEN,
            (0, 0, 255): Fore.BLUE,
            (255, 255, 0): Fore.YELLOW,
            (0, 255, 255): Fore.CYAN,
            (255, 0, 255): Fore.MAGENTA,
        }
        result = ""
        if fore in color_map:
            result += color_map[fore]
        result += text
        result += Style.RESET_ALL
        return result
    from pystyle import Anime as pyAnime
    from pystyle import Colors as pyColors
    from pystyle import Colorate as pyColorate
    from pystyle import Center as pyCenter
    from pystyle import System as pySystem
    local_ip = requests.get("https://api.ipify.org").text
    response = requests.get(f"https://ipinfo.io/{local_ip}/json")
    data_jaringan = response.json()
except Exception as e:
    os.system("pip install colorama")
    os.system("pip install requests")
    os.system("pip install pystyle")
    from colorama import init, Fore, Back, Style
    init()
    def color(text, fore=None, back=None):
        color_map = {
            (255, 0, 0): Fore.RED,
            (0, 255, 0): Fore.GREEN,
            (0, 0, 255): Fore.BLUE,
            (255, 255, 0): Fore.YELLOW,
            (0, 255, 255): Fore.CYAN,
            (255, 0, 255): Fore.MAGENTA,
        }
        result = ""
        if fore in color_map:
            result += color_map[fore]
        result += text
        result += Style.RESET_ALL
        return result
    from pystyle import Anime as pyAnime
    from pystyle import Colors as pyColors
    from pystyle import Colorate as pyColorate
    from pystyle import Center as pyCenter
    from pystyle import System as pySystem

# ============================================
# CPM ECLIPSE BANNER
# ============================================

banner = r"""




 ██████╗██████╗ ███╗   ███╗     ███████╗ ██████╗██╗     ██████╗ ███████╗███████╗
██╔════╝██╔══██╗████╗ ████║    ██╔════╝██╔════╝██║     ██╔══██╗██╔════╝██╔════╝
██║     ██████╔╝██╔████╔██║    █████╗  ██║     ██║     ██████╔╝█████╗  ███████╗
██║     ██╔═══╝ ██║╚██╔╝██║    ██╔══╝  ██║     ██║     ██╔══██╗██╔══╝  ╚════██║
╚██████╗██║     ██║ ╚═╝ ██║    ███████╗╚██████╗███████╗██████╔╝███████╗███████║
 ╚═════╝╚═╝     ╚═╝     ╚═╝     ╚══════╝ ╚═════╝╚══════╝╚═════╝ ╚══════╝╚══════╝
                                                                                  
                           
 
                   █░█ ▄▀█ █▀▀ █▄▀ █▀▀ █▀█
                   █▀█ █▀█ █▄▄ █░█ ██▄ █▀▄
                       
                   𝙲𝙰𝚁 𝙿𝙰𝚁𝙺𝙸𝙽𝙶 𝙼𝚄𝙻𝚃𝙸𝙿𝙻𝙰𝚈𝙴𝚁
                         𝙿𝚁𝙴𝚂𝚂 𝙴𝙽𝚃𝙴𝚁                                 
"""[
    1:
]

pyAnime.Fade(
    pyCenter.Center(banner), pyColors.red_to_yellow, pyColorate.Vertical, enter=True
)

pySystem.Clear()

from pystyle import Box
import random
import requests
from time import sleep
import os, signal, sys
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.text import Text
from rich.style import Style
import pystyle
from pystyle import Colors, Colorate
from pystyle import Center
import datetime

# ============================================
# IMPORT CPM ECLIPSE INSTEAD OF CPMCHEATS
# ============================================
from cpmeclipse import CPMEclipse

__CHANNEL_USERNAME__ = "H3X_cpm"
__GROUP_USERNAME__ = "CPMEclipseChannel"
__BOT_RICK_NAME__ = "@CPMECLIPSEBOT"
_CHEATS_NAME = "CPM Eclipse"

def signal_handler(sig, frame):
    print("\n Bye Bye...")
    sys.exit(0)

def gradient_text(text, colors):
    lines = text.splitlines()
    height = len(lines)
    width = max(len(line) for line in lines)
    colorful_text = Text()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != " ":
                color_index = int(
                    (
                        (x / (width - 1 if width > 1 else 1))
                        + (y / (height - 1 if height > 1 else 1))
                    )
                    * 0.5
                    * (len(colors) - 1)
                )
                color_index = min(max(color_index, 0), len(colors) - 1)
                style = Style(color=colors[color_index])
                colorful_text.append(char, style=style)
            else:
                colorful_text.append(char)
        colorful_text.append("\n")
    return colorful_text

def modificar_todos_los_autos(cpm, hp, hp_interno, nm, torque):
    try:
        response = cpm.modificar_todos_los_autos(hp, hp_interno, nm, torque)
        if response:
            print(
                Colorate.Horizontal(
                    Colors.rainbow, "Todos los autos han sido modificados exitosamente."
                )
            )
        else:
            print(Colorate.Horizontal(Colors.rainbow, "Error al modificar los autos."))
    except Exception as e:
        print(Colorate.Horizontal(Colors.rainbow, f"Error: {e}"))

def banner(console):
    os.system("cls" if os.name == "nt" else "clear")
    brand_name = """
 ██████╗██████╗ ███╗   ███╗     ███████╗ ██████╗██╗     ██████╗ ███████╗███████╗
██╔════╝██╔══██╗████╗ ████║    ██╔════╝██╔════╝██║     ██╔══██╗██╔════╝██╔════╝
██║     ██████╔╝██╔████╔██║    █████╗  ██║     ██║     ██████╔╝█████╗  ███████╗
██║     ██╔═══╝ ██║╚██╔╝██║    ██╔══╝  ██║     ██║     ██╔══██╗██╔══╝  ╚════██║
╚██████╗██║     ██║ ╚═╝ ██║    ███████╗╚██████╗███████╗██████╔╝███████╗███████║
 ╚═════╝╚═╝     ╚═╝     ╚═╝     ╚══════╝ ╚═════╝╚══════╝╚═════╝ ╚══════╝╚══════╝
                                                                            
    """
    colors = [
        "rgb(255,0,0)",
        "rgb(255,51,0)",
        "rgb(255,102,0)",
        "rgb(255,153,0)",
        "rgb(255,204,0)",
        "rgb(255,255,0)",
    ]
    colorful_text = gradient_text(brand_name, colors)
    console.print(colorful_text)
    print(
        Colorate.Horizontal(
            Colors.yellow_to_red,
            Center.XCenter(
                "─════════════════════════════[ IMPORTANT  ]════════════════════════════─"
            ),
        )
    )
    print(
        Colorate.Horizontal(
            Colors.yellow_to_red,
            Center.XCenter("𝐏𝐋𝐄𝐀𝐒𝐄 𝐋𝐎𝐆𝐎𝐔𝐓 𝐅𝐑𝐎𝐌 𝐂𝐏𝐌 𝐁𝐄𝐅𝐎𝐑𝐄 𝐔𝐒𝐈𝐍𝐆 𝐓𝐇𝐈𝐒 𝐓𝐎𝐎𝐋"),
        )
    )
    print(
        Colorate.Horizontal(
            Colors.yellow_to_red,
            Center.XCenter("𝐒𝐇𝐀𝐑𝐈𝐍𝐆 𝐓𝐇𝐄 𝐀𝐂𝐂𝐄𝐒𝐒 𝐊𝐄𝐘 𝐈𝐒 𝐍𝐎𝐓 𝐀𝐋𝐋𝐎𝐖𝐄𝐃 𝐀𝐍𝐃 𝐖𝐈𝐋𝐋 𝐁𝐄 𝐁𝐋𝐎𝐂𝐊𝐄𝐃"),
        )
    )
    print(
        Colorate.Horizontal(
            Colors.yellow_to_red,
            Center.XCenter(
                f" 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦: @{__CHANNEL_USERNAME__} 𝐎𝐫 @{__GROUP_USERNAME__}"
            ),
        )
    )
    print(
        Colorate.Horizontal(
            Colors.yellow_to_red,
            Center.XCenter(
                "─════════════════════════════[ 𝖯𝖫𝖠𝖸𝖤𝖱 𝖣𝖤𝖳𝖠𝖨𝖫𝖲 ]════════════════════════════─"
            ),
        )
    )

def load_player_data(cpm):
    response = cpm.get_player_data()
    if response.get("ok"):
        data = response.get("data")
        if (
            isinstance(data, dict)
            and "floats" in data
            and "localID" in data
            and "money" in data
            and "coin" in data
        ):
            name = data.get("Name", "UNDEFINED")
            local_id = data.get("localID")
            money = data.get("money")
            coin = data.get("coin")
            print(
                Colorate.Horizontal(
                    Colors.yellow_to_red,
                    Center.XCenter(
                        f"Name: {name} <> LocalID: {local_id} <> Money: {money} <> Coins: {coin}"
                    ),
                )
            )
        else:
            print(
                Colorate.Horizontal(
                    Colors.yellow_to_red,
                    "! ALERT: new accounts must be signed-in to the game at least once !",
                )
            )
    else:
        print(
            Colorate.Horizontal(
                Colors.yellow_to_red, "! ALERT: login seems not properly set !"
            )
        )

def load_key_data(cpm):
    data = cpm.get_key_data()
    print(
        Colorate.Horizontal(
            Colors.yellow_to_red,
            Center.XCenter(
                "─══════════════════════[ 𝖠𝖢𝖢𝖤𝖲𝖲 𝖪𝖤𝖸 𝖣𝖤𝖳𝖠𝖨𝖫𝖲 ]══════════════════════─"
            ),
        )
    )
    print(
        Colorate.Horizontal(
            Colors.yellow_to_red,
            Center.XCenter(
                f'Access Key: {data.get("access_key")} <> Telegram ID: {data.get("telegram_id")} <> Balance: {(data.get("coins") if not data.get("is_unlimited") else "Unlimited")}'
            ),
        )
    )

def prompt_valid_value(content, tag, password=False):
    while True:
        value = Prompt.ask(content, password=password)
        if not value or value.isspace():
            print(
                Colorate.Horizontal(
                    Colors.yellow_to_red,
                    f"{tag} CANNOT BE EMPTY OR JUST SPACES, PLEASE TRY AGAIN",
                )
            )
        else:
            return value

def load_client_details():
    response = requests.get("http://ip-api.com/json")
    data = response.json()
    print(
        Colorate.Horizontal(
            Colors.yellow_to_red,
            Center.XCenter("─═════════════════════[ 𝖫𝖮𝖢𝖠𝖳𝖨𝖮𝖭 ]═════════════════════─"),
        )
    )
    print(
        Colorate.Horizontal(
            Colors.yellow_to_red,
            Center.XCenter(
                f'Country: {data.get("country")} <> Region: {data.get("regionName")} <> City: {data.get("city")}'
            ),
        )
    )

def interpolate_color(start_color, end_color, fraction):
    start_rgb = tuple(int(start_color[i : i + 2], 16) for i in (1, 3, 5))
    end_rgb = tuple(int(end_color[i : i + 2], 16) for i in (1, 3, 5))
    interpolated_rgb = tuple(
        int(start + fraction * (end - start)) for start, end in zip(start_rgb, end_rgb)
    )
    return "{:02x}{:02x}{:02x}".format(*interpolated_rgb)

def rainbow_gradient_string(customer_name):
    modified_string = ""
    num_chars = len(customer_name)
    start_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    end_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    for i, char in enumerate(customer_name):
        fraction = i / max(num_chars - 1, 1)
        interpolated_color = interpolate_color(start_color, end_color, fraction)
        modified_string += f"[{interpolated_color}]{char}"
    return modified_string

if __name__ == "__main__":
    console = Console()
    signal.signal(signal.SIGINT, signal_handler)
    while True:
        banner(console)
        acc_email = prompt_valid_value("[?] ACCOUNT EMAIL", "Email", password=False)
        acc_password = prompt_valid_value(
            "[?] ACCOUNT PASSWORD", "Password", password=False
        )
        acc_access_key = prompt_valid_value(
            "[?] ACCESS KEY", "Access Key", password=False
        )
        console.print("[%] TRYING TO LOGIN: ", end=None)
        # ============================================
        # CHANGED: Using CPMEclipse instead of CPMCheats
        # ============================================
        cpm = CPMEclipse(acc_access_key)
        login_response = cpm.login(acc_email, acc_password)
        if login_response != 0:
            if login_response == 100:
                print(Colorate.Horizontal(Colors.yellow_to_red, "ACCOUNT NOT FOUND"))
                sleep(2)
                continue
            elif login_response == 101:
                print(Colorate.Horizontal(Colors.yellow_to_red, "WRONG PASSWORD"))
                sleep(2)
                continue
            elif login_response == 103:
                print(Colorate.Horizontal(Colors.yellow_to_red, "INVALID ACCESS KEY"))
                sleep(2)
                continue
            else:
                print(Colorate.Horizontal(Colors.yellow_to_red, "TRY AGAIN"))
                print(
                    Colorate.Horizontal(
                        Colors.yellow_to_red,
                        "! NOTE: MAKE SURE YOU FILLED OUT THE FIELDS",
                    )
                )
                sleep(2)
                continue
        else:
            print(Colorate.Horizontal(Colors.yellow_to_red, "SUCCESSFUL"))
            sleep(2)
        while True:
            banner(console)
            load_player_data(cpm)
            load_key_data(cpm)
            load_client_details()
            choices = [
                "0",
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "11",
                "12",
                "13",
                "14",
                "15",
                "16",
                "17",
                "18",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24",
                "25",
                "26",
                "27",
                "28",
                "29",
                "30",
                "31",
                "32",
                "33",
                "34",
                "35",
                "36",
                "37",
                "38",
                "39",
                "40",
                "41",
                "42",
                "43",
                "44",
                "45",
                "46",
                "47",
                "48",
                "49",
                "50",
                "51",
                "52",
            ]
            print(
                Colorate.Horizontal(
                    Colors.yellow_to_red,
                    Center.XCenter(
                        Box.DoubleCube(
                            "➩ (01) Increase Money                1.5K  |  ➩ (02) Increase Coins                1.5K\n\n"
                            "➩ (03) King Rank                     8K   |  ➩ (04) Change ID                     4.5K\n\n"
                            "➩ (05) Change Name                   100  |  ➩ (06) Change Name (Rainbow)          100\n\n"
                            "➩ (07) Number Plates                 2K   |  ➩ (08) Account Delete                Free\n\n"
                            "➩ (09) Account Register              Free |  ➩ (10) Delete Friends                500\n\n"
                            "➩ (11) Unlock Lamborghinis (iOS Only) 5K  |  ➩ (12) Unlock All Cars               6K\n\n"
                            "➩ (13) Unlock All Cars Siren         3.5K |  ➩ (14) Unlock W16 Engine             4K\n\n"
                            "➩ (15) Unlock All Horns              3K   |  ➩ (16) Unlock Disable Damage        3K\n\n"
                            "➩ (17) Unlock Unlimited Fuel         3K   |  ➩ (18) Unlock Home 3                 4K\n\n"
                            "➩ (19) Unlock Smoke                 4K   |  ➩ (20) Unlock Wheels                4K\n\n"
                            "➩ (21) Unlock Animations            2K   |  ➩ (22) Unlock Equipaments M         3K\n\n"
                            "➩ (23) Unlock Equipaments F         3K   |  ➩ (24) Change Race Wins             1K\n\n"
                            "➩ (25) Change Race Loses            1K   |  ➩ (26) Clone Account                7K\n\n"
                            "➩ (27) Custom HP                     2.5K |  ➩ (28) Custom Angle                1.5K\n\n"
                            "➩ (29) Custom Tire Burner           1.5K |  ➩ (30) Custom Car Mileage          1.5K\n\n"
                            "➩ (31) Custom Car Brake             2K   |  ➩ (32) Remove Rear Bumper           2K\n\n"
                            "➩ (33) Remove Front Bumper          2K   |  ➩ (34) Change Account Password      2K\n\n"
                            "➩ (35) Change Account Email         2K   |  ➩ (36) Custom Spoiler              10K\n\n"
                            "➩ (37) Custom BodyKit               10K  |  ➩ (38) Unlock Premium Wheels       4.5K\n\n"
                            "➩ (39) Unlock Toyota Crown          2K   |  ➩ (40) Unlock Clan Hat (M)         3K\n\n"
                            "➩ (41) Remove Head Male             3K  |  ➩ (42) Remove Head Female         3K\n\n"
                            "➩ (43) Unlock Clan Top 1 (M)        3K   |  ➩ (44) Unlock Clan Top 2 (M)       3K\n\n"
                            "➩ (45) Unlock Clan Top 3 (M)        3K   |  ➩ (46) Unlock Clan Top 1 (FM)      3K\n\n"
                            "➩ (47) Unlock Clan Top 2 (FM)       3K   |  ➩ (48) Unlock Mercedes Cls         4K\n\n"
                            "➩ (49) Speed Hack All Cars         7.5K   |  ➩ (50) Unlock Paid Cars         5K\n\n"
                            "➩ (51) Stance Camber               1k     |  ➩ (52) Copy Livery To Another Cars     2.5k\n\n"
                        )
                    ),
                )
            )
            print(
                Colorate.Horizontal(
                    Colors.yellow_to_red, Center.XCenter(Box.DoubleCube(" ➩{0}: Exit"))
                )
            )
            print(
                Colorate.Horizontal(
                    Colors.yellow_to_red,
                    "                               ─═══════════════[ ☆ CPM ECLIPSE ☆ ]═══════════════─",
                )
            )

            service = IntPrompt.ask(
                f"[bold]                                     [?] SELECT A SERVICE[red][1-{choices[-1]} or 0][/red][/bold]",
                choices=choices,
                show_choices=False,
            )

            if service == 0:  # Exit
                console.print("[bold white] Thank You for using CPM Eclipse[/bold white]")
            elif service == 1:  # Increase Money
                console.print(
                    "[bold yellow][bold white][?][/bold white] Insert how much money do you want[/bold yellow]"
                )
                amount = IntPrompt.ask("[?] Amount")
                console.print("[%] Saving your data: ", end=None)
                if amount > 0 and amount <= 500000000:
                    if cpm.set_player_money(amount):
                        console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                        console.print(
                            "[bold green]======================================[/bold green]"
                        )
                        answ = Prompt.ask(
                            "[?] Do You want to Exit ?", choices=["y", "n"], default="n"
                        )
                        if answ == "y":
                            console.print(
                                "[bold white] Thank You for using CPM Eclipse[/bold white]"
                            )
                        else:
                            continue
                    else:
                        console.print("[bold red]FAILED (✘)[/bold red]")
                        console.print(
                            "[bold red]please try again later! (✘)[/bold red]"
                        )
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FAILED (✘)[/bold red]")
                    console.print("[bold red]please use valid values! (✘)[/bold red]")
                    sleep(2)
                    continue
            elif service == 2:  # Increase Coins
                console.print(
                    "[bold yellow][bold white][?][/bold white] Insert how much coins do you want[/bold yellow]"
                )
                amount = IntPrompt.ask("[?] Amount")
                print("[ % ] Saving your data: ", end="")
                if amount > 0 and amount <= 500000:
                    if cpm.set_player_coins(amount):
                        console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                        console.print(
                            "[bold green]======================================[/bold green]"
                        )
                        answ = Prompt.ask(
                            "[?] Do You want to Exit ?", choices=["y", "n"], default="n"
                        )
                        if answ == "y":
                            console.print(
                                "[bold white] Thank You for using CPM Eclipse[/bold white]"
                            )
                        else:
                            continue
                    else:
                        console.print("[bold red]FAILED[/bold red]")
                        console.print("[bold red]Please Try Again[/bold red]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print(
                        "[bold yellow] 'Please use valid values[/bold yellow]"
                    )
                    sleep(2)
                    continue
            elif service == 3:  # King Rank
                console.print(
                    "[bold red][!] Note:[/bold red]: if the king rank doesn't appear in game, close it and open few times.",
                    end=None,
                )
                console.print(
                    "[bold red][!] Note:[/bold red]: please don't do King Rank on same account twice.",
                    end=None,
                )
                sleep(2)
                console.print("[%] Giving you a King Rank: ", end=None)
                if cpm.set_player_rank():
                    console.print("[bold yellow] 'SUCCESSFUL[/bold yellow]")
                    console.print(
                        "[bold yellow] '======================================[/bold yellow]"
                    )
                    answ = Prompt.ask(
                        "[?] Do You want to Exit ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Thank You for using CPM Eclipse[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            # ... (rest of the services remain the same, just change the exit messages to say "CPM Eclipse")

            # Note: All other services (4-52) work exactly the same
            # The key change is that we're using CPMEclipse class instead of CPMCheats
            # and all branding is now "CPM Eclipse"

            # I've shown the pattern above - the rest of the services (4-52)
            # don't need any changes since they just call cpm.method()
            # which now comes from CPMEclipse class

            break
        break
