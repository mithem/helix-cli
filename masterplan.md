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
- Timeline: probably no larger scale one as it might be a larger project with lots of unknowns. Will try to organize everything in Things 3 (would really like to have a MacBook Pro 😅) [Now have one 😀]
- Note: I first want to build out the CLI completely, the webclient isn‘t necessary but would be an interesting choice for expansion

## Commandline interface (cli)

### General

- Data including tasks etc. will be stored in local files, cloud sync may be possible (necessary) for webapp.
- The helix.py script should be the entry point for helix and should deal with redirecting to different functions, which are outsourced in [different files](####Files)
- To save the files, I will probably be using the pickles module (specifically pickle.dump() and pickle.load())
- For better performance, iI will be waiting for input in helix.py after startup, so the instances of classes don‘t have to be loaded for every command

### Structure

#### Classes

- Task:
  - Title
  - ID
    - Optional:
      - Description
      - Date/time due (to remind)
      - Deadline
      - Children: list(Tasks)
  - State (upcoming, due (actually right now), completed, canceled)
    - If state == completed || canceled, then the date when it was ticked/scrubbed should be added as state_updated


#### Commands

It doesn‘t matter whether commands like "Helix add" are written like "hEliX aDd". The same rule applies for the user searching for a task by name; When adding Tasks the input IS case-sensitive.

- Helix
  - Helix: Show current status with due tasks, planned for today
    - Helix -s [searchString]: search for task by name and show all hits
    - Helix -i [id]: search for task by id and show all hits
    - Helix -h: show help
- Helix add
  - Helix add -parameter [arg]: add task
    - parameters:
      - -d [description]: description of the the task
      - -dt [date]: due date
      - -dl [date]: deadline
      - -c [name]: parent of the new task (task (title))
    - Order of parameters shall not have an effect on execution
- Helix rm
  - Helix rm [taskname]: remove a task
- Helix change
  - Helix change [taskname] -parameters
  - parameters:
    - -t [title]: new title of the task
    - -d [description]: description of the the task
    - -dt [date]: due date
    - -dl [date]: deadline
    - -c [name]: parent of the task (task)
  - Order of parameters shall not have an effect on execution
- Helix tick
  - Helix tick [taskname]
- Helix untick
  - Helix untick [taskname]

#### Files

- masterplan.md
- README.md
- LICENSE
- requirements.txt
- [helper.py](#####helper.py)
- [helix.py](#####helix.py)
- [add.py](#####add.py)
- [remove.py](#####remove.py)
- [change.py](#####change.py)
- [task.py](#####task.py)
- [tick.py](#####tick.py)
- [bcolors.py](#####bcolors.py)
- [things.py](#####things.py)
- [itemhandler.py](#####itemhandler.py)
- [statehandler.py](#####statehandler.py)

##### helper.py

##### helix.py

Handle args and call functions in other modules (depending on command)

##### add.py

[see commands](####Commands)

##### remove.py

[see commands](####Commands)

##### change.py

[see commands](####Commands)

##### task.py

[see classes](####classes)

##### tick.py

Functions:

- tick(item)
  - Add/change state_updated variable to/of item
- untick(item)
  - Remove state_updated variable from item
- cancel(item)
  - Add/change state_updated variable to/of item

##### bcolors.py

- easy access to colored prints in development

##### things.py

- handle _helix things_ command
- get items, convert them into a text file (as Things3 wants it) -> dump them

##### itemhandler.py

- handle items:
  - load all items
  - get items with query (title, description etc)
  - get property of specific item (identified by title)

##### statehandler.py

- utilities for task states:
  - get date string of given date
  - get state most appropriate (given due_date etc)

##### config.py

- holds directory for todos

## (Maybe) webclient (no idea how to do that yet)
