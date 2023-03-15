def todos_list(filepath="todos.txt"):
    """read a text file and return
    the to dos in a list
    """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos_arg, filepath="todos.txt"):
    """write the to-do item list in the txt file
    """
    with open(filepath , 'w') as file:
        file.writelines(todos_arg)
