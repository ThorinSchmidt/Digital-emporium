# -*- coding: utf-8 -*-
import tkinter as tk
 
def getElement(event):
  selection = event.widget.curselection()
  index = selection[0]
  value = event.widget.get(index)
  
  result.set(value)
  print(index,' -> ',value)

def left_press(event):
  print("pressed left")
  selection = event.widget.curselection()
  index = selection[0]
  value = event.widget.get(index)
  print(index,' -> ',value)

def right_press(event):
  print("pressed right")
  selection = event.widget.curselection()
  index = selection[0]
  value = event.widget.get(index)
  print(index,' -> ',value)

 
root = tk.Tk()
root.title("Code4Example.com")     # Add a title
 
result =tk.StringVar()
 
tk.Label(root,text="""Click Listbox Element""").grid(row = 0, column = 0)
tk.Label(root,text="""result""", textvariable=result).grid(row = 1, column = 0)
 
var2 = tk.StringVar()
var2.set(('Apple','Banana','Pear', 'Peach'))
lb = tk.Listbox(root, listvariable=var2)
lb.grid(row = 0, column = 1)
lb.bind('<<ListboxSelect>>', getElement) #Select click
lb.bind('<Left>', left_press)
lb.bind('<Right>', right_press)
 
 
root.mainloop()
