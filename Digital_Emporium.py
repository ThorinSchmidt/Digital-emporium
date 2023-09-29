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
        self.master = self.fill_master()
        self.purchases = {}
        self.use_core_rules = True
        self.use_custom = False
        
        
        # GUI elements
        self.main_list = Listbox(self, selectmode = "multiple")
        self.main_list.grid()
        
    def fill_master(self):
        '''set up the master item list'''
        temp = { 1 : "bunch of stuff"}
        
        return temp



# Main

root = Tk()
root.title("Digital Emporium")
root.geometry("600x400")

app = Application(root)

root.mainloop()

