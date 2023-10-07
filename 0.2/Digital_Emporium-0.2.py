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

class Application(tk.Frame):
    '''definition of the primary frame'''
    
    def __init__(self, master):
        """ Initialize the Frame. """
        super(Application, self).__init__(master)
        self.grid()
        
        # variables
        self.data = tkf.Font(family="Courier")
        self.master_dictionary = {}
        self.headings = []
        self.flags = ""
        self.parse_file()
        
        self.create_widgets()
        self.update_flags() # includes call to update selection list

    def create_widgets(self):
        '''create the data structures and GUI elements'''
        pass
    
    def update_flags(self):
        """ rewrite the flag string """
        self.flags = ""
        
    
    def parse_file(self):
        '''set up the master item list'''
        csv = open("items.csv", "r")

        self.headings = csv.readline().split()
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

        for key in self.master_dictionary.keys():
            value = self.master_dictionary[key]
            print(key ,":", value)
 
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

