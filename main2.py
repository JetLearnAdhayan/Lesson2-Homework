import cv2

image1 = cv2.imread("input11.jpg")
image2=cv2.imread("input22.jpg")
resize1 = cv2.resize(image1, (500,500))
resize2 = cv2.resize(image2, (500,500))
subtractimage = cv2.subtract(resize1,resize2)
cv2.imshow("Output Image", subtractimage)

cv2.waitKey(0)
cv2.destroyAllWindows()

