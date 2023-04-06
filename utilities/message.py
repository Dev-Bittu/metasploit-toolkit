from .color import red, yellow, blue, green

def danger(msg: str) -> str:
    return red("[-] ") + msg

def success(msg: str) -> str:
    return green("[+] ") + msg

def warn(msg: str) -> str:
    return yellow("[!] ") + msg

def info(msg: str) -> str:
    return blue("[?] ") + msg
