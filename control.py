from tick import TickMachine
import add, remove, tabulate, change
from itemhandler import ItemHandler
from config import config
from helper import Helper
import bcolors as bc
def executeCommand(arr):
    if len(arr) == 3:
        if arr[0].lower() == "helix":
            if arr[1].lower() == "add":
                add.addTask(arr[2])
            elif arr[1].lower() == "rm":
                remove.removeTask(arr[2])
            elif arr[1].lower() == "tick":
                TickMachine.tick(arr[2])
            elif arr[1].lower() == "untick":
                TickMachine.untick(arr[2])
            # elif arr[1].lower() == "change":
            #   if len(arr)

            items = ItemHandler.loadItems()
    elif len(arr) == 1 and arr[0].lower() == "helix":
        items = ItemHandler.loadItems()
        showOverview(items)
    elif len(arr) == 2 and arr[0].lower() == "helix" and arr[1].lower() == "help":
        Helper()
        help(change.ItemChanger)
    if arr[0].lower() == "exit" or arr[0].lower() == "quit": exitHelix(True)


def showOverview(arr):
    table = []
    for i in arr:
        row = []
        row.append(i.state)
        row.append(i.title)
        row.append(i.description)
        table.append(row)
    print("\n" + tabulate.tabulate(table, headers=["status", "title", "description"], tablefmt='orgtbl') + "\n")

def getItemPath(title):
    return f"{config.helixDir}{title}.todo"

def exitHelix(really):
    if really == True:
        print(bc.col.OKBLUE + "\nExiting...\n" + bc.col.ENDC + bc.col.OKGREEN + "See you later Alligator!\n" + bc.col.ENDC)
        exit(0)
    else:
        print(bc.col.WARNING + "\nYou nerd dude! Shame on you ;)\n" + bc.col.ENDC)
