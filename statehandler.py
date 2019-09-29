from itemhandler import ItemHandler
from datetime import datetime


class StateHandler:
    def getDateString(self, date):
        return str(f"{date.year}-{date.month}-{date.day}")
    def getAppropriateState(self, title):
        item_handler = ItemHandler()
        if item_handler.getProperty(title, "due_date") == self.getDateString(datetime.now()):
            return "active"
        elif item_handler.getProperty(title, "due_date") == None:
            return "upcoming"
        elif item_handler.getProperty(title, "deadline") == None:
            return "upcoming"
        elif item_handler.getProperty(title, "deadline") == self.getDateString(datetime.now()):
            return "urgent"