from playsound import playsound
import time

CLEAR_AND_RETURN ="\033[H"

number_sets = int(input("How many sets?: "))
number_rest = int(input("How long is the rest?: "))

seconds_rest = number_rest *60

print("\033[2J")
before = 30
for _ in range(60):
    print(f"{CLEAR_AND_RETURN}Time left to the workout: {before}!")
    time.sleep(1)
    before-=1

while number_sets != 0:
    copy_sec_rest = seconds_rest
    playsound("Desktop/projects/sound.mp3")
    while copy_sec_rest != 0:
        time.sleep(1)
        copy_sec_rest -=1
        print(f"{CLEAR_AND_RETURN}Time left to the next set:{copy_sec_rest}!" )
    number_sets-=1
print("Work out is over!")