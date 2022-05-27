import pygame
import random
import datetime
import time
import threading
from bluetooth import *

socket = BluetoothSocket( RFCOMM )
socket.connect(("블루투스 주소", 1))
print("bluetooth connected!")

data = ""

pygame.mixer.init(frequency = 44100, size = -16, channels = 1, buffer = 2**12)

channel1 = pygame.mixer.Channel(0)
channel2 = pygame.mixer.Channel(1)
channel3 = pygame.mixer.Channel(2)
channel4 = pygame.mixer.Channel(3)
channel5 = pygame.mixer.Channel(4)
channel6 = pygame.mixer.Channel(5)
channel7 = pygame.mixer.Channel(6)
channel8 = pygame.mixer.Channel(7)

musical = ["/Grandpiano", "/Harp", "/Organ",
           "/Trumpet", "/12_lines_of_guitar",
           "/Accordion", "/Vibra_phone"]



music = ["/do.wav","/re.wav", "/mi.wav", 
         "/fa.wav", "/sol.wav", "/la.wav", 
         "/si.wav", "/high_do.wav"]

print(musical)

def do_play():
    while True:
        if data == "do":
            channel1.play(do)
            time.sleep(0.5)
            data = ""
def re_play():
    
    while True:
        if data == "re":
            channel2.play(re)
            time.sleep(0.5)
            data = ""
def mi_play():
    
    while True:
        if data == "mi":
            channel3.play(mi)
            time.sleep(0.5)
            data = ""
def fa_play():
    
    while True:
        if data == "fa":
            channel4.play(fa)
            time.sleep(0.5)
            data = ""
def sol_play():
    
    while True:
        if data == "sol":
            channel5.play(sol)
            time.sleep(0.5)
            data = ""
def la_play():
    
    while True:
        if data == "la":
            channel6.play(la)
            time.sleep(0.5)
            data = ""
def si_play():

    while True:
        if data == "si":
            channel7.play(si)
            time.sleep(0.5)
            data = ""
def high_do_play():
    
    while True:
        if data == "high_do":
            channel8.play(high_do)
            time.sleep(0.5)
            data = ""

threads = []

t1 = threading.Thread(target=do_play)
t1.start()
t2 = threading.Thread(target=re_play)
t2.start()
t3 = threading.Thread(target=mi_play)
t3.start()
t4 = threading.Thread(target=fa_play)
t4.start()
t5 = threading.Thread(target=sol_play)
t5.start()
t6 = threading.Thread(target=la_play)
t6.start()
t7 = threading.Thread(target=si_play)
t7.start()
t8 = threading.Thread(target=high_do_play)
t8.start()

while True:
    lst = []
    data = socket.recv(1024)
    data = data.decode('utf-8')
    data = data.split(',')
    lst = data
    print(lst)
    if(lst[1] == '1'):
        print("check")
        break
    #print("Received: %s" %data)
    
    day = datetime.datetime.today().weekday()
    
    if day == 0 and change_st == 1:
        change_st = 0
        random.shuffle(musical)
    if day == 6 and change_st == 0:
        change_st = 1
        
    do = pygame.mixer.Sound("song"+musical[day]+music[0])
    re = pygame.mixer.Sound("song"+musical[day]+music[1])
    mi = pygame.mixer.Sound("song"+musical[day]+music[2])
    fa = pygame.mixer.Sound("song"+musical[day]+music[3])
    sol = pygame.mixer.Sound("song"+musical[day]+music[4])
    la = pygame.mixer.Sound("song"+musical[day]+music[5])    
    si = pygame.mixer.Sound("song"+musical[day]+music[6])    
    high_do = pygame.mixer.Sound("song"+musical[day]+music[7])
    if musical[day] == "/Trumpet":
        sound = 0.3
    else:
        sound = 1
        
    do.set_volume(sound)
    re.set_volume(sound)
    mi.set_volume(sound)
    fa.set_volume(sound)
    sol.set_volume(sound)
    la.set_volume(sound)
    si.set_volume(sound)
    high_do.set_volume(sound)
