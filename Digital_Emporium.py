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
        
        # variables
        self.use_core_rules = True
        self.use_custom = False
        self.box_element = font.Font(family="Courier")
        self.selection_list = []
        self.master_list = []
        self.master_dict = {}
        self.purchases = []
        self.flags = ""
        

        
        self.create_widgets()
        self.update_master_list()
        self.update_flags() # includes call to update selection list
        
    def create_widgets(self):
        '''create the data structures and GUI elements'''
        # GUI elements
        # create description label
        Label(self,
                text = "Categories to Display:"
                ).grid(row = 0, column = 0, sticky = W)

        # create General check button
        self.display_general = BooleanVar()
        self.display_general.set(True)
        Checkbutton(self,
                    text = "General",
                    variable = self.display_general,
                    command = self.update_flags
                    ).grid(row = 2, column = 0, sticky = W)
        
        # create Weapons check button
        self.display_weapons = BooleanVar()
        self.display_weapons.set(True)
        Checkbutton(self,
                    text = "Weapons",
                    variable = self.display_weapons,
                    command = self.update_flags
                    ).grid(row = 2, column = 1, sticky = W)

        # create Armor check button
        self.display_armor = BooleanVar()
        self.display_armor.set(True)
        Checkbutton(self,
                    text = "Armor",
                    variable = self.display_armor,
                    command = self.update_flags
                    ).grid(row = 2, column = 2, sticky = W)

        # create Beasts check button
        self.display_beasts = BooleanVar()
        self.display_beasts.set(True)
        Checkbutton(self,
                    text = "Beasts",
                    variable = self.display_beasts,
                    command = self.update_flags
                    ).grid(row = 3, column = 0, sticky = W)

        # create Vehicles check button
        self.display_vehicles = BooleanVar()
        self.display_vehicles.set(True)
        Checkbutton(self,
                    text = "Vehicles",
                    variable = self.display_vehicles,
                    command = self.update_flags
                    ).grid(row = 3, column = 1, sticky = W)

        self.selection_lbx = Listbox(self,
                                     selectmode = "multiple",
                                     width = 46,
                                     height = 15,
                                     font = self.box_element)
        self.selection_lbx.grid(row = 4, column = 0,
                                columnspan = 3, sticky = W)

        self.description_txt = Text(self,
                                    width = 46,
                                    height = 6,
                                    font = self.box_element,
                                    wrap = WORD)
        self.description_txt.grid(row = 5,
                                  column = 0,
                                  columnspan = 3,
                                  pady = 10,
                                  sticky = W)

    def update_flags(self):
        """ rewrite the flag string """
        self.flags = ""
        
        if self.display_general.get():
            self.flags += "G"
        
        if self.display_weapons.get():
            self.flags += "W"
        
        if self.display_armor.get():
            self.flags += "A"
        
        if self.display_beasts.get():
            self.flags += "B"
            
        if self.display_vehicles.get():
            self.flags += "V"
        
        #print(self.flags)
        self.update_selection_list()
        

    def update_selection_list(self):
        ''' update the listbox. also make headings appear in "negative"
            and cause entries to have alternating backgrounds between
            yellow and blue '''
        self.selection_lbx.delete(0, END)
        itemcount = 0
        for entry in self.master_list:
            if entry[1] in self.flags:
                self.selection_lbx.insert(END, entry[0])
                if entry[2] < 0:
                    self.selection_lbx.itemconfig(END, bg = 'black',
                                                  fg='white')
                    linecount = 0
                else:
                    if linecount % 2 -- 0:
                        self.selection_lbx.itemconfig(END, bg = 'yellow')
                    else:
                        self.selection_lbx.itemconfig(END, bg = 'cyan')
                    linecount += 1
                    
        #for entry in self.selection_list:
        #    print(entry)
    
    def update_master_list(self):
        '''set up the master item list'''
        self.master_list = []
        self.master_dict = {}
        
        text_file = open("corea.txt", "r")

        for line in text_file:
            entry = line.split('|')
            # strip whitespace, convert cost and weight to float
            entry[0] = entry[0].rstrip()
            entry[1] = entry[1].strip()
            entry[2] = float(entry[2])
            entry[3] = float(entry[3])

            self.master_list.append(entry)
            if entry[2] >= 0:
                key = entry[0]
                value = entry[-1].strip()
                self.master_dict[key] = [value]
     
        text_file.close()

        for key in self.master_dict.keys():
            print(key, self.master_dict[key])

# Main
root = Tk()
root.title("Digital Emporium")
root.geometry("1000x500")
root.protocol("WM_DELETE_WINDOW", root.destroy)

app = Application(root)

root.mainloop()
print('Done.')

