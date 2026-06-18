# TODO List CLI Application

## Goal

Implement a command-line TODO list application with a REPL interface.

## Features

### Add task
Command:

add <description>

Example:

add Buy milk

### Complete task
Command:

done <id>

Example:

done 1

### Delete task
Command:

delete <id>

Example:

delete 1

### List tasks
Command:

list

Shows all tasks.

### List range
Command:

list <start_id> <end_id>

Example:

list 1 5

### Exit
Command:

exit

Terminates the application.

## Task structure

Each task contains:

- id
- description
- completed status

## Requirements

- Python 3
- Persistent storage in tasks.json
- Input validation
- Friendly error messages

