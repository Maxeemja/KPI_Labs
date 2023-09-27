from PIL import Image, ImageFilter, ImageOps, ImageEnhance


def change_brightness(image, factor):
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)


def convert_to_grayscale(image):
    return ImageOps.grayscale(image)


def apply_negative(image):
    return ImageOps.invert(image)


def apply_sepia(image):
    width, height = image.size
    sepia_filter = Image.new('RGB', (width, height))
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            tr = int((r * 0.393) + (g * 0.769) + (b * 0.189))
            tg = int((r * 0.349) + (g * 0.686) + (b * 0.168))
            tb = int((r * 0.272) + (g * 0.534) + (b * 0.131))
            sepia_filter.putpixel((x, y), (tr, tg, tb))
    return sepia_filter


def apply_sepia_with_diagonal_gradient(image):
    sepia_img = apply_sepia(image.copy())  # Apply Sepia to a copy of the original image
    if sepia_img:
        gradient = Image.new('L', image.size, 0)
        width, height = image.size
        for x in range(min(width, height)):
            gradient.putpixel((x, x), int((x / min(width, height)) * 255))
        return Image.composite(sepia_img, image, gradient)
    return None

def apply_sepia_with_gradient_from_center(image):
    sepia_img = apply_sepia(image.copy())  # Apply Sepia to a copy of the original image
    if sepia_img:
        gradient = Image.new('L', image.size, 0)
        width, height = image.size
        for y in range(height):
            gradient.putpixel((width // 2, y), int((y / height) * 255))
        return Image.composite(sepia_img, image, gradient)
    return None

def apply_sepia_with_gradient_to_center(image):
    sepia_img = apply_sepia(image.copy())  # Apply Sepia to a copy of the original image
    if sepia_img:
        gradient = Image.new('L', image.size, 0)
        width, height = image.size
        for y in range(height):
            gradient.putpixel((width // 2, y), int(((height - y) / height) * 255))
        return Image.composite(sepia_img, image, gradient)
    return None

def main():
    input_image_path = 'test2.jpg'
    output_image_path = 'output_image.jpg'

    with Image.open(input_image_path) as img:
        print("Choose a color correction and gradient combination:")
        print("1. Change Brightness")
        print("2. Convert to Grayscale")
        print("3. Apply Negative")
        print("4. Apply Sepia with Diagonal Gradient")
        print("5. Apply Sepia with Gradient from Center")
        print("6. Apply Sepia with Gradient to Center")

        choice = int(input("Enter your choice (1-6): "))

        if choice == 1:
            img = change_brightness(img, 0.3)  # Adjust brightness (1.0 is the original)
        elif choice == 2:
            img = convert_to_grayscale(img)  # Convert to grayscale
        elif choice == 3:
            img = apply_negative(img)  # Apply negative effect
        elif choice >= 4 and choice <= 6:
            sepia_img = apply_sepia(img.copy())  # Make a copy of the original image and apply Sepia to it
            if sepia_img:
                if choice == 4:
                    img = apply_sepia_with_diagonal_gradient(sepia_img)  # Sepia with diagonal gradient
                elif choice == 5:
                    img = apply_sepia_with_gradient_from_center(sepia_img)  # Sepia with gradient from center
                elif choice == 6:
                    img = apply_sepia_with_gradient_to_center(sepia_img)  # Sepia with gradient to center

        if img is not None:
            img.save(output_image_path)
            print(f"Applied selected effect and saved as {output_image_path}")
        else:
            print("An error occurred while processing the image.")


if __name__ == "__main__":
    main()
