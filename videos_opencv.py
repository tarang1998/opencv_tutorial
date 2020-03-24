import cv2

#arguments- filename('myfile.mp4') or device index of camera  index={-1,0,1,2}
cap=cv2.VideoCapture(0)

#to save the video captured
#???????????????????????????????????
fourcc=cv2.VideoWriter_fourcc('X','V','I','D')
#arguments-filename,fourcc code,FPS,size
out=cv2.VideoWriter('output.avi',fourcc,20,(640,480))

#create a while loop to capture frames continously

#in case of file --> while(cap.isOpened()) --(would be false if file path is wrong or the index provided is wrong  )
#while(True):
while(cap.isOpened()):
    #cap.read will return true if frame is available and frame saved in frame variable
    ret,frame=cap.read()

    #checking if frame is present
    if ret==True:

        #to find properties of the frame
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


        out.write(frame)

        #cv2.imshow('Frame',frame)

        #to display images in grey scale format
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('Frame',gray)


        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break

    else:
        break

#to release resources
cap.release()
out.release()
cv2.destroyAllWindows()