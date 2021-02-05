#WIP

import tkinter as tk
from bfs import bfs as bfs
import wikipedia

def search():
    a1 = wikipedia.page(e1.get(), auto_suggest = False)
    a2 = wikipedia.page(e2.get(), auto_suggest = False)
    list = bfs(a1, a2)


root = tk.Tk()
tk.Label(root, text = "First Name").grid(row=0)
tk.Label(root, text = "Last Name").grid(row=1)

e1 = tk.Entry(root)
e2 = tk.Entry(root)

e1.grid(row=0, column = 1)
e2.grid(row = 1, column = 1)

tk.Button(root,
          text='Show', command=search).grid(row=3,
                                                       column=1,
                                                       sticky=tk.W,
                                                       pady=4)
root.mainloop()
