import cv2

image = cv2.imread("logo.png")

new_width = 400
new_height = int(image.shape[0] * (new_width / image.shape[0]))

resized_image = cv2.resize(image, (new_width,new_height))

cv2.imshow("Boyulandirma Goruntu",resized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

rotated_90 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("Dondurulmus Goruntu",rotated_90)

cv2.waitKey(0)
cv2.destroyAllWindows()