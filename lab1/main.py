import json
import os
import sys

DATA_FILE = os.path.join(os.path.dirname(__file__), "tasks.json")


def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE) as f:
        return json.load(f)


def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def next_id(tasks):
    return max((t["id"] for t in tasks), default=0) + 1


def cmd_add(tasks, args):
    if not args:
        print("Usage: add <description>")
        return
    tasks.append({"id": next_id(tasks), "description": " ".join(args), "completed": False})
    save_tasks(tasks)
    print("Task added.")


def cmd_done(tasks, args):
    if not args or not args[0].isdigit():
        print("Usage: done <id>")
        return
    tid = int(args[0])
    for t in tasks:
        if t["id"] == tid:
            t["completed"] = True
            save_tasks(tasks)
            print(f"Task {tid} marked as done.")
            return
    print(f"Task with id {tid} not found.")


def cmd_delete(tasks, args):
    if not args or not args[0].isdigit():
        print("Usage: delete <id>")
        return
    tid = int(args[0])
    for i, t in enumerate(tasks):
        if t["id"] == tid:
            del tasks[i]
            save_tasks(tasks)
            print(f"Task {tid} deleted.")
            return
    print(f"Task with id {tid} not found.")


def cmd_list(tasks, args):
    if not tasks:
        print("No tasks.")
        return
    if len(args) == 2 and args[0].isdigit() and args[1].isdigit():
        start, end = int(args[0]), int(args[1])
        filtered = [t for t in tasks if start <= t["id"] <= end]
    elif args:
        print("Usage: list [<start_id> <end_id>]")
        return
    else:
        filtered = tasks

    if not filtered:
        print("No tasks in range.")
        return

    print(f"{'ID':<4} {'Status':<8} Description")
    for t in filtered:
        status = "[x]" if t["completed"] else "[ ]"
        print(f"{t['id']:<4} {status:<8} {t['description']}")


def main():
    print("TODO CLI — type 'exit' to quit.")
    while True:
        try:
            line = input("> ").strip()
        except EOFError:
            break
        if not line:
            continue

        parts = line.split()
        cmd = parts[0]
        args = parts[1:]

        tasks = load_tasks()

        if cmd == "exit":
            break
        elif cmd == "add":
            cmd_add(tasks, args)
        elif cmd == "done":
            cmd_done(tasks, args)
        elif cmd == "delete":
            cmd_delete(tasks, args)
        elif cmd == "list":
            cmd_list(tasks, args)
        else:
            print("Unknown command. Available: add, done, delete, list, exit")


if __name__ == "__main__":
    main()
