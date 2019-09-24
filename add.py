import pickle, os, control
from tasks import Task
from projects import Project
import bcolors as bc

def addTask(title, description=None, due_date=None, deadline=None, children=None, state="upcoming", readback=True):
    task = Task(title, description, due_date, deadline, children, state)
    file_path = control.getItemPath(title)
    f = open(file_path, "wb")
    pickle.dump(task, f)
    f.close()
    if (readback):print(bc.col.OKGREEN + f"Added: {title}" + bc.col.ENDC)
    return task