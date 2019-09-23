import os, pickle, add, remove

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
    print("status" + " "*4 + "title" + " "*5 + "description")
    print("-"*50)
    for i in arr:
        print(i.state + " "*3 + i.title + " " * 5 + str(i.description))