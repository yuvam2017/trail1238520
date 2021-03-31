#import cv2,os
#filename = input("Enter the filename : ")
#image = cv2.imread(f"{filename}.jpg")
#os.mkdir(f"converted/{filename}")
#grey_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#nvert = cv2.bitwise_not(grey_img)
#cv2.imwrite(f"coverted/{filename}/invert_sketch.png",invert)
#blur = cv2.GaussianBlur(invert,(21,21),0)    
#inverted_blur = cv2.bitwise_not(blur)
#sketch = cv2.divide(grey_img,inverted_blur,scale=256.0)
#cv2.imwrite(f"converted/{filename}/sketch.png",sketch)

import cv2
file = input("Enter the image path : ")
image = cv2.imread(file)
image = ~image
cv2.imwrite(f"{file}_inv.png",image)
