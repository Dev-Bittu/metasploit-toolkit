from requests import get
from json import loads
from settings import PACKAGE_INFO
from utilities.color import (
    green, 
    yellow, 
    underline,
    red
)
from requests.exceptions import ConnectionError

def update():
    print("Updating...")

def check_update():
    try:
        res = get(
            "https://raw.githubusercontent.com/Dev-Bittu/metasploit-toolkit/master/core/package_info.json"
        )
        latest_version = loads(res.text)["version"]
        current_version = PACKAGE_INFO["version"]
        if latest_version != current_version:
            print(green("[+] Update Available"))
            print(yellow(f"New Version Available... {underline(latest_version)}"))
            print(red(f"Current Version on Your System... {underline(current_version)}"))
            
            update = input("\nYou want to update MetaSploit-Toolkit? [Y/n]: ").lower()

            if update not in ["n", "no"]:
                update()
    except ConnectionError:
        pass
    except Exception as e:
        print(e)
