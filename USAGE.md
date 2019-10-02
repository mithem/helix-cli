# helix-cli Usage

helix-cli is <b>not case-sensitive</b>.

## Commands

- add
- remove
- change
- tick
- untick
- things
- exit / quit/ bye
- help

### add
add [title] [parameters]

Adds a task with specified name & parameters

Parameters:

- -d: description
- -dt: duedate / when
- -dl: deadline
- -c: subtasks / children

### remove
remove [title]

Removes the task with specified title

### change
change [title] [parameters]

Overrides parameters of task with specified parameters

Parameters:

- -d: description
- -dt: duedate / when
- -dl: deadline
- -c: subtasks / children

### tick
tick [title]

Ticks / checks / (Updates the status to completed of) specified item

### untick
untick [title]

Unticks / unchecks specified item

### things
things [identifier]

exports all specified items to Things3. You can also add mutliple titles as identifier

identifiers:
- *: all tasks
- [title]: task with name 'title'

### exit / quit / bye
- exit
- quit
- bye

Exits the program