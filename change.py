import remove, add
class ItemChanger:
    def changeTask(title, description, due_date, deadline, children, state, completion_date, readback=True):
        remove.removeTask(title, readback)
        add.addTask(title=title, description=description, due_date=due_date, deadline=deadline, children=children, state=state, completion_date=completion_date, readback=readback)
    
    def changeProject(title, description, due_date, deadline, children, state, completion_date, readback=True):
        remove.removeProject(title, readback)
        add.addProject(title=title, description=description, due_date=due_date, deadline=deadline, children=children, state=state, completion_date=completion_date, readback=readback)