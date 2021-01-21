import time
import random
import os
import subprocess
os.system("say 'program started'")
time.sleep(0.5)
os.system("say 'Merry Christmas'")
count = 0
list = ['31', '6', '16', '19', '7', '32', '10', '30', '33', '5', '21', '15', '1', '24', '20', '4', '17', '23', '9', '3', '25', '11', '29', '13', '14', '18', '26', '27', '2', '28', '22', '12', '8']
random.shuffle(list)
while True:
    A = input("Press Enter For Gift Number> ")
    if A == "":
        giftint = random.choice(list)
        print("\n" + giftint+ "\n")
        os.system("say '" + giftint + "'")
        list.remove(giftint)
        count += 1
        #print(count)
        #if count == 15:
            #os.system('say "Halfway through"')
        if count == 15:
            audio_file = "elf-son-of-a-nutcracker.mp3"
            return_code = subprocess.call(["afplay", audio_file])
        if count == 29:
            audio_file = "elf-christmas-gram.mp3"
            return_code = subprocess.call(["afplay", audio_file])
        if count == 33:
            time.sleep(1)
            os.system("say 'All gifts have been opened'")
            time.sleep(0.5)
            audio_file = "jinglebells.mp3"
            return_code = subprocess.call(["afplay", audio_file])
            break
