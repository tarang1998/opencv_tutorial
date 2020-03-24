import numpy as np
import cv2

img=cv2.imread('lena.jpg',1)

#creating an image using numpy
img=np.zeros((512,512,3),np.uint8)


#drawing line
#arguments- image, starting co-ordinates , ending co-ordinates , color  BGR, thickness
#img=cv2.line(img, (0,0) , (255,255) , (255,0,0) , 5 )
#img=cv2.arrowedLine(img, (0,0) , (255,255) , (255,0,0) , 5 )

#arguments->img,top-left vertex,bottum-right vertex, color, thickness
#if thickness == -1 rectangle filled with color
img=cv2.rectangle(img,(384,0),(510,128),(0,0,255),5)

#img,center,radius,color,thickness
img=cv2.circle(img,(447,63),63,(0,255,0),-1)

#for text
#image,ting text , starting coordinates, font ,font size,color,thickness,line type
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,"opencv",(10,500),font,4,(255,255,255),10,cv2.LINE_AA)

cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()