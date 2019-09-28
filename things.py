import pickle, webbrowser, os, datetime
from items import Task
from config import config

# get all tasks
taskObjs = []
direc = config.helixDir
for f in os.listdir(direc):
    if not f == ".DS_Store":
        fi = open(direc+f, "rb")
        obj = pickle.load(fi)
        taskObjs.append(obj)
        fi.close()


# append all task names to link, so Things3 knows
# which tasks (more than one) to add
for i in taskObjs:
    link = "things:///add?title="
    link += str(i.title) + "1%0A"
    link = link[:-4]
    if i.description != None:
        link += "&notes=" + str(i.description).replace(" ", "%20")
    if i.due_date != None:
        link += "&when=" + str(i.due_date).replace(" ", "%20").replace(":", "%3A")
    if i.deadline != None:
        link += "&deadline=" + str(i.deadline).replace(" ", "%20")
    if i.children != []:
        link += "&checklist-items="
        subtask_titles = []
        for j in i.children:
            subtask_titles.append(j.title)
        for k in subtask_titles:
            link += str(k).replace(" ", "%20") + "%0A"
        link = link[:-4]
    link += "creation-date=" + str(datetime.datetime.now().isoformat())
    link += "&reveal=true"
    webbrowser.open(link)