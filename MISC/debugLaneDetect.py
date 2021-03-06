from laneDetection import *
from rpistream import *


def makeImg(cam, dF, scale):
    image = cv2.resize(cam.image,(0,0),fx=scale,fy=scale)
    #return (dF.process3(image)).astype("uint8")
    return Ld.process4(image)

Ld= LaneDetector() #needs more params
cam=camera.Camera()
scale=0.5

p=ColorProfile.lanes
#cv2.imread("calib.png")#
calibImg = Ld.getCalibImage(cam)
res=Ld.calibrateKmeans(calibImg, p, debug=True)
#Ld.loadSvm("model.pkl") #NOT VIABLE DIFF PICKLE PROTOCOL


server = streamserver.Server(port=5000)
server.serve() # Blocking; waits for a connection before continuing
server.startStream(makeImg,[cam, Ld, scale]) # Calls retrieveImage(*args) every frame  
