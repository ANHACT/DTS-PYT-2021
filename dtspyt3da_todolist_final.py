#Simple ToDo List GUI App
#By Group: DTS-PYT-3D-A (Ardhian Hatmadji [0970356111-103], Nia Febrianti [0970356150-20])
#Python: 3.8.10/3.9.6

#=== Import Modules ===#
from tkinter import *
from tkinter import messagebox
import pickle


#=== Create ToDo List Functions ===#

#newToDo() function
def newToDo():
    todo = todo_entry.get()
    if todo != "":
        lb_todos.insert(END, todo)
        todo_entry.delete(0, "end")
    else:
        messagebox.showwarning("Warning!", "Please enter some ToDo task.")

#deleteToDo() function
def deleteToDo():
    try:
        todo_index = lb_todos.curselection()[0]
        lb_todos.delete(todo_index) #lb_todos.delete(ANCHOR)
    except:
        messagebox.showwarning("Warning!", "You must select a ToDo task.")
        
#loadToDo() function
def loadToDo():
    try:
        todos = pickle.load(open("todos.dat","rb"))
        lb_todos.delete(0, END)
        for todo in todos:
            lb_todos.insert(END, todo)
    except:
        messagebox.showwarning("Warning!", "Cannot find todos.dat")

#saveToDo() function
def saveToDo():
    todos = lb_todos.get(0,lb_todos.size())
    pickle.dump(todos,open("todos.dat","wb"))


#=== Create & Configure (Root) Window(ws for "windows") ===#
    
ws = Tk() 
ws.geometry('550x500+250+50') #'500x450+250+50'
ws.title('DTS-PYT-3D-A ToDo List')
ws.config(bg='#D27D2D')
ws.resizable(width=False, height=False)


#=== Add/Create Widgets ===#

#Add a Label
label_todos = Label(ws,text="Hi folks, tell me what are you going To Do today?",font=('Playfair Display',12),bg='#D27D2D')
label_todos.pack(pady=20)

#Create a Frame
frame_todos = Frame(ws)
frame_todos.pack(pady=10)

#Add Listbox (lb_todos for "listbox")
lb_todos = Listbox(frame_todos,width=25,height=8,font=('Alegreya',12),bd=0,fg='#CD7F52',
             highlightthickness=0,selectbackground='#CC5500',activestyle="none")
lb_todos.pack(side=LEFT, fill=BOTH)

#Add dummy/initial data
todo_list = ['Go for walk in the park','Go to the bookstore','Read the new magazine','Listening Music','Take a photoshoot',
             'Go to the market','Learning Python','Make a Python Project','Meeting with a friend','Eat a big portion of pizza']

for item in todo_list:
    lb_todos.insert(END, item)

#Add Scrollbars (sb_todos for "scrollbar")
sb_todos = Scrollbar(frame_todos)
sb_todos.pack(side=RIGHT, fill=BOTH)

lb_todos.config(yscrollcommand=sb_todos.set)
sb_todos.config(command=lb_todos.yview)

#Add Entry Box
todo_entry = Entry(ws,font=('Alternate Gothic',12))
todo_entry.pack(pady=20)

#Add another Frame for Buttons
button_frame_top = Frame(ws)
button_frame_top.pack(pady=20)

button_frame_bottom = Frame(ws)
button_frame_bottom.pack(pady=20)

#Add Buttons
addToDo_btn = Button(button_frame_top,text='Add ToDo',font=('Arvo',12),bg='#E97451',
                     padx=20,pady=10,width=12,command=newToDo)
addToDo_btn.pack(fill=BOTH, expand=True, side=LEFT)

delToDo_btn = Button(button_frame_top,text='Delete ToDo',font=('Merriweather',12),bg='#FAC898',
                     padx=20,pady=10,width=12,command=deleteToDo)
delToDo_btn.pack(fill=BOTH, expand=True, side=LEFT)

loaToDo_btn = Button(button_frame_bottom,text='Load ToDo',font=('Open Sans',12),bg='#FAC898',
                     padx=20,pady=10,width=12,command=loadToDo)
loaToDo_btn.pack(fill=BOTH, expand=True, side=LEFT)

savToDo_btn = Button(button_frame_bottom,text='Save ToDo',font=('Oswald & Abel',12),bg='#E97451',
                     padx=20,pady=10,width=12,command=saveToDo)
savToDo_btn.pack(fill=BOTH, expand=True, side=LEFT)


ws.mainloop()


