import tkinter as tk
from test3d import PyramidWindow2
from pyramid_window import PyramidWindow

def open_pyramid_window2():
    pyramid_window = PyramidWindow2(root)
def open_pyramid_window():
    pyramid_window = PyramidWindow(root)

root = tk.Tk()
root.title("Main Window")
root.geometry("400x200")


hexagon_button = tk.Button(root, text="2D Operations", command=open_pyramid_window2)
hexagon_button.pack(pady=10)

pyramid_button = tk.Button(root, text="3D Operations", command=open_pyramid_window)
pyramid_button.pack(pady=10)

root.mainloop()
