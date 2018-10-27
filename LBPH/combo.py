import argparse
import cv2
 
refPt = []
cropping = False
 
def click_and_crop(event, x, y, flags, param):
	
	global refPt, cropping

	if event == cv2.EVENT_LBUTTONDOWN:
		refPt = [(x, y)]
		cropping = True
 
	
	elif event == cv2.EVENT_LBUTTONUP:
		refPt.append((x, y))
		cropping = False
 
		cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
		cv2.imshow("image", image)
'''
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
'''

cap = cv2.VideoCapture(0)
 
if (cap.isOpened()== False): 
    print("Error opening video stream or file")
 
image=cv2.imread()

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('Frame',frame)
    # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    
        elif cv2.waitKey(25) & 0xFF == ord('O'):
            image=frame.copy()
            break
        
        else: 
            break

cap.release()

#image = cv2.imread(args["image"])
clone = image.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)
 
# keep looping until the 'q' key is pressed
while True:
	cv2.imshow("image", image)
	key = cv2.waitKey(1) & 0xFF
 
	# if the 'r' key is pressed, reset the cropping region
	if key == ord("r"):
		image = clone.copy()
 
	# if the 'c' key is pressed, break from the loop
	elif key == ord("c"):
		break
 
if len(refPt) == 2:
    roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
    #roi2=cv2.resize(roi,)
    cv2.imshow("ROI", roi)
    cv2.imwrite("croped.jpg",roi)
    cv2.waitKey(0)
 

cv2.destroyAllWindows()