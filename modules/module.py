from typing import Dict
from utilities.color import (
    green, 
    blue,
    red,
    underline
)
from utilities.message import (
    success, 
    danger
)
from core.console import Console

class BaseModule:
    def __init__(self):
        self.auther = "Dev-Bittu (Bittu)"
        self.options = {
            "required": {
                "option": {
                    "value": "this is value",
                    "default": "this is default value",
                    "description": "This is description"
                }
            },
            "optional": {
                "option": {
                    "value": "this is value",
                    "default": "this is default value",
                    "description": "This is description"
                }
            }
        }
        self.required_fields = []
        self.reference_link = ["https://github.com/Dev-Bittu/metasploit-toolkit"]  # Reference Link for guidance
        self.type = None  # Exploit/Auxiluary
        self.module_name = None # Exploit/Auxiliary path without exploit/auxiluary written on it

    def run(self):
        for required_option in self.options["required"].keys():
            if self.options["required"][required_option]["value"] is None and self.options["required"][required_option]["value"] is None:
                print(
                    danger(f"Option {required_option} is required, Set its value first.\nRun this command to set value.\n\tset {required_option} <value>")
                )
                break
        else:
            self.onrun()
            self.main()
            self.onend()

    def main(self):
        raise NotImplementedError

    def onload(self, console_object: Console=None):
        print(
            success(f"Loading {self.type}...")
        )
        if console_object is not None:
            self.change_shell_input(console_object)

    def onrun(self):
        print(
            success(f"Running {self.type}...")
        )

    def onend(self):
        print(
            success(f"{self.type}... done")
        )
    def change_shell_input(self, console_object=None):
        console_object.shell_input = f"{underline('mst')} {red(self.type+'(')}{green(self.module_name)}{red(')')} > "


class BaseExploit(BaseModule):
    def __init__(self):
        super().__init__()
        self.type = "exploit"
        self.cve = None

    def main(self):
        raise NotImplementedError

class BaseAuxiliary(BaseModule):
    def __init__(self):
        super().__init__()
        self.type = "auxiliary"
        self.cve = None

    def main(self):
        raise NotImplementedError
