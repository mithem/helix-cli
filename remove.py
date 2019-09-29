import os
from config import config
import bcolors as bc

def removeTask(title, readback=True):
    file_path = f"{config.helixDir}{title}.todo"
    try:
        os.remove(file_path)
        if (readback):print(bc.col.OKGREEN + f"Removed task: {title}" + bc.col.ENDC)
    except FileNotFoundError:
        print(bc.col.FAIL + "Task not found: " + title + bc.col.ENDC)

def removeProject(title, readback=True):
    file_path = f"{config.helixDir}{title}.todo"
    os.remove(file_path)
    if (readback):print(bc.col.OKGREEN + f"Removed project: {title}" + bc.col.ENDC)