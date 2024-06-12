import cv2
import numpy as np

# Đọc hình ảnh
image = cv2.imread('image2.jpg')

# Changing color spaces
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
# gray_image = cv2.medianBlur(gray_image, 5)

# Geometric Transformations of Images
height, width = image.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 45, 1)
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
scaled_image = cv2.resize(image, None, fx=0.5, fy=1)

translation_matrix = np.float32([[1, 0, 100], [0, 1, 50]])
translated_image = cv2.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))
flipped_image_x = cv2.flip(image,1)

# Image Thresholding
_, binary_threshold = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
adaptive_threshold = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
_, otsu_threshold = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Smoothing Images
avg_blur = cv2.blur(image, (5, 5))
median_blur = cv2.medianBlur(image, 5)
gaussian_blur = cv2.GaussianBlur(gray_image, (5, 5), 0)
bil_blur = cv2.bilateralFilter(image, 9, 75, 75)

# Gradient Images
sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=5)
schar_x = cv2.Scharr(gray_image, cv2.CV_64F, 1, 0)
schar_y = cv2.Scharr(gray_image, cv2.CV_64F, 0, 1)
magnitude_sobel = cv2.magnitude(sobel_x, sobel_y)
angel_sobel = cv2.phase(sobel_x, sobel_y, angleInDegrees=True)
laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)

# Canny Edge Detection
canny = cv2.Canny(gaussian_blur, 10, 60)
 
# Contours
# contours, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

# Hiển thị hình ảnh 
# cv2.imshow("transformed image", canny)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

lines = cv2.HoughLines(canny, 1, np.pi/180, 200)

if lines is not None:
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

circles = cv2.HoughCircles(canny, cv2.HOUGH_GRADIENT, dp=1, minDist=20, param1=50, param2=30, minRadius=0, maxRadius=0)

# if circles is not None:
#     circles = np.uint16(np.around(circles))
#     for circle in circles[0, :]:
#         center = (circle[0], circle[1])
#         radius = circle[2]
#         cv2.circle(image, center, radius, (0, 255, 0), 2)


cv2.imshow('Detected Objects', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
