import cv2
import time

def take_photo():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Kamera başlatılamadı!")
        return
    ret, frame = cap.read()
    if ret:
        timestamp = time.time()
        photo_name = f"phote.jpg"
        cv2.imwrite(photo_name, frame)
    else:
        print("Fotoğraf çekilemedi!")
    cap.release()

if __name__ == "__main__":
    while True:
        take_photo()
        time.sleep(60)
