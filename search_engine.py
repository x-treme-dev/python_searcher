import os
import time
from tkinter import *
import tkinter as tk
from tkinter import font
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from tkinter.messagebox import showerror, showwarning, showinfo

 
path = ''
file = 'file'
folder = 'folder'

# ! not use name 'root' in cicles for searching directory or files

#closing app manually
def finish():
    global root
    root.destroy()  
    print("Closing app")
 

def test_params():
    global path
    if not (test_name(path) and test_name(name.get()) ):
       showerror(title="Error", message="Path or name is empty")
    else:
        start_program()
       
def start_program():
    global out_button, root
    message_label.config(text='Searching...', foreground="blue")
    root.update()
    flag = False
    if name_radio_btn() == 'folder':
       clean_textfield()
       for current_dir, dirs, files in os.walk(path):
            for dir in dirs:
                print (f'I`m looking for a folder by name `{name.get()}`')
                if test_name(name.get()) and dir.lower().strip().startswith(name.get().lower().strip()):
                    results_text.insert(tk.INSERT, os.path.join(current_dir,dir) + "\n")
                    results_cmd.insert(tk.INSERT, results_text.get("1.0", END).replace("/", "\\") )
                    flag = True
                    
    elif name_radio_btn() == 'file':
         clean_textfield()
         for current_dir, dirs, files in os.walk(path):
            for file in files:
                print (f'I`m looking for a file by name `{name.get()}`')
                if test_name(name.get()) and file.lower().startswith(name.get().lower()):
                    results_text.insert(tk.INSERT, os.path.join(current_dir,file) + "\n")
                    results_cmd.insert(tk.INSERT, results_text.get("1.0", END).replace("/", "\\") )
                    flag = True 
    out_message(flag, name_radio_btn())
    
def get_directory():
    root = tk.Tk()   
    root.withdraw()   

    global path
    path = filedialog.askdirectory()

    if path:
        out_label.config(text=path, foreground="#008000")
    else:
        out_label.config(text="Choose a path!", foreground="#FF0000")
        showinfo(title="Path to Directory or Disk", message="Selection canceled")

def test_name(name):
      if len(name) == 0:
         return False
      else:
         return True

def name_radio_btn():
     return selected_value.get()
    
def out_message(flag, item):
     if flag==True:
          message_label.config(text= 'For copy: Ctrl+C - English keyborard layout!', foreground="#008000")
     else:
          message_label.config(text=item.capitalize() + ' is not found!', foreground="#FF0000") 

def clean_textfield():
     global results_text
     results_text.delete("1.0", END) 

            



root = tk.Tk()
root.title("search_engine")
root.geometry("560x800")
root.maxsize(600, 800)
root.update_idletasks() 

Font = font.Font(family= "Courier New", size=16, weight="normal", slant="roman")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
 

#first row
ttk.Label(mainframe, text="Where to search?", font=Font).grid(row=1, column=1, sticky=W)
tk.Button(mainframe, text='Directory or Disk', font=Font, command=get_directory).grid(row=1, column=2, sticky=N)
#second row
out_label = ttk.Label(mainframe, text="Chosen path", font=Font)
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
message_label = ttk.Label(mainframe, text="", font=Font)
message_label.grid(row=5, column=1, columnspan=2, sticky=W)
#sexth row
results_text = tk.Text(mainframe, width=35, height=10, wrap="word", font=Font)
results_text.grid(row=6, column=1, columnspan=2, pady=20, sticky="n")

results_cmd = tk.Text(mainframe, width=35, height=10, wrap="word",font=Font)
results_cmd.grid(row=7, column=1, columnspan=2, pady=20, sticky="n")
#seventh row
out_button = tk.Button(mainframe, text='To output all results', font=Font, command=test_params)
out_button.grid(row=8, column=1, columnspan=2, sticky=N)
 

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.protocol("WM_DELETE_WINDOW", finish)
name_entry.focus()
 
root.mainloop()
