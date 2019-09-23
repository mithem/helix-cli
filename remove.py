import pickle, os
from tasks import Task
from projects import Project
import bcolors as bc

def removeTask(title):
    file_path = f"/home/miguel/helix-todos/{title}.todo"
    os.remove(file_path)
    print(bc.col.OKGREEN + f"Removed: {title}" + bc.col.ENDC)