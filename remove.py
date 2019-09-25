import pickle, os
from tasks import Task
from projects import Project
import bcolors as bc

def removeTask(title, readback=True):
    file_path = f"/home/miguel/helix-todos/{title}.todo"
    os.remove(file_path)
    if (readback):print(bc.col.OKGREEN + f"Removed task: {title}" + bc.col.ENDC)

def removeProject(title, readback=True):
    file_path = f"/home/miguel/helix-todos/{title}.todo"
    os.remove(file_path)
    if (readback):print(bc.col.OKGREEN + f"Removed project: {title}" + bc.col.ENDC)