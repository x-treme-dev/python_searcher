import os
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog

path = ''
 
#C:\\Users\Admin\python
def search(*args):
 for root, dirs, files in os.walk(path):
    for file in files:
        if file.lower().startswith(name.get().lower()):
          print(os.path.join(root, file))

def find_dir(*args):
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            if (name.get() != '' and len(name.get()) > 1) and dir.lower().startswith(name.get().lower()):
                print(os.path.join(root, dir))
                 

    return None  # Папка не найдена

#closing app manually
def finish():
    root.destroy()  
    print("Closing app")

#to get directory path
def get_directory():
    root = tk.Tk()  # Создаем главный Tkinter окно (необходимо, если диалоговое окно не вызывается из существующего окна)
    root.withdraw()  # Скрываем окно (не нужно, если вы вызовете диалоговое окно из существующего окна)

    global path
    path = filedialog.askdirectory()

    if path:
        # Здесь обработка выбранного пути
        print(f"Выбранный путь: {path}")
        # Можно, например, записать путь в текстовое поле
        out_label.config(text=path)
    else:
        print("Выбор отменен")


#to create root
root = Tk()
root.title("find file by name")
root.geometry("300x250+500+200")
root.update_idletasks() 

#to create mainframe
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
 


#add label to mainframe
ttk.Label(mainframe, text="Select directory").grid(column=1, row=1, sticky=W)
#add buttont to mainframe
ttk.Button(mainframe, text='Directory', command=get_directory).grid(column=2, row=1, sticky=W)
ttk.Label(mainframe, text="Choosen path").grid(column=1, row=2, sticky=W)
out_label = ttk.Label(mainframe, text="...")
out_label.grid(column=2, row=2, sticky=W)
ttk.Label(mainframe, text="Enter file name").grid(column=1, row=3, sticky=W)
#input field for file name
name = StringVar()
name_entry = ttk.Entry(mainframe, width=20, textvariable=name)
name_entry.grid(column=2, row=3, sticky=(W, E))




for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.protocol("WM_DELETE_WINDOW", finish)
name_entry.focus()
root.bind("<Return>", find_dir)

root.mainloop()

