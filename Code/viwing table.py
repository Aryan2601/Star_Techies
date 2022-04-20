from tkinter import *
from tkinter import ttk
from database import *
def seeing_complaints():
   win = Tk()
   win.geometry("700x350")
  # Create an object of Style widget
   style = ttk.Style()
   style.theme_use('clam')
   tree = ttk.Treeview(win, column=("UserID", "Issue",), show='headings', height=5)
   tree.column("# 1", anchor=CENTER)
   tree.heading("# 1", text="userID")
   tree.column("# 2", anchor=CENTER)
   tree.heading("# 2", text="Issue")
   records = view_complaints()
   print(records)
   for row in records:
       tree.insert('', 'end', text="1", values=(row[0],row[1]))
   tree.pack()

   win.mainloop()
seeing_complaints()
