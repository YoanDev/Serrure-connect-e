from Hardware import Hardware
from detection_and_facial_recognition_2 import reco

#exemple
m1 = Hardware()
m2 = reco()

while True:
    
    #etape 1: On détecte un mouvement
    print("step0")
    x = m1.PresenceDePersonne()

    #etape 3: On lance la camera
    #etape 4: On detecte un visage
    #etape 5: On vérifie si le visage est connu
    if x == "mouvement":
        print("step1")
        y = m2.intro()
        
        #etape 6: Si le visage est connu on ouvre, sinon on demande au smartphone
        if y == "open":
            print("bravo")
            m1.AllumLed()
        else:
            try:
                print("envoie")
                m1.EnvoieImage()
            except:
                pass
            z = m1.ReceptionApplication()
            
            #etape 7: On agit selon la réponse du smartphone
            if z == "open":
                print("bravo2")
                m1.AllumLed()
            
       

