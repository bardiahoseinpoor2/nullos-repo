import os
import json
import platform
import shutil


BIG_LOGO = [
"                  __   __    ___     ______   ",
"                 [  | [  | .'   `. .' ____ \\  ",
" _ .--.  __   _   | |  | |/  .-.  \\| (___ \\_| ",
"[ `.-. |[  | | |  | |  | || |   | | _.____`.  ",
" | | | | | \\_/ |, | |  | |\\  `-'  /| \\____) | ",
"[___||__]'.__.'_/[___][___]`.___.'  \\______.' ",
]


SMALL_LOGO = [
"  _   _ _   _ _     _     ",
" | \\ | | | | | |   | |    ",
" |  \\| | | | | |   | |    ",
" | |\\  | |_| | |___| |___ ",
" |_| \\_|\\___/|_____|_____|",
"          NULL"
]


TINY_LOGO = [
"NULL"
]


def load_json(path):
    try:
        with open(path) as f:
            return json.load(f)
    except:
        return {}


def get_logo():
    width = shutil.get_terminal_size().columns

    if width >= 90:
        return BIG_LOGO
    elif width >= 50:
        return SMALL_LOGO
    else:
        return TINY_LOGO


def get_ram():
    try:
        with open("/proc/meminfo") as f:
            data = f.read()

        total = int(data.split("MemTotal:")[1].split()[0]) // 1024
        available = int(data.split("MemAvailable:")[1].split()[0]) // 1024
        used = total - available

        return f"{used}MB / {total}MB"

    except:
        return "Unknown"


settings = load_json("settings.json")

LOGO = get_logo()


info = [
    f"NullOS {VERSION_MAIN}",
    "----------------",
    "Kernel: NullKernel",
    "Shell: NullShell",
    f"NullOS Version: {VERSION_MAIN}"
    f"RAM: {get_ram()}",
    f"Path: {os.getcwd()}"
]


print()

width = shutil.get_terminal_size().columns

for i in range(max(len(LOGO), len(info))):
    left = LOGO[i] if i < len(LOGO) else ""
    right = info[i] if i < len(info) else ""

    if width < 50:
        print(left)
        if right:
            print(right)
    else:
        print(f"{left:<55}{right}")

print()
