import tkinter
import threading
from tkinter import messagebox
import sys

# ---------------- Global Variables ----------------
tasks = []  # list to store tasks -> [task_name, time_left]
timer = threading      # placeholder (not really needed)
real_timer = threading # placeholder (not really needed)
ok_thread = True       # flag to control background thread


# ---------------- Get Input from UI ----------------
def get_entry(event=""):
    text = todo.get()          # get task text
    hour = int(time.get())     # get time in seconds (convert to int)

    todo.delete(0, tkinter.END)   # clear task input
    time.delete(0, tkinter.END)   # clear time input

    todo.focus_set()  # set cursor back to input box

    add_list(text, hour)   # add task to list

    if 0 < hour < 999:     # basic validation
        update_list()      # refresh UI


# ---------------- Add Task ----------------
def add_list(text, hour):
    tasks.append([text, hour])   # store task

    # create timer thread → after 'hour' seconds, call time_passed
    timer = threading.Timer(hour, time_passed, [text])
    timer.start()


# ---------------- Update List UI ----------------
def update_list():
    if todolist.size() > 0:
        todolist.delete(0, "end")   # clear listbox

    for task in tasks:
        # display each task with remaining time
        todolist.insert(
            "end",
            "[" + task[0] + "] Time left: " + str(task[1]) + " seconds"
        )


# ---------------- Notification ----------------
def time_passed(task):
    # popup alert when timer completes
    tkinter.messagebox.showinfo("Notification", "Time for: " + task)


# ---------------- Background Timer ----------------
def real_time():
    if ok_thread:
        # run this function every 1 second
        real_timer = threading.Timer(1.0, real_time)
        real_timer.start()

    # update time for each task
    for task in tasks:
        if task[1] == 0:
            tasks.remove(task)   # remove completed task
        task[1] -= 1             # decrease time

    update_list()   # refresh UI


# ---------------- Main Application ----------------
if __name__ == '__main__':

    # create main window
    app = tkinter.Tk()
    app.geometry("440x600")
    app.title("Todolist Reminder")

    # ---------------- UI Components ----------------
    label = tkinter.Label(app, text="Enter work to do:",
                          wraplength=200,
                          justify=tkinter.LEFT)

    label_hour = tkinter.Label(app, text="Enter time (seconds)",
                               wraplength=200,
                               justify=tkinter.LEFT)

    todo = tkinter.Entry(app, width=30)   # task input
    time = tkinter.Entry(app, width=15)   # time input

    send = tkinter.Button(
        app,
        text='Add task',
        fg="#ffffff",
        bg='#6186AC',
        height=3,
        width=30,
        command=get_entry   # button click calls function
    )

    quit = tkinter.Button(
        app,
        text='Exit',
        fg="#ffffff",
        bg='#EB6464',
        height=3,
        width=30,
        command=app.destroy   # close app
    )

    todolist = tkinter.Listbox(app)   # list display

    # start background timer if tasks exist
    if tasks != "":
        real_time()


    # ---------------- Key Binding ----------------
    app.bind('<Return>', get_entry)   # press Enter to add task


    # ---------------- Layout ----------------
    label.place(x=0, y=10, width=200, height=25)
    label_hour.place(x=235, y=10, width=200, height=25)

    todo.place(x=62, y=30, width=200, height=25)
    time.place(x=275, y=30, width=50, height=25)

    send.place(x=62, y=60, width=50, height=25)
    quit.place(x=302, y=60, width=50, height=25)

    todolist.place(x=60, y=100, width=300, height=300)


    # ---------------- Run App ----------------
    app.mainloop()

    ok_thread = False   # stop background thread
    sys.exit("FINISHED")
