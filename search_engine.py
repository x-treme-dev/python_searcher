import os
import tkinter as tk
import time
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

 
 

path = ''
file = 'file'
folder = 'folder'

def name_radio_btn():
     return selected_value.get()

def on_radio_btn():
    flag = False
    if name_radio_btn() == 'folder':
       for root, dirs, files in os.walk(path):
            for dir in dirs:
                if test_name(name.get()) and dir.lower().startswith(name.get().lower()):
                    results_text.insert(tk.INSERT, os.path.join(root,dir) + "\n")
                    flag = True
                    
    elif name_radio_btn() == 'file':
         for root, dirs, files in os.walk(path):
            for file in files:
                if test_name(name.get()) and file.lower().startswith(name.get().lower()):
                    results_text.insert(tk.INSERT, os.path.join(root,file) + "\n")
                    flag = True 
    out_message(flag, name_radio_btn())                
                    
def out_message(flag, item):
     print(f"in out_message: {flag} {item}")
     if flag==True:
          message_label.config(text=item.capitalize() +' is found!', foreground="#008000")
     else:
          message_label.config(text=item.capitalize() + ' is not found!', foreground="#FF0000") 

            
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
        out_label.config(text=path, foreground="#008000")
    else:
        #print(f"Выбор отменен")
        out_label.config(text="Выбор отменен", foreground="#FF0000")


#to create root
root = Tk()
root.title("find file by name")
root.geometry("530x550+400+50")
root.maxsize(700, 600)
root.update_idletasks() 

Font = font.Font(family= "Courier New", size=16, weight="normal", slant="roman")
#to create mainframe
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
 

#first row
ttk.Label(mainframe, text="Where to search?", font=Font).grid(row=1, column=1, sticky=W)
tk.Button(mainframe, text='Directory or Disk', font=Font, command=get_directory).grid(row=1, column=2, sticky=N)
#second row
out_label = ttk.Label(mainframe, text="Choosen path", font=Font)
out_label.grid(row=2, column=1, columnspan=3, sticky=W)
#third row
tk.Label(mainframe, text="Folder or file?", font=Font).grid(row=3, column=1, sticky=W)
selected_value = StringVar(value=folder) 
tk.Radiobutton(mainframe, text=folder, value=folder, font=Font, variable=selected_value ).grid(row=3, column=2, sticky=W)
tk.Radiobutton(mainframe, text=file, value=file, font=Font, variable=selected_value).grid(row=3, column=2, sticky=E)
#four row
ttk.Label(mainframe, text="Enter name", font=Font).grid(row=4, column=1, sticky=W)
name = StringVar()
name_entry = ttk.Entry(mainframe, width=20, font=Font, textvariable=name)
name_entry.grid(row=4, column=2, sticky=(W, E))
#fifth row
message_label = ttk.Label(mainframe, text="Results:", font=Font)
message_label.grid(row=5, column=1, columnspan=2, sticky=W)
#sexth row
results_text = tk.Text(mainframe, width=35, height=10, wrap="word", font=Font)
results_text.grid(row=6, column=1, columnspan=2, pady=20, sticky="n")
#seventh row
tk.Button(mainframe, text='To output all results', font=Font, command=on_radio_btn).grid(row=7, column=1, columnspan=2, sticky=N)
 

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.protocol("WM_DELETE_WINDOW", finish)
name_entry.focus()
#root.bind("<Return>", find_folder)

root.mainloop()

