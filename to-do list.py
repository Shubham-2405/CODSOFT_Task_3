# Task 3 : To - Do List

# importing libraries
from tkinter import *
from tkinter import messagebox

# function to enter task
def entertask():
    input_text=""
    def add():
        input_text=entry_task.get(1.0, "end-1c")
        if input_text=="":
            messagebox.showwarning(title="Warning!",message="Please Enter some Text")
        else:
            listbox.insert(END,input_text)
            win2.destroy()

# creating main window
    win2=Tk()
    win2.title("Add task")
    win2.resizable(width=0, height=0)
    entry_task=Text(win2,width=30,height=5, font=("Arial", 20))
    entry_task.pack()
    button_temp=Button(win2,text="Add task",font=("calisto mt", 15),command=add)
    button_temp.pack()
    win2.mainloop()

# creating mark as completed function    
def mark():
    marked=listbox.curselection()
    temp=marked[0]
    temp_marked=listbox.get(marked)
    #update it 
    temp_marked=temp_marked+" ✔"
    listbox.delete(temp)
    listbox.insert(temp,temp_marked)

# create delete task function
def delete():
    selected=listbox.curselection()
    listbox.delete(selected[0])

# creating labels and buttons
mainwin = Tk()
mainwin.geometry("800x500")
mainwin.resizable(width=0, height=0)
mainwin.title("To - Do List")
mainwin.iconbitmap("clipboard_120835.ico")

fr1 = Frame(mainwin, width=800, height = 120, bg = 	'#2F4F4F')
fr1.place(x = 0,y = 0)

fr2 = Frame(mainwin, width=800, height = 380, bg = 	'#53868B')
fr2.place(x = 0,y = 120)


lb1 = Label(text='To - Do List', font=("Footlight MT Light", 45, 'bold', 'underline'), justify="center", bg='#2F4F4F',fg = 'white' )
lb1.place(x = 250, y=30)


listbox=Listbox(fr2,bg="#8EE5EE",fg="black",height=14,width=48,font = "Helvetica",)  
listbox.place(x = 23, y = 20)

scroll_list=Scrollbar(fr2,relief='flat',bg="#8EE5EE",background="#8EE5EE")
scroll_list.place(x=537, y=20, relheight=0.89)
listbox.config(yscrollcommand=scroll_list.set)
scroll_list.config(command=listbox.yview)

btn1 = Button(fr2, text="Add New Task", font= ("Calisto MT", 15), justify='center', relief='ridge', width = 15, command=entertask)
btn1.place(x = 580, y = 80)

btn2 = Button(fr2, text="Delete Task", font= ("Calisto MT", 15), justify='center', relief='ridge', width = 15, command=delete)
btn2.place(x = 580, y=160)

btn3 = Button(fr2, text="Mark As Completed", font= ("Calisto MT", 15), justify='center', relief='ridge', command=mark)
btn3.place(x=580, y=240)

mainwin.mainloop()