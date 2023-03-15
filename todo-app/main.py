from functions import todos_list, write_todos

while True:
    user_input = input("ENTER add ,edit,show,complete or exit:")


    if user_input.startswith('add'):
        todo = user_input[4:]

        todos = todos_list()

        todos.append(todo + '\n')
        write_todos( todos )



    elif user_input.startswith('show'):

        todos = todos_list()

        for index,item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_input.startswith("edit"):

        number = int(input("enter the value of the todo: "))
        number = number - 1

        todos = todos_list()

        new_todo = input("enter the new todo :")
        todos[number]= new_todo + "\n"

        write_todos(todos)

    elif user_input.startswith("complete"):

        number = int(input("number of todo completed: "))
        todos.pop(number - 1)
    elif user_input.startswith("exit"):
        break
