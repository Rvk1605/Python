from pygame import*
import os

music=[]
dir_path = os.path.dirname(os.path.realpath(__file__))
for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith('.mp3'):
            music.append(str(file))


print("1.Play/Change Music || ",end="")
print("2.Pause Music || ",end="")
print("3.Resume Music")
print("4.Set Volume")
print("5.Stop")
print("6.Stop and Exit")

while(True):
    os.system("cls")
    n = int(input("\nEnter Your Choice : "))
    if n==1:
        print("\n", music)
        song = input("\nEnter Song Name From List : ")
        mixer.init()
        mixer.music.load(f"{song}.mp3")
        mixer.music.play()
    if n == 2:
        mixer.music.pause()
    elif n == 3:
        mixer.music.unpause()
    elif n == 4:
        m = float(input("Volume(0-1.0) : "))
        mixer.music.set_volume(m)
    elif n==5:
        mixer.music.stop()
    elif n == 6:
        exit()

