"""Handles most (important) stuff

Gets command from helix.py, parses arguments, calls appropriate methods corresponding to command.
Also includes small utulities.
"""

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
import bcolors as bc


def parseArguments(args):
    """parses arguments

    Returns a dictionary with arguments as keys and parameters (values) as values
    Example: -d test -> 'description': 'test'
    """

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
    """handles command execution

    calls add, remove, change, help, tick, untick, things3-export and the exit function
    """
    try:
        if len(arr) >= 2:
            if arr[0].lower() == "add":
                emptyParameters = {
                    "description": None,
                    "due_date": None,
                    "deadline": None,
                    "children": [],
                    "state": "upcoming",
                    "completion_date": None
                }
                paras = {**emptyParameters, **parseArguments(arr)}
                add.addTask(arr[1], paras["description"], paras["due_date"], paras["deadline"], paras["children"], paras["state"], paras["completion_date"], True)
            elif arr[0].lower() == "rm":
                if arr[1] == "*":
                    for i in ItemHandler.loadItems():
                        remove.removeTask(i.title)
                else:
                    for i in range(2, len(arr)):
                        remove.removeTask(arr[i])
            elif arr[0].lower() == "tick":
                TickMachine.tick(arr[1])
            elif arr[0].lower() == "untick":
                TickMachine.untick(arr[1])
            elif arr[0].lower() == "change":
                prevParameters = {
                    "description": ItemHandler.getProperty(arr[1], "description"),
                    "due_date": ItemHandler.getProperty(arr[1], "due_date"),
                    "deadline": ItemHandler.getProperty(arr[1], "deadline"),
                    "children": ItemHandler.getProperty(arr[1], "children"),
                    "state": ItemHandler.getProperty(arr[1], "state"),
                    "completion_date": ItemHandler.getProperty(arr[1], "completion_date"),
                }
                newParamters = {}
                newParamters["children"] = []
                newParamters = parseArguments(arr)
                paras = {**prevParameters, **newParamters}
                try:
                    for i in range(len(prevParameters["children"]) + len(newParamters["children"])):
                        try:
                            if not prevParameters["children"][i] in paras["children"]:
                                paras["children"].append(prevParameters["children"][i])
                            if not newParamters["children"][i] in paras["children"]:
                                paras["children"].append(newParamters["children"][i])
                        except:
                            pass
                except KeyError:
                    pass
                if change.ItemChanger.changeTask(arr[1], paras["description"], paras["due_date"], paras["deadline"], paras["children"], paras["state"], paras["completion_date"], False):
                    print(bc.col.OKGREEN + "Changed task: " + arr[1] + bc.col.ENDC)
                else:
                    print(bc.col.WARNING + "Error while changing task. Some attributes may have changes though" + bc.col.ENDC)
            elif arr[0].lower() == "things":
                if arr[1] == "*":
                    Things3Helper.export2Things3(Things3Helper, ItemHandler.loadItems())
                else:
                    todos_to_export = []
                    for i in range(1, len(arr)):
                        for j in ItemHandler.getItems(title=arr[i]):
                            todos_to_export.append(j)
                    if todos_to_export != []:
                        Things3Helper.export2Things3(Things3Helper, todos_to_export)
                    else:
                        print(bc.col.WARNING + "No tasks found. Please make sure the name is valid or try again with * as the selector")
            items = ItemHandler.loadItems()
        elif len(arr) == 1 and "helix" in arr[0].lower():
            items = ItemHandler.loadItems()
            showOverview(items)
        if len(arr) >= 2 and arr[0].lower() == "helix" and arr[0].lower() == "help":
            try:
                help(arr[1])
            except IndexError:
                print("For usage instructions see USAGE.md")
        if arr[0].lower() == "exit" or arr[0].lower() == "quit" or arr[0].lower() == "bye": exitHelix(True)
    except Exception as e:
        print(bc.col.FAIL + "Error while executing command. Error: " + str(e) + bc.col.ENDC)
        return False

def showOverview(arr):
    """displays list of tasks using tabulate"""
    table = []
    for i in arr:
        row = []
        row.append(i.state)
        row.append(i.title)
        if i.description != None: row.append(i.description)
        else: row.append("None")
        if i.children != []:
            childrenView = []
            for j in i.children:
                try:
                    childrenView.append(j.title)
                except AttributeError:
                    continue
            row.append(tabulate.tabulate(childrenView))
        else: row.append("None")
        if i.due_date != None: row.append(i.due_date)
        else: row.append("None")
        if i.deadline != None: row.append(i.deadline)
        else: row.append("None")
        table.append(row)
    print("\n" + tabulate.tabulate(table, headers=["status", "title", "description", "subtasks", "due date", "deadline"], tablefmt='orgtbl') + "\n")

def getItemPath(title):
    """returns the file path of the task"""
    return f"{config.helixDir}{title}.todo"

def getItemObject(title):
    """returns the object of specified task"""
    try:
        f = open(getItemPath(title), "rb")
    except FileNotFoundError:
        print(bc.col.FAIL + "Item not found: " + title + bc.col.ENDC)
        return None
    obj = pickle.load(f)
    f.close()
    return obj

def exitHelix(really):
    """exits the program"""
    if really == True:
        print(bc.col.OKBLUE + "\nExiting...\n" + bc.col.ENDC + bc.col.OKGREEN + "See you later Alligator!\n" + bc.col.ENDC)
        exit(0)
        quit(0)
    else:
        print(bc.col.WARNING + "\nYou nerd dude! Shame on you ;)\n" + bc.col.ENDC)
