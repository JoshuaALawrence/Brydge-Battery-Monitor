import os
import re
import time
import subprocess
from threading import Thread

import pystray
from pystray import MenuItem as item
from PIL import Image

tray_icon = None

def exit_application(icon, item):
    icon.stop()

def run_powershell_command(ps_command: str) -> str:
    result = subprocess.run(
        [
            "powershell.exe",
            "-NoLogo",
            "-NoProfile",
            "-WindowStyle", "Hidden",
            "-ExecutionPolicy", "Bypass",
            "-Command", ps_command
        ],
        capture_output=True,
        text=True
    )
    return result.stdout

def get_battery_percentage() -> int:
    ps_command = r"""
    (
        Get-PnpDevice -FriendlyName '*Brydge*' | ForEach-Object {
            $local:test = $_ | 
            Get-PnpDeviceProperty -KeyName '{104EA319-6EE2-4701-BD47-8DDBF425BBE5} 2' | 
                Where Type -ne Empty;
            if ($test) {
                Get-PnpDeviceProperty -InstanceId $($test.InstanceId) -KeyName '{104EA319-6EE2-4701-BD47-8DDBF425BBE5} 2' | % Data
            }
        }
    )
    """
    output = run_powershell_command(ps_command)
    digits = re.findall(r"\d+", output)
    if digits:
        return int(digits[0])
    return -1

def update_tray_icon(icon: pystray.Icon):
    battery_percentage = get_battery_percentage()
    if battery_percentage == -1:
        print("Error: Failed to retrieve battery percentage!")
        icon_path = os.path.join(os.path.dirname(__file__), "Icons", "error.ico")
    else:
        icon_name = f"{battery_percentage}.ico"
        icon_path = os.path.join(os.path.dirname(__file__), "Icons", icon_name)
        
        if not os.path.isfile(icon_path):
            print(f"Error: Icon file {icon_path} not found!")
            icon_path = os.path.join(os.path.dirname(__file__), "Icons", "error.ico")
            
    if os.path.isfile(icon_path):
        img = Image.open(icon_path)
        icon.icon = img

def background_updater(icon: pystray.Icon, interval: int = 60):
    while True:
        update_tray_icon(icon)
        time.sleep(interval)

def start_tray_application():
    global tray_icon
    placeholder_icon_path = os.path.join(os.path.dirname(__file__), "Icons", "error.ico")
    if not os.path.isfile(placeholder_icon_path):
        print("Placeholder icon not found; please place an 'error.ico' in the Icons folder.")
        return

    menu = (item("Exit", exit_application),)

    image = Image.open(placeholder_icon_path)

    tray_icon = pystray.Icon("Brydge Battery Monitor", image, menu=menu)
    tray_icon.title = "Brydge Battery Monitor"
    
    updater_thread = Thread(target=background_updater, args=(tray_icon,), daemon=True)
    updater_thread.start()

    tray_icon.run()

if __name__ == "__main__":
    start_tray_application()
