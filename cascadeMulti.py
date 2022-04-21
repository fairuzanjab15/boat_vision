
import cv2

BolaMerah = cv2.CascadeClassifier("merah1.xml")
#BolaHijau = cv2.CascadeClassifier("hijau3.xml")
BolaKuning = cv2.CascadeClassifier("kuning3.xml")
# faceCascade = cv2.CascadeClassifier("Resources/haarcascade_russian_plate_number.xml")

# #### IMAGE CAPTURE ####
#
# img = cv2.imread('Resources/lena.png')
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
#
# for (x, y, w, h) in faces:
#     cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
#
# cv2.imshow("Result", img)
# cv2.waitKey(0)



### VIDEO CAPTURE ####

# cap = cv2.VideoCapture("Resources/pedestrian2.mp4")
cap = cv2.VideoCapture(0)
cap.set(3,352)
cap.set(4,240)
cap.set(10, 300)
while cap.isOpened():
    success, img = cap.read()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    Merah = BolaMerah.detectMultiScale(imgGray, 1.1, 4)
  #  Hijau = BolaHijau.detectMultiScale(imgGray, 1.1, 4)
    Kuning = BolaKuning.detectMultiScale(imgGray, 1.1, 4)


    for (x, y, w, h) in Merah:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        lebar = str(w)
        tinggi = str(h)
        cv2.putText(img, lebar, (x + (w//2) - 10, y), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 0), 2)
        cv2.putText(img, tinggi, (x + w, y + (y//2) + 10), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 0), 2)
     
    #for (x, y, w, h) in Hijau:
    #    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #    lebar = str(w)
    #    tinggi = str(h)
    #    cv2.putText(img, lebar, (x + (w//2) - 10, y), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 0), 2)
    #    cv2.putText(img, tinggi, (x + w, y + (y//2) + 10), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 0), 2)
        
       
    for (x, y, w, h) in Kuning:
        cv2.rectangle(img, (x, y), (x + w, y + h), ( 15, 253, 250), 2)
        lebar = str(w)
        tinggi = str(h)
        cv2.putText(img, lebar, (x + (w//2) - 10, y), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 0), 2)
        cv2.putText(img, tinggi, (x + w, y + (y//2) + 10), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 0), 2)
      
        
    cv2.imshow("Video",img)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
