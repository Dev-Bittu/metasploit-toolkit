from ftplib import FTP
from modules.module import BaseAuxiliary
from utilities.message import info


class Auxiliary(BaseAuxiliary):
    def __init__(self):
        self.options = {
            "required": {
                "host": None,
                "default": "127.0.0.1",
                "help":"Host IP"
            },
            "optional": {
                "port": None,
                "default": 21,
                "description": "port"
            }
        }

    def main(self):
        try:
            ftp = FTP(self.options["required"]["host"])
            ftp.login('anonymous')
            print(
                info(f"Host is Vulnerable with Anonymous Login By FTP.\nYou can exploit it with exploit/ftp/anonymous_ftp")
            )
            ftp.quit()
        except Exception:
            print(
                info("Host is likely not Vulnerbale")
            )
