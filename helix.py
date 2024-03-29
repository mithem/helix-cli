"""helix-cli entry script

This script handles the loop of parsing commands and executing them.
Usage: helix help
"""

from itemhandler import ItemHandler
import control, re
import bcolors as bc
items = ItemHandler.loadItems()

try:
    pattern = re.compile(r'''((?:[^ "']|"[^"]*"|'[^']*')+)''')
    print(bc.col.OKGREEN + "\nStarted" + bc.col.ENDC)
    while True:
        command = pattern.split(input())
        for i in command:
            if i == "":
                command.remove(i)
            elif i == " ":
                command.remove(i)
        control.executeCommand(command)
except KeyboardInterrupt:
    control.exitHelix(True)
