from itemhandler import ItemHandler
from datetime import datetime
class StateHandler:
    def getDateString(date):
        return str(f"{date.year}-{date.month}-{date.day}")

    def getAppropriateState(title):
        if ItemHandler.getProperty(title, "due_date") == StateHandler.getDateString(datetime.now()):
            return "active"
        elif ItemHandler.getProperty(title, "due_date") == None:
            return "upcoming"
        elif ItemHandler.getProperty(title, "deadline") == None:
            return "upcoming"
        elif ItemHandler.getProperty(title, "deadline") == StateHandler.getDateString(datetime.now()):
            return "urgent"
