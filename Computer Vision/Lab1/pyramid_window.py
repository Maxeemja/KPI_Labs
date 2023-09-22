import math
import time
import tkinter as tk
import random
import numpy as np

class PyramidWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("3D Pyramid Window")

        self.animation_in_progress = False

        # Create three buttons
        self.button1 = tk.Button(self, text="Axonometric Projection", command=self.axonometric_projection)
        self.button2 = tk.Button(self, text="Cyclic Rotation", command=self.cyclic_rotation)
        self.button3 = tk.Button(self, text="Animate Pyramid", command=self.update_colored_piramid)

        # Pack the buttons at the top in the center
        self.button1.pack(fill=tk.X, side='top')
        self.button2.pack(fill=tk.X, side='top')
        self.button3.pack(fill=tk.X, side='top')

        self.canvas = tk.Canvas(self, width=500, height=500)
        self.canvas.pack()

        # Define the vertices of a 3D pyramid
        self.pyramid_vertices_origin = [
            (0, 0, 0),  # Apex of the pyramid
            (-50, -50, 50),  # Base vertex 1
            (50, -50, 50),  # Base vertex 2
            (50, 50, 50),  # Base vertex 3
        ]

        self.pyramid_vertices = self.pyramid_vertices_origin.copy()

        self.angle = 5  # Initial rotation angle in degrees
        self.rotation_matrix = self.rotation_matrix_y(self.angle)

    def axonometric_projection(self):
        if self.animation_in_progress:
            self.canvas.after_cancel(self.animation_in_progress)
            self.animation_in_progress = False

        self.project_3d_to_2d()
        self.draw_pyramid()

    def cyclic_rotation(self):
        self.pyramid_vertices = self.pyramid_vertices_origin.copy()
        if self.animation_in_progress:
            self.canvas.after_cancel(self.animation_in_progress)
            self.animation_in_progress = False

        self.cyclic_rotate_pyramid()

    def project_3d_to_2d(self):
        projection_matrix = np.array([[1, -math.sqrt(2) / 2, 0],
                                      [0, math.sqrt(2) / 2, 0]])

        self.pyramid_vertices = [np.dot(projection_matrix, vertex) for vertex in self.pyramid_vertices_origin]

    def rotation_matrix_y(self, angle_deg):
        angle_rad = math.radians(angle_deg)
        c = math.cos(angle_rad)
        s = math.sin(angle_rad)
        return np.array([[c, 0, s],
                         [0, 1, 0],
                         [-s, 0, c]])

    def cyclic_rotate_pyramid(self):
        self.pyramid_vertices = [np.dot(self.rotation_matrix_y(self.angle), vertex) for vertex in self.pyramid_vertices]
        self.angle = 15
        self.draw_pyramid()
        self.animation_in_progress = self.canvas.after(100, self.cyclic_rotate_pyramid)

    def draw_pyramid(self):
        self.canvas.delete("all")

        # Connect the vertices to form the triangular faces of the pyramid
        base_edges = [(0, 1), (0, 2), (0, 3)]
        side_edges = [(1, 2), (2, 3), (3, 1)]

        for edge in base_edges:
            v1 = self.pyramid_vertices[edge[0]]
            v2 = self.pyramid_vertices[edge[1]]
            self.canvas.create_line(v1[0] + 250, v1[1] + 250, v2[0] + 250, v2[1] + 250)

        for edge in side_edges:
            v1 = self.pyramid_vertices[edge[0]]
            v2 = self.pyramid_vertices[edge[1]]
            self.canvas.create_line(v1[0] + 250, v1[1] + 250, v2[0] + 250, v2[1] + 250)

    def random_position_pyramid(self):
        changed_position =  random.randint(0, 100)

        # Define the 2D coordinates of the vertices for side view
        side_view_vertices = [
            (100, 250),  # Apex of the pyramid
            (50, 350),  # Base vertex 1
            (150, 350),  # Base vertex 2
            (150, 450),  # Base vertex 3
        ]

        if random.choice([True, False]):
            side_view_vertices = [(points[0] + changed_position * 2, points[1] - changed_position * 2) for points in
                                  side_view_vertices]
        else:
            side_view_vertices = [(points[0] - changed_position / 2  , points[1] - changed_position * 2) for points in
                                  side_view_vertices]
        print(side_view_vertices)

        return side_view_vertices


    def random_draw_pyramid(self):
        self.canvas.delete("all")

        colors = [
            "blanched almond", "blue", "blue violet", "brown", "burlywood", "cadet blue",
            "chartreuse", "chocolate", "coral", "cornflower blue", "cornsilk", "cyan",
            "light sky blue", "light slate gray", "light steel blue", "light yellow", "lime green",
            "pale violet red", "papaya whip", "peach puff", "peru", "pink", "plum",
            "salmon", "sandy brown", "sea green", "seashell", "sienna", "sky blue",
            "thistle", "tomato", "turquoise", "violet", "yellow", "yellow green"
        ]

        random_color = colors[random.randint(0, len(colors)-1)]

        side_view_vertices = self.random_position_pyramid()

        # Connect the vertices to form the triangular faces of the pyramid
        edges = [(0, 1), (0, 2), (0, 3), (1, 2), (2, 3), (3, 1)]

        for edge in edges:
            v1 = side_view_vertices[edge[0]]
            v2 = side_view_vertices[edge[1]]
            self.canvas.create_line(v1[0], v1[1], v2[0], v2[1], fill= random_color)

        # Connect the side vertices to complete the side faces
        for i in range(1, 4):
            v1 = side_view_vertices[i]
            v2 = side_view_vertices[i % 3 + 1]
            self.canvas.create_line(v1[0], v1[1], v2[0], v2[1], fill=random_color)

        self.animation_in_progress = self.after(500, self.random_draw_pyramid)


    def update_colored_piramid(self):
        if self.animation_in_progress:
            self.canvas.after_cancel(self.animation_in_progress)
            self.animation_in_progress = False

        self.random_draw_pyramid()



