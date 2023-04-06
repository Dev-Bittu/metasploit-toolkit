from os.path import (
    dirname, 
    realpath, 
    join
)
from json import load


BASE_DIR = dirname(realpath(__file__))

with open(join(BASE_DIR, "core", "package_info.json"), 'r') as f:
    PACKAGE_INFO = load(f)

