import os
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
 
 

path = ''
file = 'file'
folder = 'folder'
 
#C:\\Users\Admin\python
def find_file(*args):
 for root, dirs, files in os.walk(path):
    for file in files:
        if test_name(name.get()) and file.lower().startswith(name.get().lower()):
           #print(os.path.join(root, file))
              message_text.insert(tk.INSERT, os.path.join(root,file) + "\n")
        

def find_folder(*args):
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            if test_name(name.get()) and dir.lower().startswith(name.get().lower()):
                #print(os.path.join(root, dir))
                message_text.insert(tk.INSERT, os.path.join(root,dir) + "\n")
            
def test_name(name):
      if (name == '' or len(name) < 2):
         return False
      else:
         print(name, len(name))
         return True
            
#closing app manually
def finish():
    root.destroy()  
    print("Closing app")

#to get directory path
def get_directory():
    root = tk.Tk()   
    root.withdraw()   

    global path
    path = filedialog.askdirectory()

    if path:
        #print(f"Выбранный путь: {path}")
        out_label.config(text=path)
    else:
        #print(f"Выбор отменен")
        out_label.config(text="Выбор отменен")


#to create root
root = Tk()
root.title("find file by name")
root.geometry("350x300+500+200")
root.update_idletasks() 

#to create mainframe
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
 

#first row
ttk.Label(mainframe, text="Where to search?").grid(column=1, row=1, sticky=W)
ttk.Button(mainframe, text='Directory or Disk', command=get_directory).grid(column=2, row=1, sticky=N)
#second row
ttk.Label(mainframe, text="Choosen path").grid(column=1, row=2, sticky=W)
out_label = ttk.Label(mainframe, text="...wating")
out_label.grid(column=2, row=2, sticky=N)
#third row
ttk.Label(mainframe, text="To search").grid(column=1, row=3, sticky=W)
option_default = StringVar(value=folder) 
folder_btn = ttk.Radiobutton(mainframe, text=folder, value=folder, variable=option_default, command=find_folder).grid(column=2, row=3, sticky=W)
file_btn = ttk.Radiobutton(mainframe, text=file, value=file, variable=option_default, command=find_file).grid(column=2, row=3, sticky=E)
#four row
ttk.Label(mainframe, text="Enter name").grid(column=1, row=4, sticky=W)
name = StringVar()
name_entry = ttk.Entry(mainframe, width=20, textvariable=name)
name_entry.grid(column=2, row=4, sticky=(W, E))
#fifth row
ttk.Label(mainframe, text="Message").grid(column=1, row=5, sticky=W) 
message_text = tk.Text(mainframe, width=18, height=10, wrap="word")
message_text.grid(row=5, column=2,   sticky="n")
 


for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.protocol("WM_DELETE_WINDOW", finish)
name_entry.focus()
root.bind("<Return>", find_folder)

root.mainloop()

