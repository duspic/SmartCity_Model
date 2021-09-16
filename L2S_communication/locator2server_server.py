import cv2 
import numpy as np
from random import randint

#################################### PLACEHOLDER FUNCTIONS FOR LATER ########################################
def recieveMsg():
    
    x = randint(3,14)*100
    y = randint(3,9)*100
    
    return x,y,1

def getLocatorPhoto():
    
    photo = cv2.imread("slika0.jpg")
    
    return photo

def extractMap(photo):
    
    MAP = cv2.imread("mapa.png")
    
    return MAP



#################################### REAL FUNCTIONS IN USE CURRENTLY ########################################

# to know which jetcar is being traced, each ID is connected to its roof-marker color
def getColor(ID):
    
    if ID == 1:
        return [0,255,255]
    
    

# coordinates recieved are extracted from a wide-angle lens camera. They need to be adjusted accordingly (un-fisheyed)    
def undistortCoords(x,y):

    # makes an image with one white px, and un-distorts it
    img = np.zeros((2464,3264,3))
    img[y-1:y+1,x-1:x+1,:] = [255,255,255]
    img = undistort(img)
    
    #finds the position of the white px
    img = img[:,:,0]
    horizontal = img.sum(axis=0)
    vertical = img.sum(axis=1)
    
    x = np.argmax(horizontal)
    y = np.argmax(vertical)
    
    return x,y
    
    
    
def visualizeMarker(x,y,ID):
    
    x,y = undistortCoords(x,y)
    
    color = getColor(ID)
    marker = np.zeros_like(MAP)
    marker[y-5:y+5,x-5:x+5,:] = color
    
    return marker, x,y



def undistort(img, balance=1, dim2=(816,616), dim3=(1632,1332)):
    
    K=np.array([[403.5072678987361, 0.0, 390.5537285576421], [0.0, 403.056903943273, 303.0726428457018], [0.0, 0.0, 1.0]])
    D=np.array([[-0.02877771348636789], [-0.012216466999853827], [0.020949602322686396], [-0.015176688869367766]])
    

    dim1 = img.shape[:2][::-1]  #dim1 is the dimension of input image to un-distort
    assert dim1[0]/dim1[1] == dim2[0]/dim2[1], "Image to undistort needs to have same aspect ratio as the ones used in calibration"
    if not dim2:
        dim2 = dim1
    if not dim3:
        dim3 = dim1
    scaled_K = K * dim1[0] / dim2[0]  # The values of K is to scale with image dimension.
    scaled_K[2][2] = 1.0  # Except that K[2][2] is always 1.0
    
    # This is how scaled_K, dim2 and balance are used to determine the final K used to un-distort image. OpenCV document failed to make this clear!
    new_K = cv2.fisheye.estimateNewCameraMatrixForUndistortRectify(scaled_K, D, dim2, np.eye(3), balance=balance)
    map1, map2 = cv2.fisheye.initUndistortRectifyMap(scaled_K, D, np.eye(3), new_K, dim3, cv2.CV_16SC2)
    return cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)








photo = getLocatorPhoto() #FTTP
photo = undistort(photo)
MAP = extractMap(photo)

while True:
    
    x,y,ID = recieveMsg()
    marker,x,y = visualizeMarker(x,y,ID)
    
    cv2.imshow("Map with marker(s):",marker+MAP)
    cv2.waitKey(1)
    print(x,y,end='\r')
cv2.destroyAllWindows()
    