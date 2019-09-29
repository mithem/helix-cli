class ItemHandler:
    def loadItems(self):
        items = []
        for i in os.listdir("/home/miguel/helix-todos/"):
            f = open("/home/miguel/helix-todos/" + i, "rb")
            obj = pickle.load(f)
            items.append(obj)
            f.close()
        return items
    
    def getProperty(self, item_title, property):
        items = self.loadItems()
        item_titles = []
        for i in items:
            item_titles.append(i.title)
        item = items[item_titles.index(item_title)]
        if property == "description": return item.description
        elif property == "state": return item.state
        elif property == "due_date": return item.due_date
        elif property == "deadline": return item.deadline
        elif property == "children": return item.children