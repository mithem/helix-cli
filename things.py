import pickle, webbrowser, os, datetime
from items import Task
from config import config
from bcolors import col

class Things3Helper:
    def export2Things3(taskObjs):
        # append all task names to link, so Things3 knows
        # which tasks (more than one) to add
        for i in taskObjs:
            if taskObjs == None: print(col.FAIL + "Failed exporting to Things. Things3Helper didn't receive appropriate data." + col.ENDC)
            link = "things:///add?title="
            link += str(i.title)
            if i.description != None:
                link += "&notes=" + str(i.description).replace(" ", "%20").replace("'", "").replace('"', "")
            if i.due_date != None:
                link += "&when=" + str(i.due_date).replace(" ", "%20").replace(":", "%3A").replace("'", "").replace('"', "")
            if i.deadline != None:
                link += "&deadline=" + str(i.deadline).replace(" ", "%20").replace("'", "").replace('"', "")
            if i.children != []:
                link += "&checklist-items="
                subtask_titles = []
                for j in i.children:
                    subtask_titles.append(j.title)
                for k in subtask_titles:
                    link += str(k).replace(" ", "%20").replace("'", "").replace('"', "") + "%0A"
                link = link[:-4]
            link += "&creation-date=" + str(datetime.datetime.now().isoformat())[:9]
            link += "&reveal=true"
            webbrowser.open(link)