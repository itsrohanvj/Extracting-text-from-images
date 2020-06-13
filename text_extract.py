import numpy as np
import cv2
import pytesseract

#reading of image
image = cv2.imread('C:\\Users\\Rohan\\Desktop\\pan.jpg')

if image is None:
    print('Could not open or find the image: ')
    exit(0)

new_image = np.zeros(image.shape, image.dtype)
alpha = 1.4 # contrast control
beta = 0    # brightness control

print('OUTPUT BEGINS')
print('-------------------------')

#see readme file for explanation.
for y in range(image.shape[0]):
    for x in range(image.shape[1]):
        for c in range(image.shape[2]):
            new_image[y,x,c] = np.clip(alpha*image[y,x,c] + beta, 0, 255)
            
#displaying cintrasted image.
cv2.imshow('Contrast', new_image)
cv2.waitKey(0) 

#grayscaling contrasted image
gray_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)

#thresholding image
ret,thresh1 = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('Threshold Binary', thresh1)
cv2.waitKey(0) 
#saving image
cv2.imwrite('C:\\Users\\Rohan\\Desktop\\pan2.jpg',thresh1)
cv2.waitKey(0)

#tesseract configuration
config = ('-l eng --oem 1 --psm 3')
 
  # Read image from disk
im = cv2.imread('C:\\Users\\Rohan\\Desktop\\pan2.jpg', cv2.IMREAD_COLOR)
 
  # tesseract OCR on image
text = pytesseract.image_to_string(im, config=config)
print(text)

# Create a black image
img = np.zeros((1924,1024,3), np.uint8)
  
text3=repr(text2)
font                   = cv2.FONT_HERSHEY_COMPLEX
bottomLeftCornerOfText = (10,50)
fontScale              = 1
fontColor              = (255,255,255)
lineType               = 2

# Print each line. 
cv2.putText(img,text, 
    bottomLeftCornerOfText, 
    font, 
    fontScale,
    fontColor,
    lineType)

#Display the image
cv2.imshow("img",img)

#Save image
cv2.imwrite("out.jpg", img)

cv2.waitKey(0)
cv2.waitKey()
cv2.destroyAllWindows()
