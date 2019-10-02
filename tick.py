import change, control
import bcolors as bc
from statehandler import StateHandler

class TickMachine:
    """handles (un)ticking of tasks"""
    def tick(title):
        """ticks a task"""
        description = control.ItemHandler.getProperty(title, "description")
        due_date = control.ItemHandler.getProperty(title, "due_date")
        deadline = control.ItemHandler.getProperty(title, "deadline")
        children = control.ItemHandler.getProperty(title, "children")
        completion_date = control.ItemHandler.getProperty(title, "completion_date")
        change.ItemChanger.changeTask(title, description, due_date, deadline, children, state="completed", completion_date=completion_date, readback=False)
        print(bc.col.OKGREEN + f"Ticked: {title}" + bc.col.ENDC)
    
    def untick(title):
        """unticks a task"""
        description = control.ItemHandler.getProperty(title, "description")
        due_date = control.ItemHandler.getProperty(title, "due_date")
        deadline = control.ItemHandler.getProperty(title, "deadline")
        children = control.ItemHandler.getProperty(title, "children")
        completion_date = control.ItemHandler.getProperty(title, "completion_date")
        change.ItemChanger.changeTask(title=title, description=description, due_date=due_date, deadline=deadline, children=children, state=StateHandler.getAppropriateState(title), completion_date=completion_date, readback=False)
        print(bc.col.OKGREEN + f"Unticked: {title}" + bc.col.ENDC)
