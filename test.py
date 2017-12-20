from math import sqrt
import imutils
import cv2

def detectCars(img):
    cascade_src = 'cars.xml'
    car_cascade = cv2.CascadeClassifier(cascade_src)
    if (type(img) == type(None)):
        break
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
    return cars
# cars is an multidimensional array of x, y, w, h 
# ye function se ek image ka sab cars detect hota hai, aur uska co-ordinates store hota hai
# cars = detectCar(frame) <-- normal image pass 
# for (x, y, w, h) in cars:
#    idhar calculation

def validateParking(parking, car):
    x, y, w, h = car
    x2, y2, w2, h2 = parking
    if(x > x2 and y < y2 and x+w > x2 + w2 and y+h < y2+h2 ):
        return 1
    return 0


def makeRed(parking, img):
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    return img

def handleInvalidation(parking, car):
    x, y, _, _ = car
    x2, y2, _, _ = parking
    return (x2-x), (y2-y)


def motionDetect(normal, test):
    normal = imutils.resize(normal, width=500)
    test = imutils.resize(test, width=500)
	test = cv2.cvtColor(test, cv2.COLOR_BGR2GRAY)
	test = cv2.GaussianBlur(test, (21, 21), 0)
    normal = cv2.cvtColor(normal, cv2.COLOR_BGR2GRAY)
	normal = cv2.GaussianBlur(normal, (21, 21), 0)
    frameDelta = cv2.absdiff(firstFrame, gray)
	thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)
	(cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
    if cnts:
        return 1
    return 0
 

def getDistance(D, h, k, x4, x3, yt, yb, x2, x1):
    return sqrt(((x4-x3)*(yt-yb)*(sqrt(D*D+h*h))/((x2-x1)*(k-yb))-((x4-x3)*(k-yt)))-(h*h))
        
        
        
        
        
    