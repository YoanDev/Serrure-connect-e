import cv2
import socket
import threading
from gpiozero import LED
import RPi.GPIO as GPIO
import face_recognition
#from RPLCD.gpio import CharLCD

class MonThread1 (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        Hardware1 = Hardware()
        Hardware1.EnvoieImage()


class Hardware:

    def __init__(self):
        self.HOST = '172.20.10.4'
        self.PORT = 12345
        self.led = LED(17)
        GPIO.setmode(GPIO.BCM)
        self.capteur = 7
        GPIO.setup(self.capteur,GPIO.IN)
        #self.lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])


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
        
    def ReceptionApplication(self):
        s = socket.socket()
        self.HOST = "192.168.1.19"
        self.PORT = 12345
        s.bind((host,port))
        print("step1")
        s.listen(1)
        print(host)
  
        c, addr = s.accept()
        print("Receiving...")
        l = c.recv(1024)
        if l == b'on':
            print("open")
            return "open"
        else:
            print("close")
            return "close"
        c.close
    
    def PresenceDePersonne(self):
        if GPIO.input(capteur):
            print("mouvement")
    
    def AllumLed(self):
        self.led.on()
        
    def EtteindLed(self):
        self.led.off()

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

m1=Hardware()
m1.ReceptionApplication()
