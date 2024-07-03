import cv2 as cv

capture=cv.VideoCapture('video/video.mp4')

while True:
    #frame by frame
    isTrue,frame=capture.read()

    cv.imshow('Video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        #end of frames
        break
#release the capture pointer

capture.release()

cv.destroyAllWindows()
cv.waitKey(0)
