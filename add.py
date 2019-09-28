from items import Task, Project
import control, pickle
import bcolors as bc

def addTask(title, description=None, due_date=None, deadline=None, children=None, state="upcoming", completion_date=None, readback=True):
    task = Task(title, description, due_date, deadline, children, state)
    file_path = control.getItemPath(title)
    f = open(file_path, "wb")
    pickle.dump(task, f)
    f.close()
    if readback:
        print(bc.col.OKGREEN + f"Added task: {title}" + bc.col.ENDC)
    return task

def addProject(title, description=None, due_date=None, deadline=None, children=None, state="upcoming", completion_date=None, readback=True):
    project = Project(title, description, due_date, deadline, children, state)
    file_path = control.getItemPath(title)
    f = open(file_path, "wb")
    pickle.dump(project, f)
    f.close()
    if readback:
        print(bc.col.OKGREEN + f"Added project: {title}" + bc.col.ENDC)
    return project