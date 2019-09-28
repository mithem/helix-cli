import os, pickle
from config import config

class ItemHandler:
    def loadItems():
        items = []
        for i in os.listdir(config.helixDir):
            if i != "Things3-export" and i != ".DS_Store":
                f = open(config.helixDir + i, "rb")
                obj = pickle.load(f)
                items.append(obj)
                f.close()
        return items

    def getProperty(item_title, property):
        items = ItemHandler.loadItems()
        item_titles = []
        for i in items:
            item_titles.append(i.title)
        item = items[item_titles.index(item_title)]
        if property == "description": return item.description
        elif property == "state": return item.state
        elif property == "due_date": return item.due_date
        elif property == "deadline": return item.deadline
        elif property == "children": return item.children