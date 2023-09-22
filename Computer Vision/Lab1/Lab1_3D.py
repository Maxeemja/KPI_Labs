import math
import tkinter as tk
import random
import numpy as np

class PyramidApp:
    def __init__(self, root):
        self.root = root
        self.root.title("3D Quadrant-Based Pyramid")

        self.animation_in_progress = False

        # Create three buttons
        self.button1 = tk.Button(root, text="Axonometric Projection", command=self.axonometric_projection)
        self.button2 = tk.Button(root, text="Cyclic Rotation", command=self.cyclic_rotation)
        self.button3 = tk.Button(root, text="Animate Pyramid", command=self.update_colored_pyramid)

        # Pack the buttons at the top in the center
        self.button1.pack(fill=tk.X, side='top')
        self.button2.pack(fill=tk.X, side='top')
        self.button3.pack(fill=tk.X, side='top')

        self.canvas = tk.Canvas(root, width=500, height=500)
        self.canvas.pack()

        # Define the vertices of a 3D quadrant-based pyramid
        self.pyramid_vertices_origin = [
            (0, 0, 0),  # Apex of the pyramid
            (-50, -50, 50),  # Base vertex 1 (Quadrant I)
            (50, -50, 50),  # Base vertex 2 (Quadrant II)
            (50, 50, 50),  # Base vertex 3 (Quadrant III)
            (-50, 50, 50),  # Base vertex 4 (Quadrant IV)
        ]

        self.pyramid_vertices = self.pyramid_vertices_origin.copy()

        self.angle = 5  # Initial rotation angle in degrees
        self.rotation_matrix = self.rotation_matrix_y(self.angle)

    def axonometric_projection(self):
        if self.animation_in_progress:
            self.root.after_cancel(self.animation_in_progress)
            self.animation_in_progress = False

        self.project_3d_to_2d()
        self.draw_pyramid()

    def cyclic_rotation(self):
        self.pyramid_vertices = self.pyramid_vertices_origin.copy()
        if self.animation_in_progress:
            self.root.after_cancel(self.animation_in_progress)
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
        self.animation_in_progress = self.root.after(100, self.cyclic_rotate_pyramid)

    def draw_pyramid(self):
        self.canvas.delete("all")

        # Connect the vertices to form the quadrants of the pyramid
        quadrant_edges = [(0, 1, 2), (0, 2, 3), (0, 3, 4), (0, 4, 1)]

        for edges in quadrant_edges:
            for i in range(len(edges)):
                v1 = self.pyramid_vertices[edges[i]]
                v2 = self.pyramid_vertices[edges[(i + 1) % len(edges)]]
                self.canvas.create_line(v1[0] + 250, v1[1] + 250, v2[0] + 250, v2[1] + 250)

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

        # Connect the vertices to form the quadrants of the pyramid
        quadrant_edges = [(0, 1, 2), (0, 2, 3), (0, 3, 4), (0, 4, 1)]

        for edges in quadrant_edges:
            for i in range(len(edges)):
                v1 = self.pyramid_vertices_origin[edges[i]]
                v2 = self.pyramid_vertices_origin[edges[(i + 1) % len(edges)]]
                self.canvas.create_line(v1[0] + 250, v1[1] + 250, v2[0] + 250, v2[1] + 250, fill=random_color)

        self.animation_in_progress = self.root.after(1000, self.random_draw_pyramid)

    def perspective_projection(self, distance):
        perspective_vertices = []

        for vertex in self.pyramid_vertices_origin:
            x, y, z = vertex
            perspective_x = x / (1 + z / distance)
            perspective_y = y / (1 + z / distance)
            perspective_vertices.append((perspective_x, perspective_y))

        self.pyramid_vertices = perspective_vertices

    def update_colored_pyramid(self):
        if self.animation_in_progress:
            self.root.after_cancel(self.animation_in_progress)
            self.animation_in_progress = False

        distance = 500  # Adjust this value to control the perspective effect

        self.perspective_projection(distance)
        self.random_draw_pyramid()

# Create the main application window
root = tk.Tk()
app = PyramidApp(root)

# Run the main event loop
root.mainloop()
