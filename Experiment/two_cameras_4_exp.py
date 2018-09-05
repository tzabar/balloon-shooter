import cv2
cap1 = cv2.VideoCapture(0)

# cap0 = cv2.VideoCapture(0)
# ret0, frame0 = cap0.read()
# assert ret0  # succeeds
while True:
    ret1, frame1 = cap1.read()
    assert ret1  # fails?!

    cv2.imshow('frame1', frame1)
    cv2.waitKey()

ret1, frame1 = cap1.read()
assert ret1  # fails?!

cv2.imshow('frame2', frame1)
cv2.waitKey()