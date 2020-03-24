import cv2

#print(cv2.__version__)

#reading images
#arguments-image,flag(color:1,grayscale:0,unchanged:-1(loads image as it is including alpha channel)),
#if wrong path given result of 'img' is None else result is a matrix(pixel value)
img=cv2.imread('lena.jpg',1)
#print(img)


#displaying images 
#argument- name of the window in which image will open, image var
cv2.imshow('image',img)
#to keep displaying the images, no of milliseconds for which the window should be open,if 0 given window needs to be closed
#cv2.waitKey(5000)
#to capture any key that is pressedto use 
#if using 64 bit better  to use 0xFF
k=cv2.waitKey(0) & 0xFF

if k== 27:   #k=escape key
    #destroying windows
    cv2.destroyAllWindows()

elif k==ord('s'):  # s to save the image
    #writing an image to the file
    #arguments-image file name,image var
    cv2.imwrite('lena_copy.jpg',img)
    cv2.destroyAllWindows()
    


