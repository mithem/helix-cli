import control
from statehandler import StateHandler
from itemhandler import ItemHandler
from change import ItemChanger

class Helper:
    def __init__(self):
        ItemHandler.__doc__ = "handles item loading and properties"
        ItemHandler.getProperty.__doc__ = "gets property of specified task"
        ItemHandler.loadItems.__doc__ = "returns all tasks saved in helix-todos directory"
        StateHandler.__doc__ = "utilities for handling states"
        StateHandler.getAppropriateState.__doc__ = "returns the best state the task/item should have (if active)\nExample: 'active' if due_date == today; 'urgent' if deadline == today"
        StateHandler.getDateString.__doc__ = "returns the date as a string. ['2019-09-25']"
        control.executeCommand.__doc__ = "basis for handling input commands. calls functions for adding/removing/etc. items and equally important stuff"
        control.getItemPath.__doc__ = "returns path of the file corresponding to a specific task"
        control.exitHelix.__doc__ = "exits helix if wanted to"
        control.showOverview.__doc__ = "uses tabulate to present the tasks from input"

        ItemChanger.__doc__ = "utilities for changing tasks"
        ItemChanger.changeTask.__doc__ = "gets task properties from input and applies them to the specified task"
