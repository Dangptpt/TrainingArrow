import cv2
import imutils
image = cv2.imread('Project/Img/page_1.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150)

contours = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
contours = sorted(contours, key=cv2.contourArea, reverse=False)

cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
number = 0
# loop over our contours
for c in contours:
    (x, y, w, h) = cv2.boundingRect(c)
    print(x, y, w, h)
    # approximate the contour
    
print(f"Number of Contours found = {number}" )


# cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
# cv2.imshow('Pix',img)
# cv2.imshow('Thres',thres)
# cv2.waitKey()
# cv2.destroyAllWindows()