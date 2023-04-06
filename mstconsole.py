from core.console import Console
from os.path import join
from utilities.color import red
from settings import BASE_DIR

def main():
    console = Console()
    console.banner(
        module_path = join(
            BASE_DIR,"modules"
        )
    )
    while True:
        try:
            console.run()
        except KeyboardInterrupt:
            print(red("[-] Cannot exit the program, if you want to exit, type \"exit\"."))
        except Exception as e:
            print(red(f"[-] Error occured: {e}"))


if __name__ == "__main__":
    main()
