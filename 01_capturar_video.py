import cv2

captura = cv2.VideoCapture(0)

while (captura.isOpened()):
    ret, video = captura.read()
    if (ret):
        video = cv2.flip(video, 1)
        cv2.imshow('Frame', video)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

captura.release()
cv2.destroyAllWindows()
