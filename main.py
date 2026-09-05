debug_mode = False
CURRENT_VERSION = """
4.8.2
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
# IMPORT CPM ECLIPSE
# ============================================
from cpmeclipse import CPMEclipse

__CHANNEL_USERNAME__ = "cpmeclipse"
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
        console.print("[%] TRYING TO LOGIN: ", end="")
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

            if service == 0:
                console.print("[bold white] Thank You for using CPM Eclipse[/bold white]")
                sys.exit(0)
                
            elif service == 1:
                console.print(
                    "[bold yellow][bold white][?][/bold white] Insert how much money do you want[/bold yellow]"
                )
                amount = IntPrompt.ask("[?] Amount")
                console.print("[%] Saving your data: ", end="")
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
                            sys.exit(0)
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
                    
            elif service == 2:
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
                            sys.exit(0)
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
                    
            elif service == 3:
                console.print(
                    "[bold red][!] Note:[/bold red]: if the king rank doesn't appear in game, close it and open few times.",
                    end="",
                )
                console.print(
                    "[bold red][!] Note:[/bold red]: please don't do King Rank on same account twice.",
                    end="",
                )
                sleep(2)
                console.print("[%] Giving you a King Rank: ", end="")
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
                        sys.exit(0)
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
                    
            elif service == 4:
                console.print("[bold yellow] '[?] Enter your new ID[/bold yellow]")
                new_id = Prompt.ask("[?] ID")
                console.print("[%] Saving your data: ", end="")
                if len(new_id) >= 8 and (" " in new_id) == False:
                    if cpm.set_player_localid(new_id.upper()):
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
                            sys.exit(0)
                        else:
                            continue
                    else:
                        console.print("[bold red]FAILED[/bold red]")
                        console.print("[bold red]Please Try Again[/bold red]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold yellow] 'Please use valid ID[/bold yellow]")
                    sleep(2)
                    continue
                    
            elif service == 5:
                console.print("[bold yellow] '[?] Enter your new Name[/bold yellow]")
                new_name = Prompt.ask("[?] Name")
                console.print("[%] Saving your data: ", end="")
                if len(new_name) >= 0:
                    if cpm.set_player_name(new_name):
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
                            sys.exit(0)
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
                    
            elif service == 6:
                console.print(
                    "[bold yellow] '[?] Enter your new Rainbow Name[/bold yellow]"
                )
                new_name = Prompt.ask("[?] Name")
                console.print("[%] Saving your data: ", end="")
                if len(new_name) >= 0:
                    if cpm.set_player_name(rainbow_gradient_string(new_name)):
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
                            sys.exit(0)
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
                    
            elif service == 7:
                console.print("[%] Giving you a Number Plates: ", end="")
                if cpm.set_player_plates():
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
                        sys.exit(0)
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
                    
            elif service == 8:
                console.print(
                    "[bold yellow] '[!] After deleting your account there is no going back !![/bold yellow]"
                )
                answ = Prompt.ask(
                    "[?] Do You want to Delete this Account ?!",
                    choices=["y", "n"],
                    default="n",
                )
                if answ == "y":
                    cpm.delete()
                    console.print("[bold yellow] 'SUCCESSFUL[/bold yellow]")
                    console.print(
                        "[bold yellow] '======================================[/bold yellow]"
                    )
                    console.print(
                        f"[bold yellow] Thank You for using our tool, please join our telegram channel: @{__CHANNEL_USERNAME__}[/bold yellow]"
                    )
                    sys.exit(0)
                else:
                    continue
                    
            elif service == 9:
                console.print("[bold yellow] '[!] Registring new Account[/bold yellow]")
                acc2_email = prompt_valid_value(
                    "[?] Account Email", "Email", password=False
                )
                acc2_password = prompt_valid_value(
                    "[?] Account Password", "Password", password=False
                )
                console.print("[%] Creating new Account: ", end="")
                status = cpm.register(acc2_email, acc2_password)
                if status == 0:
                    console.print("[bold yellow] 'SUCCESSFUL[/bold yellow]")
                    console.print(
                        "[bold yellow] '======================================[/bold yellow]"
                    )
                    console.print(
                        "[bold yellow] 'INFO: In order to tweak this account with CPM Eclipse[/bold yellow]"
                    )
                    console.print(
                        "[bold yellow] 'you most sign-in to the game using this account[/bold yellow]"
                    )
                    sleep(2)
                    continue
                elif status == 105:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print(
                        "[bold yellow] 'This email is already exists ![/bold yellow]"
                    )
                    sleep(2)
                    continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
                    
            elif service == 10:
                console.print("[%] Deleting your Friends: ", end="")
                if cpm.delete_player_friends():
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
                        sys.exit(0)
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
                    
            elif service == 11:
                console.print(
                    "[!] Note: this function takes a while to complete, please don't cancel.",
                    end="",
                )
                console.print("[%] Unlocking All Lamborghinis: ", end="")
                if cpm.unlock_all_lamborghinis():
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
                        sys.exit(0)
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
                    
            elif service == 12:
                console.print("[%] Unlocking All Cars: ", end="")
                if cpm.unlock_all_cars():
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
                        sys.exit(0)
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
                    
            elif service == 13:
                console.print("[%] Unlocking All Cars Siren: ", end="")
                if cpm.unlock_all_cars_siren():
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
                        sys.exit(0)
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
                    
            elif service == 14:
                console.print("[%] Unlocking w16 Engine: ", end="")
                if cpm.unlock_w16():
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
                        sys.exit(0)
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
                    
            elif service == 15:
                console.print("[%] Unlocking All Horns: ", end="")
                if cpm.unlock_horns():
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
                        sys.exit(0)
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
                    
            elif service == 16:
                console.print("[%] Unlocking Disable Damage: ", end="")
                if cpm.disable_engine_damage():
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
                        sys.exit(0)
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
                    
            elif service == 17:
                console.print("[%] Unlocking Unlimited Fuel: ", end="")
                if cpm.unlimited_fuel():
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
                        sys.exit(0)
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
                    
            elif service == 18:
                console.print("[%] Unlocking Houses: ", end="")
                if cpm.unlock_houses():
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
                        sys.exit(0)
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
                    
            elif service == 19:
                console.print("[%] Unlocking Smoke: ", end="")
                if cpm.unlock_smoke():
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
                        sys.exit(0)
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
                    
            elif service == 20:
                console.print("[%] Unlocking Wheels: ", end="")
                if cpm.unlock_wheels():
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
                        sys.exit(0)
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
                    
            elif service == 21:
                console.print("[%] Unlocking Animations: ", end="")
                if cpm.unlock_animations():
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
                        sys.exit(0)
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
                    
            elif service == 22:
                console.print("[%] Unlocking Equipaments Male: ", end="")
                if cpm.unlock_equipments_male():
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
                        sys.exit(0)
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
                    
            elif service == 23:
                console.print("[%] Unlocking Equipaments Female: ", end="")
                if cpm.unlock_equipments_female():
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
                        sys.exit(0)
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
                    
            elif service == 24:
                console.print(
                    "[bold yellow] '[!] Insert how much races you win[/bold yellow]"
                )
                amount = IntPrompt.ask("[?] Amount")
                console.print("[%] Changing your data: ", end="")
                if amount > 0:
                    if cpm.set_player_wins(amount):
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
                            sys.exit(0)
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
                        "[bold yellow] '[!] Please use valid values[/bold yellow]"
                    )
                    sleep(2)
                    continue
                    
            elif service == 25:
                console.print(
                    "[bold yellow] '[!] Insert how much races you lose[/bold yellow]"
                )
                amount = IntPrompt.ask("[?] Amount")
                console.print("[%] Changing your data: ", end="")
                if amount > 0:
                    if cpm.set_player_loses(amount):
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
                            sys.exit(0)
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
                        "[bold yellow] '[!] Please use valid values[/bold yellow]"
                    )
                    sleep(2)
                    continue
                    
            elif service == 26:
                console.print(
                    "[bold yellow] '[!] Please Enter Account Details[/bold yellow]"
                )
                to_email = prompt_valid_value(
                    "[?] Account Email", "Email", password=False
                )
                to_password = prompt_valid_value(
                    "[?] Account Password", "Password", password=False
                )
                console.print("[%] Cloning your account: ", end="")
                if cpm.account_clone(to_email, to_password):
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
                        sys.exit(0)
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print(
                        "[bold yellow] '[!] RECEIVER ACCOUNT IS INVALID OR NOT REGISTERED[/bold yellow]"
                    )
                    sleep(2)
                    continue
                    
            elif service == 27:
                console.print(
                    "[bold yellow][!] Note[/bold yellow]: original speed can not be restored!"
                )
                console.print("[bold yellow][!] Enter Car Details.[/bold yellow]")
                car_id = IntPrompt.ask("[bold][?] Car Id[/bold]")
                new_hp = IntPrompt.ask("[bold][?]Enter New HP[/bold]")
                new_inner_hp = IntPrompt.ask("[bold][?]Enter New Inner Hp[/bold]")
                new_nm = IntPrompt.ask("[bold][?]Enter New NM[/bold]")
                new_torque = IntPrompt.ask("[bold][?]Enter New Torque[/bold]")
                console.print(
                    "[bold yellow][%] Hacking Car Speed[/bold yellow]:", end=""
                )
                if cpm.hack_car_speed(car_id, new_hp, new_inner_hp, new_nm, new_torque):
                    console.print("[bold green]SUCCESFUL (✔)[/bold green]")
                    console.print("================================")
                    answ = Prompt.ask(
                        "[?] Do You want to Exit ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Thank You for using CPM Eclipse[/bold white]"
                        )
                        sys.exit(0)
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print(
                        "[bold yellow] '[!] Please use valid values[/bold yellow]"
                    )
                    sleep(2)
                    continue
                    
            elif service == 28:
                console.print("[bold yellow] '[!] ENTER CAR DETAILS[/bold yellow]")
                car_id = IntPrompt.ask("[bold][?] CAR ID[/bold]")
                console.print("[bold yellow] '[!] ENTER STEERING ANGLE[/bold yellow]")
                custom = IntPrompt.ask(
                    "[red][?] ENTER THE AMOUNT OF ANGLE YOU WANT[/red]"
                )
                console.print("[red][%] HACKING CAR ANGLE[/red]: ", end="")
                if cpm.max_max1(car_id, custom):
                    console.print("[bold yellow] 'SUCCESSFUL[/bold yellow]")
                    answ = Prompt.ask(
                        "[red][?] DO YOU WANT TO EXIT[/red] ?",
                        choices=["y", "n"],
                        default="n",
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Thank You for using CPM Eclipse[/bold white]"
                        )
                        sys.exit(0)
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
                    
            elif service == 29:
                console.print("[bold yellow] '[!] ENTER CAR DETAILS[/bold yellow]")
                car_id = IntPrompt.ask("[bold][?] CAR ID[/bold]")
                console.print("[bold yellow] '[!] ENTER PERCENTAGE[/bold yellow]")
                custom = IntPrompt.ask("[pink][?] ENTER PERCENTAGE TIRES U WANT[/pink]")
                console.print("[red][%] Setting Percentage [/red]: ", end="")
                if cpm.max_max2(car_id, custom):
                    console.print("[bold yellow] 'SUCCESSFUL[/bold yellow]")
                    answ = Prompt.ask(
                        "[bold green][?] DO YOU WANT TO EXIT[/bold green] ?",
                        choices=["y", "n"],
                        default="n",
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Thank You for using CPM Eclipse[/bold white]"
                        )
                        sys.exit(0)
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
                    
            elif service == 30:
                console.print("[bold]ENTER CAR DETAILS![/bold]")
                car_id = IntPrompt.ask("[bold][?] CAR ID[/bold]")
                console.print("[bold]ENTER NEW MILLAGE![/bold]")
                custom = IntPrompt.ask("[bold blue][?] ENTER MILLAGE U WANT[/bold blue]")
                console.print("[bold red][%] Setting Percentage [/bold red]: ", end="")
                if cpm.millage_car(car_id, custom):
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    answ = Prompt.ask(
                        "[bold][?] DO YOU WANT TO EXIT[/bold] ?",
                        choices=["y", "n"],
                        default="n",
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Thank You for using CPM Eclipse[/bold white]"
                        )
                        sys.exit(0)
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
                    
            elif service == 31:
                console.print("[bold]ENTER CAR DETAILS![/bold]")
                car_id = IntPrompt.ask("[bold][?] CAR ID[/bold]")
                console.print("[bold]ENTER NEW BRAKE![/bold]")
                custom = IntPrompt.ask("[bold blue][?] ENTER BRAKE U WANT[/bold blue]")
                console.print("[bold red][%] Setting BRAKE [/bold red]: ", end="")
                if cpm.brake_car(car_id, custom):
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    answ = Prompt.ask(
                        "[bold][?] DO YOU WANT TO EXIT[/bold] ?",
                        choices=["y", "n"],
                        default="n",
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Thank You for using CPM Eclipse[/bold white]"
                        )
                        sys.exit(0)
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
                    
            elif service == 32:
                console.print("[bold]ENTER CAR DETAILS![/bold]")
                car_id = IntPrompt.ask("[bold][?] CAR ID[/bold]")
                console.print("[bold red][%] Removing Rear Bumper [/bold red]: ", end="")
                if cpm.rear_bumper(car_id):
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    answ = Prompt.ask(
                        "[bold][?] DO YOU WANT TO EXIT[/bold] ?",
                        choices=["y", "n"],
                        default="n",
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Thank You for using CPM Eclipse[/bold white]"
                        )
                        sys.exit(0)
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
                    
            elif service == 33:
                console.print("[bold]ENTER CAR DETAILS![/bold]")
                car_id = IntPrompt.ask("[bold][?] CAR ID[/bold]")
                console.print("[bold red][%] Removing Front Bumper [/bold red]: ", end="")
                if cpm.front_bumper(car_id):
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    answ = Prompt.ask(
                        "[bold][?] DO YOU WANT TO EXIT[/bold] ?",
                        choices=["y", "n"],
                        default="n",
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Thank You for using CPM Eclipse[/bold white]"
                        )
                        sys.exit(0)
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
                    
            elif service == 34:
                console.print("[bold]Enter New Password![/bold]")
                new_password = prompt_valid_value(
                    "[bold][?] Account New Password[/bold]", "Password", password=False
                )
                console.print("[bold red][%] Changing Password [/bold red]: ", end="")
                if cpm.change_password(new_password):
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    answ = Prompt.ask(
                        "[bold][?] DO YOU WANT TO EXIT[/bold] ?",
                        choices=["y", "n"],
                        default="n",
                    )
                    if answ == "y":
                        console.print(
                            "[bold white]Thank You for using CPM Eclipse[/bold white]"
                        )
                        sys.exit(0)
                    else:
                        continue
                else:
                    console.print("[bold yellow]FAILED[/bold yellow]")
                    console.print("[bold yellow]PLEASE TRY AGAIN[/bold yellow]")
                    sleep(2)
                    continue
                    
            elif service == 35:
                console.print("[bold]Enter New Email![/bold]")
                new_email = prompt_valid_value(
                    "[bold][?] Account New Email[/bold]", "Email"
                )
                console.print("[bold red][%] Changing Email [/bold red]: ", end="")
                if cpm.change_email(new_email):
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    answ = Prompt.ask(
                        "[bold][?] DO YOU WANT TO EXIT[/bold] ?",
                        choices=["y", "n"],
                        default="n",
                    )
                    if answ == "y":
                        console.print(
                            "[bold white]Thank You for using CPM Eclipse[/bold white]"
                        )
                        sys.exit(0)
                    else:
                        break
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]EMAIL IS ALREADY REGISTERED [/bold red]")
                    sleep(4)
                    
            elif service == 36:
                console.print("[bold]ENTER CAR DETAILS![/bold]")
                car_id = IntPrompt.ask("[bold][?] CAR ID[/bold]")
                console.print("[bold]ENTER SPOILER ID![/bold]")
                custom = IntPrompt.ask("[bold blue][?]ENTER NEW SPOILER ID[/bold blue]")
                console.print("[bold red][%] SAVING YOUR DATA [/bold red]: ", end="")
                if cpm.telmunnongodz(car_id, custom):
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    answ = Prompt.ask(
                        "[bold][?] DO YOU WANT TO EXIT[/bold] ?",
                        choices=["y", "n"],
                        default="n",
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Thank You for using CPM Eclipse[/bold white]"
                        )
                        sys.exit(0)
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
                    
            elif service == 37:
                console.print("[bold]ENTER CAR DETAILS![/bold]")
                car_id = IntPrompt.ask("[bold][?] CAR ID[/bold]")
                console.print("[bold]ENTER BODYKIT ID![/bold]")
                custom = IntPrompt.ask("[bold blue][?]INSERT BODYKIT ID[/bold blue]")
                console.print("[bold red][%] SAVING YOUR DATA [/bold red]: ", end="")
                if cpm.telmunnongonz(car_id, custom):
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    answ = Prompt.ask(
                        "[bold][?] DO YOU WANT TO EXIT[/bold] ?",
                        choices=["y", "n"],
                        default="n",
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Thank You for using CPM Eclipse[/bold white]"
                        )
                        sys.exit(0)
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
                    
            elif service == 38:
                console.print("[%] Unlocking Premium Wheels..: ", end="")
                if cpm.shittin():
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
                        sys.exit(0)
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
                    
            elif service == 39:
                console.print(
                    "[!] Note: this function takes a while to complete, please don't cancel.",
                    end="",
                )
                console.print("[%] Unlocking Toyota Crown: ", end="")
                if cpm.unlock_crown():
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
                        sys.exit(0)
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
                    
            elif service == 40:
                console.print("[%] Unlocking Clan Hat: ", end="")
                if cpm.unlock_hat_m():
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
                        sys.exit(0)
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
                    
            elif service == 41:
                console.print("[%] Removing Male head: ", end="")
                if cpm.rmhm():
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
                        sys.exit(0)
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
                    
            elif service == 42:
                console.print("[%] Removing Female Head: ", end="")
                if cpm.rmhfm():
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
                        sys.exit(0)
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
                    
            elif service == 43:
                console.print("[%] Unlocking Clan clothes Top 1: ", end="")
                if cpm.unlock_topm():
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
                        sys.exit(0)
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
                    
            elif service == 44:
                console.print("[%] Unlocking Clan clothes Top 1: ", end="")
                if cpm.unlock_topmz():
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
                        sys.exit(0)
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
                    
            elif service == 45:
                console.print("[%] Unlocking Clan clothes Top 3: ", end="")
                if cpm.unlock_topmx():
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
                        sys.exit(0)
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
                    
            elif service == 46:
                console.print("[%] Unlocking Clan clothes Top: ", end="")
                if cpm.unlock_topf():
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
                        sys.exit(0)
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
                    
            elif service == 47:
                console.print("[%] Unlocking Clan clothes Top 1: ", end="")
                if cpm.unlock_topfz():
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
                        sys.exit(0)
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
                    
            elif service == 48:
                console.print("[%] Unlocking Mercedes Cls: ", end="")
                if cpm.unlock_cls():
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
                        sys.exit(0)
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
                    
            elif service == 49:
                console.print("[bold]ENTER DETAILS TO MODIFY ALL CARS![/bold]")
                new_hp = IntPrompt.ask("[bold][?] New HP entry[/bold]")
                new_inner_hp = IntPrompt.ask("[bold][?] New internal HP input[/bold]")
                new_nm = IntPrompt.ask("[bold][?] New entry NM[/bold]")
                new_torque = IntPrompt.ask("[bold][?] Enter new torque[/bold]")
                console.print("[bold red][%] modificar all cars [/bold red]: ", end="")
                if cpm.modificar_todos_los_autos(new_hp, new_inner_hp, new_nm, new_torque):
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[bold][?]DO YOU WANT TO LEAVE?[/bold] ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print("thanks for using CPM Eclipse")
                        sys.exit(0)
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
                    
            elif service == 50:
                console.print("[%] Unlock Paid Cars: ", end="")
                if cpm.unlock_paid_cars():
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
                        sys.exit(0)
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
                    
            elif service == 51:
                console.print("[bold]ENTER CAR DETAILS![/bold]")
                car_id = IntPrompt.ask("[bold][?] CAR ID[/bold]")
                console.print("[bold]ENTER VALUE FOR STANCE [/bold]")
                custom = IntPrompt.ask("[bold blue][?]INSERT VALUE[/bold blue]")
                console.print("[bold red][%] SAVING YOUR DATA [/bold red]: ", end="")
                if cpm.incline(car_id, custom):
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    answ = Prompt.ask(
                        "[bold][?] DO YOU WANT TO EXIT[/bold] ?",
                        choices=["y", "n"],
                        default="n",
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Thank You for using CPM Eclipse[/bold white]"
                        )
                        sys.exit(0)
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
                    
            elif service == 52:
                console.print("[bold]ENTER CAR DETAILS![/bold]")
                source_car_id = IntPrompt.ask("[bold][?] SOURCE CAR ID[/bold]")
                target_car_id = IntPrompt.ask("[bold][?] TARGET CAR ID[/bold]")
                console.print("[%] COPYING LIVERY, PLEASE WAIT: ", end="")
                if cpm.copy_livery(source_car_id, target_car_id):
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
                        sys.exit(0)
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
                    
            break
        break
