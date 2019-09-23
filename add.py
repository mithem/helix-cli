import pickle, os
from tasks import Task
from projects import Project
import bcolors as bc

def addTask(title, description=None, due_date=None, deadline=None, children=None, state="upcoming"):
    task = Task(title, description, due_date, deadline, children, state)
    file_path = f"/home/miguel/helix-todos/{title}.todo"
    f = open(file_path, "wb")
    pickle.dump(task, f)
    f.close()
    print(bc.col.OKGREEN + f"Added: {title}" + bc.col.ENDC)
    return task