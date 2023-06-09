from pyfiglet import Figlet
from random import choice
from time import sleep
from utilities.message import success
from threading import Thread, current_thread
from os import walk
from os.path import join
from utilities.color import blue, yellow
from settings import PACKAGE_INFO
from glob import glob

def starting_console() -> None:
    """
    Show prompt "starting mestasploit-toolkit"
    """
    for _ in range(5):
        print(success("Starting metasploit-toolkit console... /"), end="\r")
        sleep(.2)
        print(success("sTarting metasploit-toolkit console... -"), end="\r")
        sleep(.2)
        print(success("stArting metasploit-toolkit console... \\"), end="\r")
        sleep(.2)
        print(success("staRting metasploit-toolkit console... -"), end="\r")
        sleep(.2)
        print(success("starTing metasploit-toolkit console... /"), end="\r")
        sleep(.2)
        print(success("startIng metasploit-toolkit console... -"), end="\r")
        sleep(.2)
        print(success("startiNg metasploit-toolkit console... \\"), end="\r")
        sleep(.2)
        print(success("startinG metasploit-toolkit console... -"), end="\r")
        sleep(.2)
        print(success("starting Metasploit-toolkit console... /"), end="\r")
        sleep(.2)
        print(success("starting mEtasploit-toolkit console... -"), end="\r")
        sleep(.2)
        print(success("starting meTasploit-toolkit console... \\"), end="\r")
        sleep(.2)
        print(success("starting metAsploit-toolkit console... -"), end="\r")
        sleep(.2)
        print(success("starting metaSploit-toolkit console... /"), end="\r")
        sleep(.2)
        print(success("starting metasPloit-toolkit console... -"), end="\r")
        sleep(.2)
        print(success("starting metaspLoit-toolkit console... \\"), end="\r")
        sleep(.2)
        print(success("starting metasplOit-toolkit console... -"), end="\r")
        sleep(.2)
        print(success("starting metasploIt-toolkit console... /"), end="\r")
        sleep(.2)
        print(success("starting metasploiT-toolkit console... -"), end="\r")
        sleep(.2)
        print(success("starting metasploit-Toolkit console... \\"), end="\r")
        sleep(.2)
        print(success("starting metasploit-tOolkit console... -"), end="\r")
        sleep(.2)
        print(success("starting metasploit-toOlkit console... /"), end="\r")
        sleep(.2)
        print(success("starting metasploit-tooLkit console... -"), end="\r")
        sleep(.2)
        print(success("starting metasploit-toolKit console... \\"), end="\r")
        sleep(.2)
        print(success("starting metasploit-toolkIt console... -"), end="\r")
        sleep(.2)
        print(success("starting metasploit-toolkiT console... /"), end="\r")
        sleep(.2)
        print(success("starting metasploit-toolkit Console... -"), end="\r")
        sleep(.2)
        print(success("starting metasploit-toolkit cOnsole... \\"), end="\r")
        sleep(.2)
        print(success("starting metasploit-toolkit coNsole... -"), end="\r")
        sleep(.2)
        print(success("starting metasploit-toolkit conSole... /"), end="\r")
        sleep(.2)
        print(success("starting metasploit-toolkit consOle... -"), end="\r")
        sleep(.2)
        print(success("starting metasploit-toolkit consoLe... \\"), end="\r")
        sleep(.2)
        print(success("starting metasploit-toolkit consolE... -"), end="\r")
        sleep(.2)
    print(success("Started Metasploit-Toolkit Console."))

def count_module(module_path) -> dict:
    """
    Count total numbers of modules,
    return a dict type object.
    """
    dirs = glob(f"{module_path}/*/", recursive = True)
    modules = []
    info = {}
    for dir in dirs:
        if "__pycache__" not in dir:
            modules.append(
                (dir.replace(module_path, "").replace("/",""))
            )
    for module in modules:
        info[module] = sum(1 for _, _, files in walk(join(module_path, module)) if "__pycache__" not in files for f in files)
    current_thread().return_value = {
        "total": sum(info.values())
    } | info


def mst_banner() -> Figlet:
    """
    Show any random banner with text shown MetaSploit-Toolkit
    """
    banner_fonts = [
        'doh',
        'broadway',
        'starwars',
        'xttyb',
        'times',
        'clb8x10',
        'nancyj-underlined',
        'smslant',
        'roman',
        'rozzo',
        'tubular',
        'charact3',
        'graffiti',
        'cybermedium',
        'univers',
        'slant',
        'ogre',
        'poison',
        'banner3-D',
        'epic',
        'nancyj-fancy'
    ]
    figlet = Figlet(font=choice(banner_fonts))
    return figlet.renderText(PACKAGE_INFO['name'])

def banner(module_path):
    """
    Show banner,
    Count module
    """
    t1 = Thread(
        target=starting_console,
        args=()
    )
    t2 = Thread(
        target=count_module, 
        args=(
            module_path,
        )
    )
    t1.start()
    t2.start()
    
    t2.join()
    t1.join()
    
    modules = t2.return_value

    print(mst_banner())
    print(success(f"Total Modules: {modules['total']}"))
    for module, no_of_module in modules.items():
        if module not in ["__pycache__", "total"]:
            print(blue(module.title()), yellow(no_of_module), sep=": ", end="\t")
    print()
