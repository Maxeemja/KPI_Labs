import tkinter as tk
import time

# Function to create an isometric 2D triangle
def create_triangle(canvas, window_width, window_height):
    triangle_size = 50
    x1 = (window_width - triangle_size) / 2
    y1 = (window_height - triangle_size) / 2
    x2 = x1 + triangle_size
    y2 = y1
    x3 = x1 + triangle_size / 2
    y3 = y1 - (triangle_size * (3**0.5)) / 2

    return canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill="blue")

# Function to scale up the triangle
def scale_up_animation(canvas, triangle, window_width, window_height):
    for _ in range(5):
        canvas.scale(triangle, window_width / 2, window_height / 2, 1.2, 1.2)
        canvas.update()
        time.sleep(0.5)

# Function to move the triangle left and right
def move_lr_animation(canvas, triangle, window_width, window_height):
    for _ in range(150):
        canvas.move(triangle, -1, 0)
        canvas.update()
        time.sleep(0.01)
    for _ in range(150):
        canvas.move(triangle, 1, 0)
        canvas.update()
        time.sleep(0.01)

# Function to scale down the triangle
def scale_down_animation(canvas, triangle, window_width, window_height):
    for _ in range(5):
        canvas.scale(triangle, window_width / 2, window_height / 2, 0.8, 0.8)
        canvas.update()
        time.sleep(0.5)

# Function to stop the current animation and clear the canvas
def stop_animation():
    global current_animation
    canvas.delete("all")  # Clear the canvas
    if current_animation is not None:
        root.after_cancel(current_animation)

        current_animation = None

# Function to start the selected animation and clear the canvas
def start_animation(animation_func):
    stop_animation()
    triangle = create_triangle(canvas, root.winfo_width(), root.winfo_height())
    animation_func(canvas, triangle, root.winfo_width(), root.winfo_height())
    global current_animation
    current_animation = root.after(1, lambda: start_animation(animation_func))

# Create the main window
root = tk.Tk()
root.title("Triangle Manipulation")

# Set the initial window size to accommodate animations
initial_width = 350
initial_height = 300
root.geometry(f"{initial_width}x{370}")

# Create a canvas for drawing
canvas = tk.Canvas(root, width=initial_width, height=initial_height, bg="white")
canvas.pack()

# Create a frame for buttons
button_frame = tk.Frame(root)
button_frame.pack()

# Create buttons for different actions
button1 = tk.Button(button_frame, text="Scale Up", command=lambda: start_animation(scale_up_animation))
button2 = tk.Button(button_frame, text="Move Left/Right", command=lambda: start_animation(move_lr_animation))
button3 = tk.Button(button_frame, text="Scale Down", command=lambda: start_animation(scale_down_animation))

button1.pack(side="left", padx=10)
button2.pack(side="left", padx=10)
button3.pack(side="left", padx=10)

# Variable to store the current animation
current_animation = None

root.mainloop()
