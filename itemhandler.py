"""Handles items
"""

import os, pickle
from config import config

class ItemHandler:
    """utilities for handling items
    """
    def loadItems():
        """returns all tasks saved locally on disk"""
        items = []
        for i in os.listdir(config.helixDir):
            if i != "Things3-export" and i != ".DS_Store":
                f = open(config.helixDir + i, "rb")
                obj = pickle.load(f)
                items.append(obj)
                f.close()
        return items

    def getItems(title=None, description=None, due_date=None, deadline=None, state=None, strict_mode=False):
        """returns all items matching a certain query"""
        all_items = ItemHandler.loadItems()
        queryItems = []
        for i in all_items:
            if (title != None) and (not strict_mode and title in i.title) or (strict_mode and str(i.title) == title):
                queryItems.append(i)
            if (description != None) and (not strict_mode and description in i.description) or (strict_mode and str(i.description) == description):
                queryItems.append(i)
            if (due_date != None) and (not strict_mode and due_date in i.due_date) or (strict_mode and str(i.due_date) == due_date):
                queryItems.append(i)
            if (deadline != None) and (not strict_mode and deadline in i.deadline) or (strict_mode and str(i.deadline) == deadline):
                queryItems.append(i)
            if (state != None) and (not strict_mode and state in i.state) or (strict_mode and str(i.state) == state):
                queryItems.append(i)
        return queryItems
                

    def getProperty(item_title, property):
        """returns a certain property of a certain item"""
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
