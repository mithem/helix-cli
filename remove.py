import os
from config import config
import bcolors as bc

def removeTask(title, readback=True):
    """removes specified task from disk"""
    file_path = f"{config.helixDir}{title}.todo"
    try:
        os.remove(file_path)
        if (readback):print(bc.col.OKGREEN + f"Removed task: {title}" + bc.col.ENDC)
        response_code = 200
    except FileNotFoundError:
        print(bc.col.FAIL + "Task not found: " + title + bc.col.ENDC)
        response_code = 404
    except:
        print(bc.col.FAIL + "file exists but cannot be removed")
        response_code = 502
    return response_code
