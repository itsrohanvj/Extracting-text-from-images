


# Extract Text from Images
------------------------------------------------------------------------
#### The code takes input of image preprocess it then tesseract process the preprocessed image to give the output.

#### First starting with break down of code:
1. Libraries :
a. cv2=OpenCV Library
b. pytesseract=Tessaract library
c. numpy=Numerical Python

2. Functions:
a. imread= Reading image from directory.
b. new_image=Like we create an empty array in similar way we can call it an empty image variable.

characteristics: Initial pixel values equal to zero
Same size and type as the original image

alpha=this value controls contrast of image.
beta=it controls brightness of image.

3. three 'for' loops= to read three values(B,G,R) per pixel of image and bring out the changes required like change in contrast.

imshow= to display the image
waitKey= to wait for user 
cvtColor= convert coloured image to B&W.
threshold= for thresholding, here I have used binary thresholding.
imwrite= to save new image.

config= defines the configuration of tesseract module.
pytesseract.image_to_string= tesseract function to extract text from processed image.

np.zeros= numpy function to create an all black image. 

puText= to relay text on image created by np.zero.

#### Work flow of program:
1. It reads the image from the directory.
2. Different preprocessing is done: Contrasting, greyscaling and thresholding to improve accuracy.
3. saving of processed image.(Not mandatory to do this step).
4. reading of processed image from directory(if saved) and if not saved we can directly call the processed image without saving it.
5. Tesseract comes in role, it extracts texts from processed image 
6. Extracted texts are displayed in image and also printed on output screen.


#### To run this code:
1. jupyter notebook(recommended)
2. modules required: cv2, tesseract, numpy.
3. make sure to add correct path of input images.
4. since image quality is high so initially it may take 10-15 seconds to load image.
5. Alternative: you can also install tesseract in system and pass your image through commmand line.
6. to pass through cmd: <file name><space> ..<output file name> -l eng 
7. the result will be in the form of txt file.
