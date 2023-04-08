from core.banner import banner
from os import system
from utilities.message import (
    info, 
    danger,
    warn,
)
from threading import Thread
from settings import BASE_DIR
from os.path import (
    join, 
    exists
)
from core.update import check_update
from utilities.color import (
    underline,
    green
)
from utilities.screen_cleaner import clear
from importlib import import_module
from prettytable import PrettyTable


class Console:
    def __init__(self) -> None:
        self.auther = "Dev-Bittu (Bittu)"
        self.shell_input = f"{underline('mst')} > "
        self.current_module = None

    def console(self):
        print("\n")
        while True:
            query = input(self.shell_input).strip().lower()
            
            if query == "exit":
                exit()
            elif query in ("help", "?"):
                self.help()
            elif query == "clear":
                clear()
            elif "use " in query:
                self.load_module(query.replace("use ", "").strip())
            elif query in ("options", "show options"):
                self.show_options()
            elif "set " in query:
                s = query.replace("set ","").strip().split(" ")
                self.set_option(option=s[0], value=s[1])
            else:
                print(info(f"Command \"{query}\" not found. Executing in system"))
                system(query)

    def start_console(self):
        banner_thread = Thread(target=banner,args=(join(BASE_DIR, "modules"),))
        update_thread = Thread(target=check_update,args=())
        
        banner_thread.start()
        update_thread.start()

        update_thread.join()
        banner_thread.join()

    def help(self):
        print('This is help')

    def load_module(self, module_name):
        if self.is_module_exists(module_name):
            m = import_module(
                join("modules", module_name).replace("/","."), 
                "."
            )
            if module_name.split("/")[0] == "exploit":
                self.current_module = m.Exploit()
                self.current_module.onload(self)
        else:
            print(
                danger(f"Module {module_name} doesnt exists.")
            )

    def is_module_exists(self, module_name) -> bool:
        return exists(join(BASE_DIR, "modules", module_name+".py"))
    
    def set_option(self, option, value):
        if self.current_module is None:
            print(
                warn("Currently any module is not using.")
            )
        else:
            if option in self.current_module.options["required"].keys():
                self.current_module.options["required"][option]["value"] = value
            elif option in self.current_module.options["optional"].keys():
                self.current_module.options["optional"][option]["value"] = value
            else:
                print(
                    warn(f"There is not any option available for {option}")
                )

    def show_options(self):
        if self.current_module is None:
            print(
                warn("Currently any module is not using.")
            )
        else:
            required_options_table = PrettyTable()
            required_options_table.field_names = ["option", "value", "default", "description"]
            for required_option in self.current_module.options["required"]:
                required_options_table.add_row(
                    [
                        required_option,
                        self.current_module.options["required"][required_option]["value"],
                        self.current_module.options["required"][required_option]["default"],
                        self.current_module.options["required"][required_option]["description"]
                    ]
                )
            optional_options_table = PrettyTable()
            optional_options_table.field_names = ["option", "value", "default", "description"]
            for optional_option in self.current_module.options["optional"]:
                optional_options_table.add_row(
                    [
                        optional_option,
                        self.current_module.options["optional"][optional_option]["value"],
                        self.current_module.options["optional"][optional_option]["default"],
                        self.current_module.options["optional"][optional_option]["description"]
                    ]
                )
            print(green("\nREQUIRED OPTIONS:"))
            print(required_options_table)
            print(green("\nOPTIONAL OPTIONS:"))
            print(optional_options_table)
