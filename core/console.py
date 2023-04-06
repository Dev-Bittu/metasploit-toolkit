from core.banner import banner
from os import system
from utilities.message import info

class Console:
    def __init__(self) -> None:
        self.auther = "Dev-Bittu (Bittu)"
        self.shell_input = "mst > "

    def run(self):
        print("\n")
        while True:
            query = input(self.shell_input).strip().lower()
            
            if query == "exit":
                exit()
            elif query == "help":
                self.help()
            else:
                print(info(f"Command \"{query}\" not found. Executing in system"))
                system(query)

    def banner(self, module_path):
        banner(module_path)
        print()

    def help(self):
        print('This is help')

    def load_module(self, module_name):
        pass

    def is_module_exists(self, module_name):
        pass
