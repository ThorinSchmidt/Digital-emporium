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
        self.master_dict = {}
        self.purchase_list = []
        self.flags = ""
        
        self.create_widgets()
        self.update_master_dict()
        self.update_flags() # includes call to update selection list

    def get_element(self, event):
        '''retrieve index of selected element'''
        self.description_txt.delete(0.0, END)
        selection = event.widget.curselection()
        index = selection[0]
        key = event.widget.get(index)
        if self.master_dict[key][4] > -1:
            text = self.master_dict[key][-1]
            self.description_txt.insert(0.0, text)
            #print(text)

        


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
                                     selectmode = SINGLE,
                                     width = 47,
                                     height = 15,
                                     font = self.box_element)
        self.selection_lbx.grid(row = 4,
                                rowspan = 2,
                                column = 0,
                                columnspan = 3,
                                sticky = W)
        self.selection_lbx.bind('<<ListboxSelect>>', self.get_element)

        self.cart_in_btn = Button(self,
                                  font = self.box_element,
                                  width = 13,
                                  command = self.purchase_item,
                                  text = "Cart In  (->)")
        self.cart_in_btn.grid(row = 4,
                              column = 3,
                              sticky = S)
        
        self.cart_out_btn = Button(self,
                                   font = self.box_element,
                                   width = 13,
                                   command = self.return_item,
                                   text = "Cart Out (<-)")
        self.cart_out_btn.grid(row = 5,
                               column = 3,
                               sticky = N)

        self.empty_cart_btn = Button(self,
                                     font = self.box_element,
                                     width = 13,
                                     command = self.empty_cart,
                                     text = "Empty Cart")
        self.empty_cart_btn.grid(row = 5,
                                 column = 3,
                                 sticky = S)
        
        self.basket_lbl = Label(self,
                                width = 47,
                                font =self.box_element,
                                anchor = W,
                                text = "Purchases")
        self.basket_lbl.grid(row = 2,
                             column = 4,
                             sticky = W)

        self.basket_txt = Listbox(self,                                  selectmode = SINGLE,
                                  width = 47,
                                  height = 15,
                                  font = self.box_element)
        self.basket_txt.grid(row = 4,
                             rowspan = 2,
                             column = 4,
                             sticky = W)
        
        self.description_txt = Text(self,
                                    width = 47,
                                    height = 6,
                                    font = self.box_element,
                                    wrap = WORD)
        self.description_txt.grid(row = 6,
                                  column = 0,
                                  columnspan = 3,
                                  pady = 10,
                                  sticky = W)
        
    def purchase_item(self):
        '''move selected item to the "basket"'''
        key = self.selection_lbx.get(ACTIVE)
        value = self.master_dict.get(key)
        if value[4] > -1:
            item = value[0]+"\n"
            self.purchase_dict.append(item)
            print(self.purchase_list)



        

    def return_item(self):
        '''remove selected item from the "basket"'''
        pass

    def empty_cart(self):
        '''remove selected item from the "basket"'''
        self.purchases.set(value = [])
    
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
        for key in self.master_dict.keys():
            value = self.master_dict[key]
            #print(value)
            if value[3] in self.flags:
                itemcount += 1
                self.selection_lbx.insert(END, key)
                if value[4] < 0:
                    self.selection_lbx.itemconfig(END, bg = 'black',
                                                  fg='white')
                    linecount = 0
                else:
                    if linecount % 2 -- 0:
                        self.selection_lbx.itemconfig(END, bg = 'yellow')
                    else:
                        self.selection_lbx.itemconfig(END, bg = 'cyan')
                    linecount += 1
                    
        self.selection_lbx.focus_set()
        self.selection_lbx.activate(0)
        #print(self.selection_lbx.get(ACTIVE))
        #for entry in self.selection_list:
        #    print(entry)
    
    def update_master_dict(self):
        '''set up the master item list'''
        self.master_dict = {}
        
        text_file = open("corea.txt", "r")

        for line in text_file:
            entry = line.split('|')
            # strip whitespace, convertcost and weight to float
            entry[3] = entry[3].strip()
            entry[4] = float(entry[4])
            entry[5] = float(entry[5])
            entry[6] = entry[6].strip()

            key = entry[0]+entry[1]+entry[2]
            #print(key)
            value = entry
            self.master_dict[key] = value
 
        text_file.close()

        #for key in self.master_dict.keys():
        #    print(key, self.master_dict[key])


# Main
root = Tk()
root.title("Digital Emporium")
root.geometry("1100x500")
root.protocol("WM_DELETE_WINDOW", root.destroy)

app = Application(root)

root.mainloop()
print('Done.')

