
class Helper:
    def __init__(self):
        control.ItemHandler.__doc__ = "handles item loading and properties"
        control.ItemHandler.getProperty.__doc__ = "gets property of specified item (task/project)"
        control.ItemHandler.loadItems.__doc__ = "returns all tasks saved in helix-todos directory"
        control.StateHandler.__doc__ = "utilities for handling states"
        control.StateHandler.getAppropriateState.__doc__ = "returns the best state the task/item should have (if active)\nExample: 'active' if due_date == today; 'urgent' if deadline == today"
        control.StateHandler.getDateString.__doc__ = "returns the date as a string. ['2019-09-25']"
        control.executeCommand.__doc__ = "basis for handling input commands. calls functions for adding/removing/etc. items and equally important stuff"
        control.getItemPath.__doc__ = "returns path of the file corresponding to a specific task/project"
        control.exitHelix.__doc__ = "exits helix if wanted to"
        control.showOverview.__doc__ = "uses tabulate to present the tasks from input"

        change.ItemChanger.__doc__ = "utilities for changing tasks/projects"
        change.ItemChanger.changeTask.__doc__ = "gets task properties from input and applies them to the specified task"
        change.ItemChanger.changeProject.__doc__ = "gets project properties from input and applies them to the specified project"

        main.__doc__ = "the entry point of the script for very basic structure (calls control.executeCommand)"