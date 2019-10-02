from items import Task
import control, pickle
import bcolors as bc
from itemhandler import ItemHandler

def addTask(title, description=None, due_date=None, deadline=None, children=[], state="upcoming", completion_date=None, readback=True):
    """writes a new file to disk"""
    new_children = []
    response_code = 0
    for i in children:
        try:
            ItemHandler.getItems(title=i.title)
            new_children.append(i)
        except AttributeError:
            print(bc.col.WARNING + "Task doesn't exist. Not adding to children." + bc.col.ENDC)
            response_code = 404
            continue
    try:
        task = Task(title, description, due_date, deadline, new_children, state)
        file_path = control.getItemPath(title)
        f = open(file_path, "wb")
        pickle.dump(task, f)
        f.close()
        response_code = 200
    except:
        print(bc.col.FAIL + "Error while adding task" + bc.col.ENDC)
        response_code = 502
    if readback:
        print(bc.col.OKGREEN + f"Added task: {title}" + bc.col.ENDC)
    return response_code
