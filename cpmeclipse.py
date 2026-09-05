import platform
import os
import requests
import subprocess
import urllib.parse
import json
from concurrent.futures import ThreadPoolExecutor
import ssl
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ============================================
# CPM ECLIPSE - Advanced Car Parking Tool
# Version: 4.8.2
# Powered by H3X
# ============================================

__ENDPOINT_URL__: str = "https://cpmcheats.hostzera.com.br/api2"


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
                print(f"✅ CPM Eclipse: Login successful!")
            return response_decoded.get("error")
        except Exception as e:
            print(f"❌ Login error: {e}")
            return 500

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

    def account_clone(self, account_email, account_password) -> bool:
        """Clone account"""
        payload = {
            "account_auth": self.auth_token,
            "account_email": account_email,
            "account_password": account_password,
        }
        params = {"key": self.access_key}
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

    def modificar_todos_los_autos(self, new_hp, new_inner_hp, new_nm, new_torque) -> bool:
        """Modify ALL cars with speed hack"""
        try:
            with open("car_ids.json", "r") as file:
                car_ids = json.load(file)
        except:
            car_ids = []
            print("⚠️ car_ids.json not found, using default cars")
        
        if not car_ids:
            print("❌ No car IDs found!")
            return False

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
        return True

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
