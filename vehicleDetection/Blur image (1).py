import cv2
img = cv2.imread(r"C:\Users\P.Dhanashreenydhi\Desktop\SIH\blur images\blur4.jpeg",cv2.IMREAD_GRAYSCALE)
laplacian_var = cv2.Laplacian(img, cv2.CV_64F).var()
if laplacian_var < 30:
    print("Image blurry")
else:
    print("Not blurry")

print(laplacian_var)

# cv2.imshow("Img", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
