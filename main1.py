import cv2

image1 = cv2.imread("input11.jpg")
image2=cv2.imread("input22.jpg")
resize1 = cv2.resize(image1, (500,500))
resize2 = cv2.resize(image2, (500,500))
#0.5 and 0.4 are weeights to be multiplied for each pixel,
#0 is gamma_value(measurment of brightness)

addImage = cv2.addWeighted(resize1,0.5,resize2,0.4,0)

cv2.imshow("Output Image", addImage)
cv2.waitKey(0)
cv2.destroyAllWindows()