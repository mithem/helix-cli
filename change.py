import remove, add
from bcolors import col
class ItemChanger:
    def changeTask(title, description, due_date, deadline, children, state, completion_date, readback=True):
        """Changes a task
        
        Just removes old task and creates a new one
        """
        rmResp = remove.removeTask(title, readback)
        if rmResp == 200:
            addResp = add.addTask(title=title, description=description, due_date=due_date, deadline=deadline, children=children, state=state, completion_date=completion_date, readback=readback)
            if addResp != 200:
                print(col.FAIL + "Error while changing (adding) task. Error code: " + str(addResp))
        else:
            print(col.FAIL + "Error while changing (removing) task. Error code: " + str(rmResp))
        return rmResp == addResp == 200
