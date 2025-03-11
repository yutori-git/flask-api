
import time
import random
from playsound import playsound 
from mutagen.mp3 import MP3 as mp3
#playlist = ["a12.mp3", "a54.mp3", "ab0.mp3", "c0.mp3", "fx2.mp3", "y0.mp3", "yori0.mp3", "yotte0.mp3", "yotte1.mp3"]
#playsound(random.choice(playlist))
#playlist = ["サンプル２.mp3", "サンプル３.mp3", "サンプル４.mp3"]
#random.shuffle(playlist)
playlist = ["ソザイ１.mp3", "ソザイ２.mp3", "ソザイ３.mp3", "ソザイ４.mp3"]
r = 28800
for i in range(r):
    n = i + 1
    print(n, "回目の再生")
    p = random.choice(playlist)
    print(p)
    playsound(p)
    """
    playsound(p)
    mc = mp3(p).info.length
    random.shuffle(playlist)
    #time.sleep(mc)

for p in playlist:
    #playsound(random.choice(playlist))
    #random.shuffle(playlist)
    playsound(p)
    #mc = mp3(p).info.length
    #time.sleep(mc)



random.shuffle(playlist)
for p in playlist:
    playsound(p)
    mc = mp3(p).info.length
    #time.sleep(mc)


for p in playlist:
    playsound(p)
    mc = playsound(p).info.length
    time.sleep(mc + 0.5)
from mutagen.mp3 import MP3 as mp3
audio = mp3("サンプル２.mp3").info.length
print (audio)

from playsound import playsound 
playsound("サンプル３.mp3")
"""