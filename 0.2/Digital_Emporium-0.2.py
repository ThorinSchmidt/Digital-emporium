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
import tkinter as tk
import tkinter.font as tkf
import tkinter.ttk as ttk

class ListStyle(ttk.Style):
    '''defines the style for the treeviews in the application'''
    def __init__(self, master):
        super(ListStyle, self).__init__(master)

        # Pick A Theme
        self.theme_use('default')

        # Configure the Treeview Colors
        self.configure("Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=25,
                fieldbackground="#D3D3D3")

        # Change Selected Color
        self.map('Treeview',
                background=[('selected', "#347083")])

class TreeFrame(tk.Frame):
    '''generic frame for Treeviews, contains treeview & vert scrollbar'''
    def __init__(self, master,
                 geometry=(310,100),
                 headings=("One", "Two", "Three"),
                 columns=(("One", tk.W, 100),
                          ("Two", tk.W, 100),
                          ("Three", tk.W, 100)),
                 dictionary={},
                 grid_x=0,
                 grid_y=0,
                 frame_sticky=tk.W):
        super(TreeFrame, self).__init__(master)


        #Create Treeview and Scrollbar widgets
        self.tree_view = ttk.Treeview(columns=headings, show="headings")
        vsb = ttk.Scrollbar(orient="vertical",
            command=self.tree_view.yview)
        self.tree_view.configure(yscrollcommand=vsb.set)
        self.tree_view.grid(column=0, row=0, sticky='nsew')
        vsb.grid(column=1, row=0, sticky='ns')


        # Create Striped Row Tags
        self.tree_view.tag_configure('oddrow', background="yellow")
        self.tree_view.tag_configure('evenrow', background="lightblue")
        self.tree_view.tag_configure('subheadrow', background="black",
                                     foreground="white")

        # Format tue Columns
        self.tree_view.column("#0", width=0, stretch=False)
        for entry in columns:
            self.tree_view.column(entry[0], anchor=entry[1],
                                  width=entry[2], stretch=False)
        # Create Headings
        self.tree_view.heading("#0", text="", anchor=tk.W)
        for heading in headings:
            self.tree_view.heading(heading, text=heading.title(), anchor=tk.W,
                                   command=lambda c=heading: sortby(self.tree,
                                                                    c, 0))
        #Fill the treeview
        line_count = 0
        for key in dictionary.keys():
            value = dictionary[key]
            if float(value[1]) < 0:
                price = ''
            else:
                price = value[1]

            if float(value[2]) < 0:
                weight = ''
            else:
                weight = value[2]

            entry = (key,value[0], price, weight)

            if price == '':
                self.tree_view.insert(parent='', index='end', iid=line_count,
                                      text='', values=entry,
                                      tags=('subheadrow',))
                
            elif line_count % 2 == 0:
                self.tree_view.insert(parent='', index='end', iid=line_count,
                                      text='', values=entry, tags=('evenrow',))
            else:
                self.tree_view.insert(parent='', index='end', iid=line_count,
                                      text='', values=entry, tags=('oddrow',))

            line_count += 1
        
        #Grid the TreeFrame
        self.grid(row=grid_y, column=grid_x, sticky=frame_sticky)
    

class Application(tk.Frame):
    '''definition of the primary frame'''
    def __init__(self, master):
        """ Initialize the Frame. """
        super(Application, self).__init__(master)
        self.grid()

        # configure style
        self.style = ListStyle(self)
        
        # variables
        self.data = tkf.Font(family="Courier")
        self.master_dictionary = {}
        self.flags = ""
        self.parse_file()
        
        self.create_widgets()
        self.update_flags() # includes call to update selection list

    def create_widgets(self):
        '''create the GUI elements'''
        #test_dict = {0 : ("A", "B"),
        #             1 : ("D", "E"),
        #             2 : ("G", "H"),
        #             3 : ("J", "K"),
        #             4 : ("M", "N"),
        #             5 : ("P", "Q")}
        self.inventory = TreeFrame(self,
                                   geometry=(400,100),
                                   headings=("ID", "Item", "Price(GP)", "Weight"),
                                   columns=(("ID", tk.W, 0),
                                            ("Item", tk.W, 200),
                                            ("Price(GP)", tk.CENTER, 55),
                                            ("Weight", tk.CENTER, 55)),
                                   dictionary=self.master_dictionary,
                                   grid_x=0,
                                   grid_y=0,
                                   frame_sticky=tk.W)
    
    def update_flags(self):
        """ rewrite the flag string """
        self.flags = ""
        
    
    def parse_file(self):
        '''set up the master item list'''
        csv = open("items.csv", "r")

        #get rid of first line in csv file
        csv.readline().split()
           
        for line in csv:
            entry = line.split(',')
            # strip whitespace, convert numerics
            entry[0] = int(entry[0])
            entry[1] = entry[1].rstrip()
            entry[2] = float(entry[2])
            entry[3] = float(entry[3])
            entry[4] = entry[4].strip()
            entry[5] = entry[5].strip()

            key = entry.pop(0)
            #value = entry[:]
            self.master_dictionary.update({key : entry})

        #for key in self.master_dictionary.keys():
        #    value = self.master_dictionary[key]
        #    print(key ,":", value)
 
        csv.close()

        #for key in self.master_dict.keys():
        #    print(key, self.master_dict[key])


# Main
root = tk.Tk()
root.title("Digital Emporium")
root.geometry("1100x500")

app = Application(root)

root.mainloop()
print('Done.')

