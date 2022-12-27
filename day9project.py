import tkinter
import threading
from tkinter import messagebox
import sys

tasks = [] # list of tasks
timer = threading # create a new thread for the real time 
real_timer = threading # create a new thread for the real time
ok_thread = True # boolean to stop the thread


def get_entry(event=""):
    text = todo.get() # get the text from the entry
    hour = int(time.get()) # get the time

    todo.delete(0, tkinter.END) # delete the text in the entry
    time.delete(0, tkinter.END) # delete the text in the entry
    
    todo.focus_set() # set the focus on the entry
    add_list(text, hour) # add the task to the list
    if 0 < hour < 999: # if the time is between 0 and 999
        update_list() # update the list


def add_list(text, hour): # add a task to the list
    tasks.append([text, hour]) # add the task to the list
    timer = threading.Timer(hour, time_passed, [text]) # create a new thread
    timer.start()
 

def update_list():
    if todolist.size() > 0: # if todolist is not empty
        todolist.delete(0, "end") # delete all the items
    for task in tasks: # for each task in tasks
        todolist.insert("end", "[" + task[0] + "] Time left: " + str(task[1]) + " secondes") 
        #add the task to the list


def time_passed(task):
    tkinter.messagebox.showinfo("Notification", "Time for : " + task) # show a message box


def real_time():
    if ok_thread: # if ok_thread is True
        real_timer = threading.Timer(1.0, real_time) # create a new thread 
        real_timer.start() # start the thread
    for task in tasks: # for each task in tasks
        if task[1] == 0: # if the time is 0
            tasks.remove(task) # remove the task
        task[1] -= 1 # decrement the time
    update_list() # update the list


if __name__ == '__main__': # if the file is executed directly (not imported)
    # application
    app = tkinter.Tk() # create a new window
    app.geometry("440x600") # set the size of the window
    app.title("Todolist Remainder") # set the title of the window

    # widgets
    label = tkinter.Label(app, text="Enter work to do:",
                          wraplength = 200,
                          justify = tkinter.LEFT) # create a label
    label_hour = tkinter.Label(app, text="Enter time (secondes)", 
                               wraplength = 200,
                               justify = tkinter.LEFT) # create a label 
    todo = tkinter.Entry(app, width=30) # create an entry
    time = tkinter.Entry(app, width=15) # create an entry 
    send = tkinter.Button(app, text='Add task', fg="#ffffff", bg='#6186AC', height=3, width=30, command=get_entry) # create a button
    quit = tkinter.Button(app, text='Exit', fg="#ffffff", bg='#EB6464', height=3, width=30, command=app.destroy)
    todolist = tkinter.Listbox(app) # create a listbox
    if tasks != "": # if tasks is not empty
        real_time() # start the thread

    # binding
    app.bind('<Return>', get_entry) # bind the return key to the function get_entry 
    
    # widgets placement
    label.place(x=0, y=10, width=200, height=25) # place the label
    label_hour.place(x=235, y=10, width=200, height=25) 
    todo.place(x=62, y=30, width=200, height=25) # place the entry 
    time.place(x=275, y=30, width=50, height=25)
    send.place(x=62, y=60, width=50, height=25)
    quit.place(x=302, y=60, width=50, height=25)
    todolist.place(x=60, y = 100, width=300, height=300)

    app.mainloop() # start the mainloop
    ok_thread = False # stop the thread
    sys.exit("FINISHED") # exit the application