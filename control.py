import os, pickle, add, remove, tabulate, change
from tick import TickMachine
from datetime import datetime

class ItemHandler:
    def loadItems():
        items = []
        for i in os.listdir("/home/miguel/helix-todos/"):
            f = open("/home/miguel/helix-todos/" + i, "rb")
            obj = pickle.load(f)
            items.append(obj)
            f.close()
        return items
    
    def getProperty(item_title, property):
        items = ItemHandler.loadItems()
        item_titles = []
        for i in items:
            item_titles.append(i.title)
        item = items[item_titles.index(item_title)]
        if property == "description": return item.description
        elif property == "state": return item.state
        elif property == "due_date": return item.due_date
        elif property == "deadline": return item.deadline
        elif property == "children": return item.children

class StateHandler:
    def getDateString(date):
        return str(f"{date.year}-{date.month}-{date.day}")
    def getAppropriateState(title):
        oldState = ItemHandler.getProperty(title, "state")
        if ItemHandler.getProperty(title, "due_date") == StateHandler.getDateString(datetime.now()):
            return "active"
        elif ItemHandler.getProperty(title, "due_date") == None:
            return "upcoming"
        elif ItemHandler.getProperty(title, "deadline") == None:
            return "upcoming"
        elif ItemHandler.getProperty(title, "deadline") == StateHandler.getDateString(datetime.now()):
            return "urgent"

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
            #elif arr[1].lower() == "change":
            #   if len(arr) 

            items = ItemHandler.loadItems()
                
    elif len(arr) == 1 and arr[0].lower() == "helix":
        items = ItemHandler.loadItems()
        showOverview(items)
    if arr[0].lower() == "exit" or arr[0].lower() == "quit": exit(0)

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
    return f"/home/miguel/helix-todos/{title}.todo"