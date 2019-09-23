import os, pickle, add, remove, tabulate

def loadItems():
    items = []
    for i in os.listdir("/home/miguel/helix-todos/"):
        f = open("/home/miguel/helix-todos/" + i, "rb")
        obj = pickle.load(f)
        items.append(obj)
        f.close()
    return items

def executeCommand(arr):
    if len(arr) == 3:
        if arr[0].lower() == "helix":
            if arr[1].lower() == "add":
                add.addTask(arr[2])
                items = loadItems()
            elif arr[1].lower() == "rm":
                remove.removeTask(arr[2])
                items = loadItems()
    elif len(arr) == 1 and arr[0].lower() == "helix":
        items = loadItems()
        showOverview(items)

def showOverview(arr):
    table = []
    for i in arr:
        row = []
        row.append(i.state)
        row.append(i.title)
        row.append(i.description)
        table.append(row)
    
    print("\n" + tabulate.tabulate(table, headers=["status", "title", "description"], tablefmt='orgtbl') + "\n")