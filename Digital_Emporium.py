# Digital Emporium
# Thorin Schmidt
# 09/25/2023

'''
    A utility program that allows the user to select items for "purchase" from 
    the equipent listed in the rulebooks. (Core Rules to start, incorporation
    of Equipment Emporium next, then we'll see.) 
    
    Project Links:
        Github: github.com/ThorinSchmidt/Digital-emporium
        Trello: trello.com/invite/b/c78AwgXw/ATTI4eb261e4a1d1e2ac82ae916
                    f791563bb24D74547/digital-emporium
        Colab:  colab.research.google.com/drive/1zpEPA3qeGzOTXTcgkoXFpsCN
                    pUypDST9?usp=sharing
'''
from tkinter import *
from tkinter import font
import sys

class Application(Frame):
    '''definition of the primary frame'''
    
    def __init__(self, master):
        """ Initialize the Frame. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        '''create the data structures and GUI elements'''
        # variables
        self.use_core_rules = True
        self.use_custom = False
        self.box_element = font.Font(family="Courier")
        self.data_list = self.fill_master()
        self.purchases = []        
        
        # GUI elements
        self.selection_lbx = Listbox(self, selectmode = "multiple", width = 46,
                                height = 20, font = self.box_element)
        self.selection_lbx.grid()
        
        # populate the listbox
        for item in range(len(self.data_list)):
            self.selection_lbx.insert(END, self.data_list[item][0])
	
            # coloring alternative lines of listbox
            self.selection_lbx.itemconfig(item,
                    bg = "yellow" if item % 2 == 0 else "cyan")
                
    def fill_master(self):
        '''set up the master item list'''
        local_list = []
        text_file = open("core.txt", "r")

        for line in text_file:
            entry = line.split('|')
            # strip whitespace, convert cost and weight to float
            entry[0] = entry[0].rstrip()
            entry[1] = entry[1].strip()
            entry[2] = float(entry[2])
            entry[3] = float(entry[3])

            local_list.append(entry)
     
        text_file.close()
        
        return local_list


# Main

root = Tk()
root.title("Digital Emporium")
root.geometry("1000x400")
root.protocol("WM_DELETE_WINDOW", root.destroy)

app = Application(root)

root.mainloop()
print('Done.')

