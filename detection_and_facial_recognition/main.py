from Hardware import Hardware
from detection_and_facial_recognition_2 import reco

m1 = Hardware()
m2 = reco()
m1.SetLed()

# On demande à l'utilisateur s'il a un capteur de mouvement
val = input("Avez vous un détecteur de mouvement? Entrez o pour oui, n pour non\n")

#Le programme tourne indéfinement
while True:
    
    #etape 1: On détecte un mouvement
    x = m1.PresenceDePersonne(val)

    #etape 2: On lance la camera
    #etape 3: On detecte un visage
    #etape 4: On vérifie si le visage est connu
    if x == "mouvement":
        y = m2.intro()
        
        #etape 5: Si le visage est connu on ouvre, sinon on demande au smartphone
        if y == "open":
            print("bravo")
            m1.AllumLed()
        elif y == "Aucun visage":
            pass
        else:
            # Un try catch est utilisé pour ne pas que le programme plante en cas d'échec
            try:
                print("envoie")
                m1.EnvoieImage()
            except:
                pass
            
            # Attention, le programme se bloque jusqu'à la réception d'une image
            z = m1.ReceptionApplication()
            
            #etape 6: On agit selon la réponse du smartphone
            if z == "open":
                print("bravo2")
                m1.AllumLed()
                m2.copy_new_photo()
       

