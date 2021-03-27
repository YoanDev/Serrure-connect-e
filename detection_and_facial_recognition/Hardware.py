import cv2
import socket
import threading
from gpiozero import LED
import RPi.GPIO as GPIO
import face_recognition
import time

#from RPLCD.gpio import CharLCD


class Hardware:

    def __init__(self):
        self.HOST = '192.168.43.82'
        self.PORT = 12345
        self.led = LED(17)
        
        #self.lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])


    def EnvoieImage(self):
        host = '192.168.43.94'
        port = 1234
        client = socket.socket()
        client.connect((host, port))
        print('Connexion vers ' + host + ':' + str(port) + ' reussie.')

        f = open('known_faces/test.png', 'rb')
        print('Sending...')
        l = f.read(1024)
        while (l):
            print('Sending...')
            client.send(l)
            l = f.read(1024)
            print(len(l))

        client.shutdown(socket.SHUT_WR)

        print('Deconnexion')
        client.close()
        
    def ReceptionApplication(self):
        print("reception")
        s = socket.socket()
        s.bind((self.HOST,self.PORT))
        s.listen(1)
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
        GPIO.setmode(GPIO.BCM)
        capteur = 7
        GPIO.setup(capteur,GPIO.IN)
        time.sleep(10)
        while True:
            time.sleep(0.1)
            if GPIO.input(capteur):
                print("mouvement")
                return "mouvement"
            else:
                print("No mouv")
                
            #time.sleep(0.5)
        
    
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


