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

        # Connect the vertices to form the faces of the pyramid
        edges = [
            (0, 1), (0, 2), (0, 3), (0, 4),
            (1, 2), (2, 3), (3, 4), (4, 1)
        ]

        for edge in edges:
            v1 = self.pyramid_vertices[edge[0]]
            v2 = self.pyramid_vertices[edge[1]]
            self.canvas.create_line(v1[0] + 250, v1[1] + 250, v2[0] + 250, v2[1] + 250)

    def random_position_pyramid(self):
        changed_position = random.randint(0, 100)

        # Define the 2D coordinates of the vertices for a quadrant-based view
        quadrant_view_vertices = [
            (100, 250),  # Apex of the pyramid
            (50, 350),  # Base vertex 1 (Quadrant I)
            (150, 350),  # Base vertex 2 (Quadrant II)
            (150, 450),  # Base vertex 3 (Quadrant III)
            (50, 450),  # Base vertex 4 (Quadrant IV)
        ]

        if random.choice([True, False]):
            quadrant_view_vertices = [(points[0] + changed_position * 2, points[1] - changed_position * 2) for points in
                                  quadrant_view_vertices]
        else:
            quadrant_view_vertices = [(points[0] - changed_position / 2, points[1] - changed_position * 2) for points in
                                  quadrant_view_vertices]

        return quadrant_view_vertices

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

        random_color = colors[random.randint(0, len(colors) - 1)]

        quadrant_view_vertices = self.random_position_pyramid()

        # Connect the vertices to form the faces of the pyramid
        edges = [
            (0, 1), (0, 2), (0, 3), (0, 4),
            (1, 2), (2, 3), (3, 4), (4, 1)
        ]

        for edge in edges:
            v1 = quadrant_view_vertices[edge[0]]
            v2 = quadrant_view_vertices[edge[1]]
            self.canvas.create_line(v1[0], v1[1], v2[0], v2[1], fill=random_color)

    def update_colored_pyramid(self):
        if self.animation_in_progress:
            self.root.after_cancel(self.animation_in_progress)
            self.animation_in_progress = False

        self.animate_colored_pyramid()

    def animate_colored_pyramid(self):
        self.canvas.delete("all")  # Remove the pyramid
        self.root.after(500, self.random_draw_pyramid_centered)  # Wait 500 milliseconds
        self.animation_in_progress = self.root.after(1000, self.animate_colored_pyramid)  # Re-schedule the animation

    def random_draw_pyramid_centered(self):
        self.canvas.delete("all")

        colors = [
            "blanched almond", "blue", "blue violet", "brown", "burlywood", "cadet blue",
            "chartreuse", "chocolate", "coral", "cornflower blue", "cornsilk", "cyan",
            "light sky blue", "light slate gray", "light steel blue", "light yellow", "lime green",
            "pale violet red", "papaya whip", "peach puff", "peru", "pink", "plum",
            "salmon", "sandy brown", "sea green", "seashell", "sienna", "sky blue",
            "thistle", "tomato", "turquoise", "violet", "yellow", "yellow green"
        ]

        random_color = colors[random.randint(0, len(colors) - 1)]

        # Center coordinates of the canvas
        center_x = self.canvas.winfo_reqwidth() // 2
        center_y = self.canvas.winfo_reqheight() // 2

        quadrant_view_vertices = self.random_position_pyramid()

        # Offset to center the pyramid
        offset_x = center_x - sum(x for x, _ in quadrant_view_vertices) // len(quadrant_view_vertices)
        offset_y = center_y - sum(y for _, y in quadrant_view_vertices) // len(quadrant_view_vertices)

        # Adjust the pyramid vertices to keep it centered
        centered_vertices = [(x + offset_x, y + offset_y) for x, y in quadrant_view_vertices]

        # Define the faces of the pyramid
        faces = [
            [centered_vertices[0], centered_vertices[1], centered_vertices[2]],
            [centered_vertices[0], centered_vertices[2], centered_vertices[3]],
            [centered_vertices[0], centered_vertices[3], centered_vertices[4]],
            [centered_vertices[0], centered_vertices[4], centered_vertices[1]],
            [centered_vertices[1], centered_vertices[2], centered_vertices[3], centered_vertices[4]]
        ]

        # Fill the faces with the random color
        for face in faces:
            self.canvas.create_polygon(face, fill=random_color, outline="black")

        # Define the edges of the pyramid
        edges = [
            (centered_vertices[0], centered_vertices[1]),
            (centered_vertices[0], centered_vertices[2]),
            (centered_vertices[0], centered_vertices[3]),
            (centered_vertices[0], centered_vertices[4]),
            (centered_vertices[1], centered_vertices[2]),
            (centered_vertices[2], centered_vertices[3]),
            (centered_vertices[3], centered_vertices[4]),
            (centered_vertices[4], centered_vertices[1])
        ]

        # Draw all edges with black color
        for edge in edges:
            self.canvas.create_line(edge[0][0], edge[0][1], edge[1][0], edge[1][1], fill="black")


# Create the main application window
root = tk.Tk()
app = PyramidApp(root)

# Run the main event loop
root.mainloop()
