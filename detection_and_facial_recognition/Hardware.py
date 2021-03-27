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
        
        self.LED = LED(17)
        self.PORT = 1234

    # Cette méthode permet d'envoyer une photo au smartphone via TCP
    def EnvoieImage(self):
        host = '192.168.1.11'
        client = socket.socket() # On ouvre le tunel
        client.connect((host, self.PORT)) # On connecte le tunel au port

        f = open('new_faces/test.png', 'rb')
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
        
    # Cette méthode permet de recevoir une réponse du smartphone via TCP
    def ReceptionApplication(self):
        host = '192.168.1.19'
        print("reception...")
        s = socket.socket() # On ouvre le tunel
        s.bind((host,self.PORT)) # On connecte le tunel au port
        s.listen() # On écoute si un client essaie de se connecter
        
        c, addr = s.accept()
        print("Receiving...")
        l = c.recv(1024) # On recoit le message du smartphone
        if l == b'on':
            print("open")
            return "open"
        else:
            print("close")
            return "close"
        c.close
    
    #Cette fonction permet de récupérer les informations du capteurs de mouvement
    def PresenceDePersonne(self,val):
        GPIO.setmode(GPIO.BCM)
        capteur = 7
        GPIO.setup(capteur,GPIO.IN)
        time.sleep(10)     
        while True:
            time.sleep(0.1)
            
            # Le capteur retourne 1 si mouvement
            if GPIO.input(capteur):
                print("mouvement")
                return "mouvement"
            elif val== "n":
                return "mouvement"
            else:
                print("No mouv")
                
            #time.sleep(0.5)
        
    # Cette fonction permet d'allumer une LED
    def AllumLed(self):
        GPIO.setmode(GPIO.BCM)                                                        
        GPIO.setup(2, GPIO.OUT)
        GPIO.output(2, GPIO.HIGH) # On allume
        time.sleep(10)                 
        GPIO.output(2, GPIO.LOW) # On éteint
        
    # Cette fonction permet d'initialiser l'état de LED pour qu'elle soit éteinte
    def SetLed(self):
        GPIO.setmode(GPIO.BCM)                                                        
        GPIO.setup(2, GPIO.OUT)                
        GPIO.output(2, GPIO.LOW) # On éteint
        
    # Cette fonction permet d'écrire un message sur un écran LCD
    # Le matériel n'a pas été mis en place
    # Cette fonction n'a jamais été testé
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


