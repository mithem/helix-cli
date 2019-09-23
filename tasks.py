class Task():
    def __init__(self, title, description=None, due_date=None, deadline=None, children=[], state="upcoming"):
        self.title = title
        #self.identifier = identifier
        self.description = description
        self.due_date = due_date
        self.deadline = deadline
        self.children = children
        self.state = state