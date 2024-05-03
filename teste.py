from tkinter import *

def on_close():
    global running
    running = False
    root.destroy()

root = Tk()
running = True

root.protocol("WM_DELETE_WINDOW", on_close)

while running:
    root.update_idletasks()
    root.update()
