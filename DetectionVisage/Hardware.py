import cv2
import socket
import threading
from gpiozero import LED
#from RPLCD.gpio import CharLCD

class MonThread1 (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        Hardware1 = Hardware()
        Hardware1.EnvoieImage()

# class MonThread2 (threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#
#     def run(self):
#         Hardware1 = Hardware()
#         Hardware1.EnvoieImage()

class Hardware:

    def __init__(self):
        self.HOST = '172.20.10.4'
        self.PORT = 12345
        #self.lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])

    def detectVisage(self):
        cap = cv2.VideoCapture(0)
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        while(True):
            ret, img = cap.read()

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
                cv2.imwrite("test.png", img)
            cv2.imshow('frame', img)


            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cv2.destroyAllWindows()
        cap.release()

    def EnvoieImage(self):

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.HOST, self.PORT))
        print('Connexion vers ' + self.HOST + ':' + str(self.PORT) + ' reussie.')

        f = open('test.png', 'rb')
        print('Sending...')
        l = f.read(1024)
        while (l):
            print('Sending...')
            client.send(l)
            l = f.read(1024)
            print(len(l))

        client.shutdown(socket.SHUT_WR)

        print('Reception...')
        donnees = client.recv(1024)
        print('Recu :', donnees)

        print('Deconnexion')
        client.close()

    def AllumLed(self):
        self.led = LED(17)
        self.led.on()

    def EcritureLCD(self,message):
        try:
            self.lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])
            if message == "OK":
                self.lcd.write_string(u'Ouvert')
            elif message == "Refuse":
                self.lcd.write_string(u'Ferme')
            else:
                self.lcd.write_string(u'Patientez')
        except:
            pass 

if __name__ == '__main__':

    m1 = MonThread1()
    m1.start()
    m2 = Hardware()
    m2.detectVisage()

