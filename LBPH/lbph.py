import cv2
import numpy as np

def detectFace(img):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face_cascade=cv2.CascadeClassifier("E:/opencv/build/etc/haarcascades/haarcascade_frontalface_default.xml")
    faces=face_cascade.detectMultiScale(gray,scaleFactor=1.2, minNeighbors=5)
    x,y,w,h=faces[0]
    return gray[y:y+w,x:x+h],faces[0]

def draw_rectangle(img, rect):
    (x, y, w, h) = rect
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

image_test=cv2.imread("C:/Users/Atharva/Pictures/Camera Roll/WIN_20181009_20_11_54_Pro.jpg")
image_test=cv2.resize(image_test,(int(image_test.shape[1]/2),int(image_test.shape[0]/2)))
face_extract,rect=detectFace(image_test)
labels=[]
labels.append(1)
labels.append(2)


draw_rectangle(image_test, rect)
image_train_1=cv2.imread("croped1.jpg")
image_train_1=cv2.resize(image_train_1,(100,100))
image_train_gray_1=cv2.cvtColor(image_train_1,cv2.COLOR_BGR2GRAY)

image_train_2=cv2.imread("croped2.jpg")
image_train_2=cv2.resize(image_train_2,(100,100))
image_train_gray_2=cv2.cvtColor(image_train_2,cv2.COLOR_BGR2GRAY)

faces=[]
faces.append(image_train_gray_1)
faces.append(image_train_gray_2)
cv2.imshow("test",image_test)
#cv2.imshow("train",image_train)

#face_recognizer = cv2.face.createLBPHFaceRecognizer()
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.train(faces, np.array(labels))

label_res= face_recognizer.predict(face_extract)
print(label_res)

cv2.waitKey(0)
cv2.destroyAllWindows()