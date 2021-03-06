import cv2
import imutils

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 300)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)

cap1 = cv2.VideoCapture(1)
cap1.set(cv2.CAP_PROP_FRAME_WIDTH, 300)
cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)


def read_frame():
    webCameShow(cap.read(), display1)
    webCameShow(cap1.read(), display2)
    # webCameShow(cap2.read(),display6)
    # webCameShow(cap3.read(),display7)
    window.after(10, read_frame)


def webCameShow(N, Display):
    _, frameXX = N
    cv2imageXX = cv2.cvtColor(frameXX, cv2.COLOR_BGR2RGBA)
    # imgtkXX = ImageTk.PhotoImage(image=imgXX) Display.imgtk = imgtkXX Display.configure(image=imgtkXX)
    imgXX = Image.fromarray(cv2imageXX)


read_frame()
webCameShow()
