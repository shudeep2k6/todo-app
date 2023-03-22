import functions
import PySimpleGUI as sg

label = sg.Text("to-do list")
input_box = sg.InputText(tooltip="enter todo",key="todo")
add_button = sg.Button("add")
list_box = sg.Listbox(values=functions.todos_list(), key='todos',
                      enable_events=True,
                      size=[44,12])
edit_button = sg.Button("edit")

window = sg.Window("my to-do app",
                   layout=[[label],[input_box ,add_button],[list_box, edit_button]],
                   font=('Helvetica',14) )
while True:

    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "add":
            todos = functions.todos_list()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)

        case "edit":
            todo_edit = values['todos'][0]
            new_todo = values['todo']

            todos=functions.todos_list()
            index = todos.index(todo_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case sg.WIN_CLOSED:
            break


window.close()

