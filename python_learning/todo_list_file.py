def task_write():
    task = input("Enter a task = ")
    task_priority = input("Enter task priority = ")
    
    with open("todo.txt", "a") as f:
        f.write(f"Task = {task} || Priority = {task_priority} \n")


def task_read():
    with open("todo.txt", "r") as f:
        task = f.read()
        print(task)


a = input("What to do ? 1 -> Write Todo | 2 -> Read Todo \n")

match a:
    case "1":
        task_write()
    case "2":
        task_read()
    case default :
        exit(0)