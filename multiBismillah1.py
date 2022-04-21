from turtle import width
import cv2

"""
mendefinisikan titik tengah dari layar
titik tengah ini dijadikan titik utama tengah
"""

#mendefiniskan kamera & ukuran layar
# cap is variable berisi fungsi kamera
cap = cv2.VideoCapture(0)
cap.set(width,640) #width
cap.set(height,240) #height
cap.set(10, 300)

#supaya windows kameranya muncul maka harus di ulang dengan while
#while cap.isOpened():
while True:
    success, img = cap.read()
    cv2.imshow("Video",img)

    if cv2.waitKey(1) == ord('x'):
         break #& 0xFF

#mengurusi titik tengah
for (x, y, w, h) in Tengah:
    lebar = str(w)
    tinggi = str(h)
    

#agar dapat digunakan oleh aplikasi lain
cap.release()