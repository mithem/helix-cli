"""The script for settings up the environment (optionally)
"""

import os, config, shutil
from bcolors import col

try:
    import pickle
except ImportError:
    print(col.FAIL + "Please make sure to install pickle: pip3 install pickle" + col.ENDC)
try:
    import tabulate
except ImportError:
    print(col.FAIL + "Please make sure to install tabulate: pip3 install tabulate" + col.ENDC)

answer = input("Do you want to copy this repo in the path specified in config.py?[y/N]\n(" + config.config.setupDir + ")")
if answer.lower() == "y":
    if os.path.isdir(config.config.setupDir):
        files = [
            "add.py",
            "bcolors.py",
            "change.py",
            "config.py",
            "control.py",
            "helix.py",
            "itemhandler.py",
            "items.py",
            "remove.py",
            "setup.py",
            "statehandler.py",
            "things.py",
            "tick.py"
        ]
        try:
            for i in os.listdir("."):
                if i in files:
                    shutil.copy(i, config.config.setupDir)
        except PermissionError:
            print(col.FAIL + "Permission error. Make sure to run this script with sudo." + col.ENDC)