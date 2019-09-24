import control, pickle, add, remove
import bcolors as bc
import control
from change import ItemChanger

class TickMachine:
    def tick(title):
        description = control.ItemHandler.getProperty(title, "description")
        due_date = control.ItemHandler.getProperty(title, "due_date")
        deadline = control.ItemHandler.getProperty(title, "deadline")
        children = control.ItemHandler.getProperty(title, "children")
        ItemChanger.changeTask(title, description, due_date, deadline, children, state="completed", readback=False)
        print(bc.col.OKGREEN + f"Ticked: {title}" + bc.col.ENDC)
    
    def untick(title):
        description = control.ItemHandler.getProperty(title, "description")
        due_date = control.ItemHandler.getProperty(title, "due_date")
        deadline = control.ItemHandler.getProperty(title, "deadline")
        children = control.ItemHandler.getProperty(title, "children")
        ItemChanger.changeTask(title=title, description=description, due_date=due_date, deadline=deadline, children=children, state=control.StateHandler.getAppropriateState(title), readback=False)
        print(bc.col.OKGREEN + f"Unticked: {title}" + bc.col.ENDC)
