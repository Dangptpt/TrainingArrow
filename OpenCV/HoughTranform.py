import cv2
import numpy as np

# Đọc hình ảnh
img = cv2.imread('image1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

cv2.imshow('Gray 1', gray1)
cv2.imshow('Gray 2', gray2)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Áp dụng Gaussian Blur để làm mịn hình ảnh và giảm nhiễu
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Phát hiện các cạnh trong hình ảnh bằng phương pháp Canny Edge Detection
edges = cv2.Canny(blur, 50, 150)

# Phát hiện các đường thẳng bằng Hough Line Transform
lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

# Vẽ các đường thẳng được phát hiện trên hình ảnh gốc
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
        cv2.line(image2, (x1, y1), (x2, y2), (0, 0, 255), 2)

# Phát hiện các hình tròn bằng Hough Circle Transform
#circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1, minDist=20, param1=50, param2=30, minRadius=0, maxRadius=0)

# Vẽ các hình tròn được phát hiện trên hình ảnh gốc
# if circles is not None:
#     circles = np.uint16(np.around(circles))
#     for circle in circles[0, :]:
#         center = (circle[0], circle[1])
#         radius = circle[2]
#         cv2.circle(img, center, radius, (0, 255, 0), 2)

# Hiển thị hình ảnh với các đường thẳng và hình tròn được phát hiện
cv2.imshow('Detected Objects', image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
