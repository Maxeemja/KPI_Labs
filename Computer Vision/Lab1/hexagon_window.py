import math
import time
import tkinter as tk

class HexagonWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Hexagon Window")

        self.animation_in_progress = False

        # Create three buttons
        self.button1 = tk.Button(self, text="Rotation", command=self.hexagon_rotation)
        self.button2 = tk.Button(self, text="Moving", command=self.hexagon_moving)
        self.button3 = tk.Button(self, text="Scaling", command=self.hexagon_scaling)

        # Pack the buttons at the top in the center
        self.button1.pack(fill=tk.X, side='top')
        self.button2.pack(fill=tk.X, side='top')
        self.button3.pack(fill=tk.X, side='top')

        self.canvas = tk.Canvas(self, width=500, height=500)
        self.canvas.pack()

        # Define the hexagon as a 2D list of coordinates (x, y)
        self.hexagon_matrix_origin = [
            (250, 220),
            (275, 220),
            (287.5, 237.5),
            (275, 255),
            (250, 255),
            (237.5, 237.5),
        ]
        self.hexagon_matrix = self.hexagon_matrix_origin

        self.rotation_angle = 15  # Initial rotation angle
        self.scale_factor = 1.2
        self.x_center, self.y_center = 300, 250
        self.scale_int = -0.1

    def hexagon_rotation(self):
        if self.animation_in_progress:
            self.canvas.after_cancel(self.animation_in_progress)
            self.animation_in_progress = False

        self.create_hexagon()
        self.update_hexagon()

    def hexagon_moving(self):
        if self.animation_in_progress:
            self.canvas.after_cancel(self.animation_in_progress)
            self.animation_in_progress = False

        self.create_hexagon()
        self.move_hexagon()

    def move_hexagon(self, step_count=0):
        if step_count < 50:
            start_position = (100, 100)
            end_position = (500, 500)

            step_x = (end_position[0] - start_position[0]) / 50
            step_y = (end_position[1] - start_position[1]) / 50

            new_position = [(start_position[0] + step_x * step_count - 200, start_position[1] + step_y * step_count - 200)
                            for start_position in self.hexagon_matrix_origin]
            self.canvas.coords(self.hexagon, *sum(new_position, ()))
            step_count += 1
            self.animation_in_progress = self.after(100, self.move_hexagon, step_count)
        else:
            # Reset the position after each movement
            # self.canvas.coords(self.hexagon, *sum(self.hexagon_matrix_origin, ()))
            self.animation_in_progress = self.after(100, self.move_hexagon)  # Move again after 1 second

    def hexagon_scaling(self):
        if self.animation_in_progress:
            self.canvas.after_cancel(self.animation_in_progress)
            self.animation_in_progress = False

        self.create_hexagon()
        self.update_scaling()

    def update_scaling(self):
        if self.scale_factor > 1.7:
            self.scale_factor -= 0.1
            self.scale_int = -0.1
        elif self.scale_factor < 0.6:
            self.scale_factor += 0.1
            self.scale_int = 0.1
        else:
            self.scale_factor += self.scale_int

        scaled_hexagon_matrix = [
            ((x - self.x_center) * self.scale_factor + self.x_center,
             (y - self.y_center) * self.scale_factor + self.y_center)
            for x, y in self.hexagon_matrix
        ]

        self.hexagon_matrix = scaled_hexagon_matrix
        self.canvas.coords(self.hexagon, *sum(scaled_hexagon_matrix, ()))  # Flatten the list and update canvas

        self.animation_in_progress = self.after(400, self.update_scaling)

    def rotate_point(self, point, angle):
        x, y = point
        angle_rad = math.radians(angle)
        x_new = (x - self.x_center) * math.cos(angle_rad) - (y - self.y_center) * math.sin(angle_rad) + self.x_center
        y_new = (x - self.x_center) * math.sin(angle_rad) + (y - self.y_center) * math.cos(angle_rad) + self.y_center
        return (round(x_new), round(y_new))

    def create_hexagon(self):
        self.canvas.delete("all")
        self.hexagon_matrix = self.hexagon_matrix_origin
        self.hexagon = self.canvas.create_polygon(self.hexagon_matrix, outline='black', width=1, fill='gray')

        self.loop_counter = 0
        time.sleep(0.5)

    def rotate_hexagon(self, hexagon, angle):
        return [self.rotate_point(point, angle) for point in hexagon]

    def update_hexagon(self):
        self.loop_counter += 1
        if self.loop_counter % 15 == 0:
            angle = math.radians(self.loop_counter)
            radius = 50 + 30 * math.sin(angle)
            self.x_center = 300 + radius * math.cos(angle)
            self.y_center = 250 + radius * math.sin(angle)

        self.hexagon_matrix = self.rotate_hexagon(self.hexagon_matrix, self.rotation_angle)
        flat_coordinates = [coord for pair in self.hexagon_matrix for coord in pair]
        self.canvas.coords(self.hexagon, *flat_coordinates)
        self.animation_in_progress = self.after(300, self.update_hexagon)
