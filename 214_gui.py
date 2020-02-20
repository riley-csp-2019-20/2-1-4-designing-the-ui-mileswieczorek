import tkinter as tk

# main window
root = tk.Tk()
root.wm_geometry("200x200")
root.grid()

blue = tk.Canvas(height = 100, width = 100, background = "blue")
blue.grid(row = 0, column = 0)

green = tk.Canvas(height = 100, width = 50, background = "green")
green.grid(row = 0, column= 1)

red = tk.Canvas(height = 100, width = 100, background = "red")
red.grid(row = 1, column = 0)

yellow = tk.Canvas(height = 100, width = 50, background = "yellow")
yellow.grid(row = 1, column = 1)

root.mainloop()