import cv2

def get_contour(image):
    # Перетворіть зображення в градієнти Грінна
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gradient = cv2.morphologyEx(grayscale, cv2.MORPH_GRADIENT, (3, 3))

    # Знайдіть контури в зображенні
    contours, hierarchy = cv2.findContours(gradient, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Знайдіть найбільший контур
    largest_contour = max(contours, key=cv2.contourArea)

    # Поверніть контур
    return largest_contour


if __name__ == "__main__":
    # Завантажте зображення
    image = cv2.imread("input.png")

    # Отримайте контур об'єкта ідентифікації
    contour = get_contour(image)

    # Нанесіть контур на зображення
    cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)

    # Покажіть зображення
    cv2.imshow("Image", image)
    cv2.waitKey(0)
