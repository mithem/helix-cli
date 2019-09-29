import os, pickle
from items import Task
from config import config

for i in range(10):
    task = Task("test" + str(i), description="Hello World" + str(i), due_date="in 1 Minute", deadline="morgen", children=[Task("Item 1"), Task("Item 2")])
    f = open(config.helixDir+str(i), "wb")
    pickle.dump(task, f)
    f.close()