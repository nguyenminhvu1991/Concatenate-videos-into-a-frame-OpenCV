#Reference:
#http://answers.opencv.org/question/200077/combine-several-videos-in-the-same-window-python/

import numpy as np
import cv2

cap = cv2.VideoCapture('path-to-video-1')  
cap2 = cv2.VideoCapture('path-to-video-2')

while(cap.isOpened()):
    r1, f1 = cap.read()     # read the first video
    r2, f2 = cap2.read()     # read the second video
    
    if r1 == True and r2 == True: # you *have* to check *both* captures ! 
        h,w,c = f1.shape
        h,w,c
        h2, w2, c2 = f2.shape
        h2, w2, c2 # check and see that f1 <f2
        if h != h2 or w != w2: # resize right img to left size
            f1 = cv2.resize(f1,(w2,h2)) #note the order of w2 and h2
            f1.shape
            both = np.concatenate((f1, f2), axis=1)   # concatenate the videos
            cv2.imshow('Frame', both)     # show the frames
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    else: 
        break
    
cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()



