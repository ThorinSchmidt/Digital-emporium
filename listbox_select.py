import tkinter as tk
def on_select(event):
    # get the selected item
    selected_item = event.widget.get(tk.ACTIVE)
    print(selected_item)
# create the main window
root = tk.Tk()
# create a listbox widget
listbox = tk.Listbox(root, selectmode = tk.MULTIPLE)
listbox.pack()
# add some items to the listbox
listbox.insert(0, "Item 1")
listbox.insert(1, "Item 2")
listbox.insert(2, "Item 3")
# bind the click event to the listbox widget
listbox.bind("<<ListboxSelect>>", on_select)
# run the main loop
root.mainloop()
