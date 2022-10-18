import cv2

image = cv2.imread('img1.jpg')
cv2.imwrite("0_Original.png", image)

g_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("1_Gray_Scale.png", g_scale)

inv_g_scale = cv2.bitwise_not(g_scale)
cv2.imwrite("2_Inverted_Gray_Scale.png", inv_g_scale)

blur = cv2.GaussianBlur(inv_g_scale, (17,17), 0)
cv2.imwrite("3_Blurred.png", blur)

inv_blur = cv2.bitwise_not(blur)
cv2.imwrite("4_Inverted_Blurred.png", inv_blur)

ans = cv2.divide(g_scale, inv_blur, scale = 256.0)

cv2.imwrite("5_Pencil_Sketch.png", ans)