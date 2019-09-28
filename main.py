from itemhandler import ItemHandler
import control
import bcolors as bc
items = ItemHandler.loadItems()

try:
    print(bc.col.OKGREEN + "\nStarted" + bc.col.ENDC)
    while True:
        control.executeCommand(input().split(" "))
except KeyboardInterrupt:
    control.exitHelix(True)
