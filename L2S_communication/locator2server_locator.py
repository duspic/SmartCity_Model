# main loop

import cv2
import numpy as np


def preproc(img,color):
    
    if color == 'yellow':
        lower = np.array([0,85,110])
        upper = np.array([40,255,255])
    
    img_proc = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    img_proc = cv2.inRange(img_proc,lower,upper)
    img_proc = cv2.erode(img_proc,np.ones((7,7)))
    img_proc = cv2.dilate(img_proc,np.ones((25,25)))
    
    img_proc = cv2.Canny(img_proc,254,255)
    
    return img_proc


def getID(color):
    
    if color == 'yellow':
        return 1
    

def getJetCoords(img,color='yellow'):
    
    # extracts only jetcars, based on their colored roof markers and returns a black&white image
    img_proc = preproc(img,color)
    
    # adds all columns and rows
    horizontal = img_proc.sum(axis=0)
    vertical = img_proc.sum(axis=1)
    
    # get the leftmost peak, then make it 0 to get the second one (hopefuly the rightmost)
    left = np.argmax(horizontal)
    horizontal[left] = 0
    right = np.argmax(horizontal)
    
    # get the upmost peak, then make it 0 to get the second one (hopefuly the downmost)
    up = np.argmax(vertical)
    vertical[up] = 0
    down = np.argmax(vertical)
    
    # ideally, the center should be between the 4 values values
    x = int((left+right)/2)
    y = int((up+down)/2) 
    
    ID = getID(color)
    
    return x,y,ID


def sendMsg(msg):
    # make this happen
    print(msg)



def gstreamer_pipeline(
        capture_width=3264,
        capture_height=2464,
        display_width=3264,
        display_height=2464,
        framerate=21,
        flip_method=0
        ):
    return(
            "nvarguscamerasrc! "
            "video/x-raw(memory:NVMM),"
            "width=(int)%d, height=(int)%d, "
            "format=(string)NV12, framerate=(fraction)%d/1 !"
            "nvvidconv flip-method=%d ! "
            "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
            "videoconvert ! "
            "video/x-raw, format=(string)BGR ! appsink"
            % (
                capture_width,
                capture_height,
                framerate,
                flip_method,
                display_width,
                display_height,
                )
            )




cap = cv2.VideoCapture(gstreamer_pipeline(), cv2.CAP_GSTREAMER)

while True:
    
    # frame loading
    ret, frame = cap.read()
    if ret == False:
        print("Video end!")
        break

    # main chores
    x,y,ID = getJetCoords(frame)
    msg = str(x)+','+str(y)+','+str(ID)
    sendMsg(msg)
    
    # exit strategy, (only when frames are being displayed)
    #key =  cv2.waitKey(1) & 0xFF 
    #if key == ord('q'):
    #    break
    

cap.release()
cv2.destroyAllWindows()