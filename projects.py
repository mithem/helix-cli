class Project():
    def __init__(self, title, identifier):
        self.title = title
        self.identifier = identifier
        self.descripton = None
        self.due_date = None
        self.deadline = None
        self.children = []
        self.state = "upcoming"