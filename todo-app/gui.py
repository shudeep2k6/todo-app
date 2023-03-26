import functions
import PySimpleGUI as sg
import time


clock1 = sg.Text('',key='clock')
label = sg.Text("to-do list")
input_box = sg.InputText(tooltip="enter todo",key="todo")
add_button = sg.Button("add")
list_box = sg.Listbox(values=functions.todos_list(), key='todos',
                       enable_events=True,size=[44,12])
edit_button = sg.Button("edit")
complete_button=sg.Button("complete")
exit_button=sg.Button("exit")

window = sg.Window("my to-do app",
                   layout=[[clock1],
                           [label],
                           [input_box ,add_button],
                           [list_box, edit_button,complete_button],
                           [exit_button]],
                   font=('Helvetica',14) )
while True:

    event, values = window.read()
    window("clock").update(value=time.strftime("%b %d,%y %H:%M:%S"))
    print(event)
    print(values)
    match event:
        case "add":
            todos = functions.todos_list()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos=functions.todos_list()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("please select any item")

        case "complete":
            try:
                todo_to_complete= values['todos'][0]
                todos = functions.todos_list()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)

            except IndexError:
                sg.popup("please select any item")

        case "exit":
            break


        case sg.WIN_CLOSED:
            break


window.close()

