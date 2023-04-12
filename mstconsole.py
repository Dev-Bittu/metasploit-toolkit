from core.console import Console
from os.path import join
from utilities.color import red
from settings import BASE_DIR

def main():
    """
    The main function from where console get started.
    """

    console = Console() #Console object
    try:
        console.start_console()
    finally:
        while True:
            try:
                console.console()
            except KeyboardInterrupt:
                print(red("[-] Cannot exit the program, if you want to exit, type \"exit\"."))
            except Exception as e:
                print(red(f"[-] Error occured: {e}"))


if __name__ == "__main__":
    main()
