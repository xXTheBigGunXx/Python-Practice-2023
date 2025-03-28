import time
import datetime
from playsound import playsound

CLEAR = "\033[2J"
CLEAR_AND_RETURN ="\033[H"

place_holder = datetime.datetime.now()
time_now = f"{place_holder:%H:%M:%S}"
users_input = input(str("Set allarm clock to : (HH/MM/SS)  "))
print(CLEAR)
while str(time_now) != str(users_input):
    inside_loop = datetime.datetime.now()
    time_now = f"{inside_loop:%H:%M:%S}"
    print(f"{CLEAR_AND_RETURN}{time_now} - laikas dabar.")
playsound("Desktop/projects/alarm_sound.mp3")
time.sleep(30)



