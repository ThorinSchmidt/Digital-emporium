#listbox of lists
import tkinter as tk

def populateListbox(lstt):
    listbox.insert("end", *lst)

root = tk.Tk()
listbox = tk.Listbox(root)
listbox.pack()
lst = ["1 one", "2  two", "3   three", "4    four"]
btn = tk.Button(root, text="Populate listbox", command = lambda: populateListbox(lst))
btn.pack()

root.mainloop()
