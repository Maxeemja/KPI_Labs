import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image, ImageEnhance

def enhance_image(image):
    im = Image.open(image)
    enhancer = ImageEnhance.Sharpness(im)
    factor = 10
    im_s_1 = enhancer.enhance(factor)
    im_s_1.save('enhanced_image.png')
    return 'enhanced_image.png'

def show_histogram(image, title):
    plt.hist(image.ravel(), 256, [0, 256])
    plt.title(title)
    plt.show()

def detect_sown_areas(image):
    # Convert the image to the HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the lower and upper threshold for the color of sown areas (greenish color for vegetation)
    lower_green = np.array([25, 50, 50])
    upper_green = np.array([100, 255, 255])

    # Mask the image to extract the sown areas based on the defined color threshold
    mask = cv2.inRange(hsv_image, lower_green, upper_green)
    sown_areas = cv2.bitwise_and(image, image, mask=mask)

    return sown_areas, mask

def main():
    # Define the path to your satellite image
    image_path = "input3.jpg"

    # Load the input image
    input_image = cv2.imread(image_path)

    # Resize the input image to 600x600
    resized_image = cv2.resize(input_image, (600, 600))

    # Save the resized image
    cv2.imwrite('resized_image.png', resized_image)

    # Enhance the resized image
    enhanced_image_path = enhance_image('resized_image.png')

    # Load the enhanced satellite image
    enhanced_image = cv2.imread(enhanced_image_path)

    # Detect sown areas
    sown_areas_image, mask = detect_sown_areas(enhanced_image)

    # Display the enhanced image and sown areas mask
    cv2.imshow('Enhanced Satellite Image', enhanced_image)
    plt.imshow(mask, cmap='gray')
    plt.title('Sown Areas Mask')
    plt.show()

    # Show histograms of the enhanced image and sown areas mask
    show_histogram(mask, 'Sown Areas Mask Histogram')
    show_histogram(input_image, 'Original Image Histogram')

    show_histogram(cv2.cvtColor(enhanced_image, cv2.COLOR_BGR2GRAY), 'Enhanced Image Histogram')
    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw rectangles around the detected sown areas
    result_image = enhanced_image.copy()
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(result_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the sown areas detected with rectangle borders
    cv2.imshow('Detected Sown Areas', result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
