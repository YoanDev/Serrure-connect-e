import cv2

class Hardware:

    def detectVisage(self):
        cap = cv2.VideoCapture(0)
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        while(True):
            ret, img = cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)

            cv2.imshow('frame', img)

        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    Hardware1 = Hardware()
    Hardware1.detectVisage()