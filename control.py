from tick import TickMachine
import add
import remove
import tabulate
import change
import pickle
import shutil
from things import Things3Helper
from itemhandler import ItemHandler
from config import config
from helper import Helper
import bcolors as bc


def parseArguments(args):
    try:
        arguments = {}
        for i in args:
            parameter = i
            try:
                argument = args[args.index(i)+1]
            except IndexError: continue
            if parameter == "-t":
                arguments['title'] = argument
            elif parameter == "-d":
                arguments['description'] = argument
            elif parameter == "-dt":
                arguments['due_date'] = argument
            elif parameter == "-dl":
                arguments['deadline'] = argument
            elif parameter == "-c":
                if getItemObject(argument) in arguments:
                    arguments['children'].append(getItemObject(argument))
                else:
                    arguments['children'] = [getItemObject(argument)]
        return arguments

    except IndexError:
        executeCommand("helix help change")
    except Exception as e:
        raise e

def executeCommand(arr):
    if len(arr) >= 3:
        if arr[0].lower() == "helix":
            if arr[1].lower() == "add":
                emptyParameters = {
                    "description": None,
                    "due_date": None,
                    "deadline": None,
                    "children": [],
                    "state": "upcoming",
                    "completion_date": None
                }
                paras = {**emptyParameters, **parseArguments(arr)}
                add.addTask(arr[2], paras["description"], paras["due_date"], paras["deadline"], paras["children"], paras["state"], paras["completion_date"], True)
            elif arr[1].lower() == "rm":
                if arr[2] == "*":
                    for i in ItemHandler.loadItems():
                        remove.removeTask(i.title)
                else:
                    for i in range(2, len(arr)):
                        remove.removeTask(arr[i])
            elif arr[1].lower() == "tick":
                TickMachine.tick(arr[2])
            elif arr[1].lower() == "untick":
                TickMachine.untick(arr[2])
            elif arr[1].lower() == "change":
                emptyParameters = {
                    "description": None,
                    "due_date": None,
                    "deadline": None,
                    "children": [],
                    "state": "upcoming",
                    "completion_date": None
                }
                paras = {**emptyParameters, **parseArguments(arr)}
                change.ItemChanger.changeTask(arr[2], paras["description"], paras["due_date"], paras["deadline"], paras["children"], paras["state"], paras["completion_date"], False)
                print(bc.col.OKGREEN + "Changed task: " + arr[2] + bc.col.ENDC)
            elif arr[1].lower() == "things":
                if arr[2] == "*":
                    Things3Helper.export2Things3(ItemHandler.loadItems())
                else:
                    todos_to_export = []
                    for i in range(2, len(arr)):
                        for j in ItemHandler.getItems(title=arr[i]):
                            todos_to_export.append(j)
                    Things3Helper.export2Things3(todos_to_export)
            items = ItemHandler.loadItems()
    elif len(arr) == 1 and arr[0].lower() == "helix":
        items = ItemHandler.loadItems()
        showOverview(items)
    if len(arr) >= 2 and arr[0].lower() == "helix" and arr[1].lower() == "help":
        Helper()
        try:
            help(arr[2])
        except IndexError:
            help()
    if arr[0].lower() == "exit" or arr[0].lower() == "quit": exitHelix(True)


def showOverview(arr):
    table = []
    for i in arr:
        row = []
        row.append(i.state)
        row.append(i.title)
        if i.description != None: row.append(i.description)
        else: row.append("None")
        if i.children != []:
            childrenView = []
            print(type(i.children))
            for j in i.children:
                childrenView.append(j.title)
            row.append(tabulate.tabulate(childrenView))
        else: row.append("None")
        if i.due_date != None: row.append(i.due_date)
        else: row.append("None")
        if i.deadline != None: row.append(i.deadline)
        else: row.append("None")
        table.append(row)
    print("\n" + tabulate.tabulate(table, headers=["status", "title", "description", "children", "due date", "deadline"], tablefmt='orgtbl') + "\n")

def getItemPath(title):
    return f"{config.helixDir}{title}.todo"

def getItemObject(title):
    try:
        f = open(getItemPath(title), "rb")
    except FileNotFoundError:
        print(bc.col.FAIL + "Item not found: " + title + bc.col.ENDC)
        return None
    obj = pickle.load(f)
    f.close()
    return obj

def exitHelix(really):
    if really == True:
        print(bc.col.OKBLUE + "\nExiting...\n" + bc.col.ENDC + bc.col.OKGREEN + "See you later Alligator!\n" + bc.col.ENDC)
        exit(0)
    else:
        print(bc.col.WARNING + "\nYou nerd dude! Shame on you ;)\n" + bc.col.ENDC)
