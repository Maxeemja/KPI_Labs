import tkinter as tk
import time

canvas = None

def draw_pyramid():
    global canvas
    canvas.delete("all")
    # Coordinates of the base vertices of the pyramid
    base_vertices = [
        (100, 300),  # Bottom-left
        (300, 300),  # Bottom-right
        (300, 100),  # Top-right
        (100, 100),  # Top-left
    ]
    apex = (200, 0)  # Apex of the pyramid

    # Draw the base quadrilateral
    canvas.create_polygon(base_vertices[0], base_vertices[1], base_vertices[2], base_vertices[3], fill='#008000', outline='black', stipple='gray50')
    # Draw the three triangular faces of the pyramid
    canvas.create_polygon(apex, base_vertices[0], base_vertices[1], fill='#0000FF', outline='black', stipple='gray50')
    canvas.create_polygon(apex, base_vertices[1], base_vertices[2], fill='#FF6347', outline='black', stipple='gray50')
    canvas.create_polygon(apex, base_vertices[2], base_vertices[3], fill='#FF0000', outline='black', stipple='gray50')
    canvas.create_polygon(apex, base_vertices[3], base_vertices[0], fill='#FFFF00', outline='black', stipple='gray50')

def interpolation():
    global canvas
    canvas.delete("all")
    base_vertices = [
        (100, 300),  # Bottom-left
        (300, 300),  # Bottom-right
        (300, 100),  # Top-right
        (100, 100),  # Top-left
    ]
    apex = (200, 0)  # Apex of the pyramid

    lines = [
        (apex, base_vertices[0]),
        (apex, base_vertices[1]),
        (apex, base_vertices[2]),
        (apex, base_vertices[3]),
        (base_vertices[0], base_vertices[1]),
        (base_vertices[1], base_vertices[2]),
        (base_vertices[2], base_vertices[3]),
        (base_vertices[3], base_vertices[0]),
    ]

    def linear_interpolation(p1, p2, n=100):
        x1, y1 = p1
        x2, y2 = p2
        return [(x1 + (x2 - x1) * i / n, y1 + (y2 - y1) * i / n) for i in range(n + 1)]

    def update_image():
        canvas.delete("lines")
        for line in lines:
            interpolated = linear_interpolation(line[0], line[1])
            for i in range(len(interpolated) - 1):
                point1, point2 = interpolated[i], interpolated[i + 1]
                canvas.create_line(point1, point2, tags="lines", fill="black")
                canvas.update()
                time.sleep(0.01)

    update_image()

def back_face_culling():
    global canvas
    canvas.delete("all")

    def is_backface(vertices):
        # Define the view direction (in this case, from the top)
        view_direction = (0, 0, -2)

        # Calculate the normal vector for the base quadrilateral
        v1 = (vertices[1][0] - vertices[0][0], vertices[1][1] - vertices[0][1], vertices[1][2] - vertices[0][2])
        v2 = (vertices[2][0] - vertices[0][0], vertices[2][1] - vertices[0][1], vertices[2][2] - vertices[0][2])
        base_normal_vector = (
            v1[1] * v2[2] - v1[2] * v2[1],
            v1[2] * v2[0] - v1[0] * v2[2],
            v1[0] * v2[1] - v1[1] * v2[0]
        )

        # Check the angle between the view direction and the base normal
        dot_product = sum(i * j for i, j in zip(base_normal_vector, view_direction))
        return dot_product >= 0

    def draw():
        canvas.delete("all")
        base_vertices = [
            (100, 300, 0),  # Bottom-left
            (300, 300, 0),  # Bottom-right
            (300, 100, 0),  # Top-right
            (100, 100, 0),  # Top-left
        ]
        apex = (200, 0, 150)  # Apex of the pyramid

        for i, vertices_indices in enumerate([(apex, base_vertices[0], base_vertices[1]),
                                               (apex, base_vertices[1], base_vertices[2]),
                                               (apex, base_vertices[2], base_vertices[3]),
                                               (apex, base_vertices[3], base_vertices[0])]):
            if not is_backface(vertices_indices):
                canvas.create_polygon([v[0:2] for v in vertices_indices], fill=f'#{i * 50:02X}0000',
                                      outline='black', stipple='gray50')

    draw()

def main():
    global canvas
    root = tk.Tk()
    root.title("Lab3")
    canvas = tk.Canvas(root, width=400, height=400)
    canvas.pack()
    button1 = tk.Button(root, text="Draw with Back Face Culling", command=back_face_culling)
    button2 = tk.Button(root, text="Draw with Interpolation", command=interpolation)
    button3 = tk.Button(root, text="Draw All", command=draw_pyramid)

    button1.pack()
    button1.pack(side="left")
    button2.pack()
    button2.pack(side="left")
    button3.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
