# Python program demonstrating
# Multiple selection in Listbox widget


from tkinter import *
from tkinter import font
import sys

window = Tk()
window.geometry('1000x500')
window.protocol("WM_DELETE_WINDOW", window.destroy)

# Choosing selectmode as multiple
# for selecting multiple options
box_element = font.Font(family="Courier")
list = Listbox(window, selectmode = "multiple", font = box_element)

# Widget expands horizontally and
# vertically by assigning both to
# fill option
list.pack(expand = YES, fill = "both")

# Taking a list 'x' with the items
# as languages
def fill_list():
    '''open the files and put the contents into a list of lists'''
    local_list = []
    text_file = open("core.txt", "r")

    for line in text_file:
        entry = line.split('|')
        # strip whitespace, convert cost and weight to float
        entry[0] = entry[0].strip()
        entry[1] = entry[1].strip()
        entry[2] = float(entry[2])
        entry[3] = float(entry[3])

        local_list.append(entry)
 
    text_file.close()
    
    return local_list

inventory = fill_list()

for each_item in range(len(inventory)):
	
	list.insert(END, inventory[each_item][0])
	
	# coloring alternative lines of listbox
	list.itemconfig(each_item,
			bg = "lightgray" if each_item % 2 == 0 else "cyan")
	
window.mainloop()
print('done.')