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
    green,
    blue
)
from utilities.screen_cleaner import clear
from importlib import import_module
from prettytable import PrettyTable


class Console:
    """
    The Console class.
    """
    def __init__(self) -> None:
        self.auther = "Dev-Bittu (Bittu)"
        self.shell_input = f"{underline('mst')} > "
        self.current_module = None

    def console(self):
        """
        get input by console,
        and response according to shell_input
        """
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
            elif query in ("run", "exploit"):
                self.run()
            elif query == "info":
                self.info()
            else:
                print(info(f"Command \"{query}\" not found. Executing in system"))
                system(query)

    def start_console(self):
        """
        Show banner, 
        and Check pdate
        """
        banner_thread = Thread(target=banner,args=(join(BASE_DIR, "modules"),))
        update_thread = Thread(target=check_update,args=())
        
        banner_thread.start()
        update_thread.start()

        update_thread.join()
        banner_thread.join()

    def help(self):
        """
        Show basic information
        """
        print('This is help')

    def load_module(self, module_name):
        """
        Load module, 
        when "use " get called
        """
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
        """
        Check if module_name exists.
        """
        return exists(join(BASE_DIR, "modules", module_name+".py"))
    
    def set_option(self, option, value):
        """
        Set option with value to current module
        """
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
        """
        Show all options and their values (required/optional) in prompt
        """
        if self.module_status():
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
    
    def run(self):
        """
        Start execution of module,
        run/exploit command will start this method
        """
        if module:=self.module_status():
            module.run()

    def info(self):
        """
        Show information about current module,
        like its's Auther, Options ,, Reference Links
        """
        print(f"{blue('Module Type')}: {self.current_module.type}\t{blue('Module Name')}: {self.current_module.module_name}\n")
        print(f"{blue('Required Options')}: {self.current_module.options['required'].keys()}\n")
        print(f"{blue('Optional Options')}: {self.current_module.options['optional'].keys()}\n")
        print(f"{blue('About the exploit')}:\n{self.current_module.about}\n")
        print(f"{blue('Auther')}: {self.current_module.auther}\n")
        print(f"{blue('Reference Links')}: {self.current_module.reference_links}\n")

    def module_status(self):
        """
        Check, Is current module none.
        return:
            None, if current_module is None and print a msg
            Module Object, if current_module is not None
        """
        if self.current_module is None:
            return print(
                warn("Not any module using")
            )
        else:
            return self.current_module
