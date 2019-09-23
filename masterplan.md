# ToDo-App Helix masterplan

A ToDo-App which shall be as flexible and modular as possible. Of course I just want to learn something but it would obviously be great if it would be actually useful.
This version of the masterplan was created on September 21st 2019, a few stylistic corrections were made on September 23rd 2019.

## General data

- Name: Helix
- Source Control: git/GitHub
- License: Lawyer, please!
- Languages:

- Python for CLI
- HTML, CSS, JS, maybe PHP (please not) and probably SQL for the webapp (maybe react?)
- Timeline: probably no larger scale one as it might be a larger project with lots of unknowns. Will try to organize everything in Things 3 (would really like to have a MacBook Pro 😅)
- Note: I first want to build out the CLI completely, the webclient isn‘t necessary but would be an interesting choice for expansion

## Commandline interface (cli)

### General

- Data including tasks/projects etc. will be stored in local files, cloud sync may be possible (necessary) for webapp.
- The main.py script should be the entry point for helix and should deal with redirecting to different functions, which are outsourced in [different files](####Files)
- To save the files, i will probably be using the pickles module (specifically pickle.dump() and pickle.load())
- For better performance, i will be waiting for input in main.py after startup, so the instances of classes don‘t have to be loaded for every command

### Structure

#### Classes

- checklist item1
- project 2
  - project 2 item 1

- Task:
  - Title
    - ID
      - Optional:
        - Description
        - Date/time due (to remind)
        - Deadline
        - Children: list(Tasks, Projects)
    - State (upcoming, due (actually right now), completed, canceled)
      - If state == completed || canceled, then the date when it was ticked/scrubbed should be added as state_updated
- Project
  - Title
  - ID
    - Optional:
      - Description
      - Date/time due (to remind)
      - Deadline
      - Children: list(Tasks, Projects)
    - State (upcoming, due (actually right now), completed, canceled)

#### Commands

It doesn‘t matter whether commands like "Helix add" are written like "hEliX aDd". The same rule applies for the user searching for a task/project by name; When adding Tasks/Projects the input IS case-sensitive.

- Helix
  - Helix: Show current status with due tasks, planned for today
    - Helix -s [searchString]: search for task by name and show all hits
    - Helix -i [id]: search for task by id and show all hits
    - Helix -h: show help
- Helix add
  - Helix add -parameter [arg]: add task/project
  - Parameters:
    - -t [name]: add task with title of _name_
    - -p [name] add project with title of _name_
    - Optional parameters:
      - -d [description]: description of the the task/project
      - -dt [date]: due date
      - -dl [date]: deadline
      - -cn [name]: parent of the new task/project (can be either a task or project); string
      - -ci [id]: parent of the new task/project (can be either a task or project); int
    - Order of parameters shall not have an effect on execution
- Helix rm
  - Helix rm -parameter [arg]: remove a task/project
  - Parameters:
    - Helix rm -s [name]: remove all tasks/projects with _name_
    - Helix rm -i [id]: remove all tasks/projects with _id_
- Helix change
  - Helix change -selectiveParameter -changeParameters
  - selectiveParameters:
    - -s [name]: select all tasks/projects with _name_
    - -i [id]: select all tasks/projects with _id_
  - changeParameters:
    - -d [description]: description of the the task/project
    - -dt [date]: due date
    - -dl [date]: deadline
    - -cn [name]: parent of the task/project (can be either a task or project); string
    - -ci [id]: parent of the task/project (can be either a task or project); int
  - Order of parameters shall not have an effect on execution
- Helix tick
  - Helix tick -[parameter] [identifier]
  - Parameters:
    - -s [name]: tick all tasks/projects by _name_
    - -i [id]: tick task/project by _id_
- Helix untick
  - Helix untick -[parameter] [identifier]
  - Parameters:
    - -s [name]: untick all tasks/projects by _name_
    - -i [id]: untick task/project by _id_

#### Files

- masterplan.md
- README.md
- LICENSE
- [help.py](#####help.py)
- [main.py](#####main.py)
- [add.py](#####add.py)
- [remove.py](#####remove.py)
- [change.py](#####change.py)
- [task.py](#####task.py)
- [project.py](#####project.py)
- [tick.py](#####tick.py)

##### help.py

##### main.py

Handle args and call functions in other modules (depending on command)

##### add.py

[see commands](####Commands)

##### remove.py

[see commands](####Commands)

##### change.py

[see commands](####Commands)

##### task.py

[see classes](####classes)

##### project.py

[see classes](####classes)

##### tick.py

Functions:

- tick(item)
  - Add/change state_updated variable to/of item
- untick(item)
  - Remove state_updated variable from item
- cancel(item)
  - Add/change state_updated variable to/of item

## (Maybe) webclient (no idea how to do that yet)
