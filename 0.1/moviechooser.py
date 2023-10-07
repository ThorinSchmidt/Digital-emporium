# Category boxes
# Demonstrates check buttons
from tkinter import *

class Application(Frame):
    """ GUI Application for categories demo. """
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create widgets for checkbox demo. """
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

        # create easts check button
        self.display_beasts = BooleanVar()
        self.display_beasts.set(True)
        Checkbutton(self,
                    text = "Beasts",
                    variable = self.display_beasts,
                    command = self.update_flags
                    ).grid(row = 3, column = 0, sticky = W)

        # create Vehicle check button
        self.display_vehicles = BooleanVar()
        self.display_vehicles.set(True)
        Checkbutton(self,
                    text = "Vehicles",
                    variable = self.display_vehicles,
                    command = self.update_flags
                    ).grid(row = 3, column = 1, sticky = W)

        # create text field to display results
        self.results_txt = Text(self, width = 40, height = 5, wrap = WORD)
        self.results_txt.grid(row = 5, column = 0, columnspan = 3)
        self.update_flags()

    def update_flags(self):
        """ Update text widget and display user's favorite movie types. """
        flags = ""
        
        if self.display_general.get():
            flags += "G"
        
        if self.display_weapons.get():
            flags += "W"
        
        if self.display_armor.get():
            flags += "A"
        
        if self.display_beasts.get():
            flags += "B"
            
        if self.display_vehicles.get():
            flags += "V"
        
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, flags)

# main
root = Tk()
root.title("Movie Chooser")
app = Application(root)
root.mainloop()
