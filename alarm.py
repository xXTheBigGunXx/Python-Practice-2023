from playsound import playsound
import time

def alarm():

    for _ in kiekis:

        for sekunde in (minutes):
            print(sekunde)
            time.sleep(1)
        playsound("Users\matas\Desktop\projects\sound.mp3")

        for sek in (poilsis * 60):
            print(sek)
            time.sleep(1)
        playsound("Desktop\projects\sound.mp3")

minutes = (input("Minutes - "))
poilsis = (input("Sekundes - "))
kiekis = (input("Kiekis - "))
alarm()