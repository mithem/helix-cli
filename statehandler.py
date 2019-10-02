from itemhandler import ItemHandler
from datetime import datetime
class StateHandler:
    """utilities commonly used when working with states"""
    def getDateString(date):
        """returns iso-date-string of specified date"""
        return str(f"{date.year}-{date.month}-{date.day}")

    def getAppropriateState(title):
        """returns appropriate state depending of due_date and deadline"""
        if ItemHandler.getProperty(title, "due_date") == StateHandler.getDateString(datetime.now()):
            return "active"
        elif ItemHandler.getProperty(title, "due_date") == None:
            return "upcoming"
        elif ItemHandler.getProperty(title, "deadline") == None:
            return "upcoming"
        elif ItemHandler.getProperty(title, "deadline") == StateHandler.getDateString(datetime.now()):
            return "urgent"
