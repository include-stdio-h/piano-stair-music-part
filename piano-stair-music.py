import os
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pygame
import random
import datetime
import time
import threading
from bluetooth import *

socket = BluetoothSocket(RFCOMM)
socket.connect(("98:D3:71:F9:6A:40", 1))
print("bluetooth connected!")

pygame.mixer.init(frequency=44100, size=-16, channels=1, buffer=2 ** 12)

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

music = ["/do.wav", "/re.wav", "/mi.wav",
         "/fa.wav", "/sol.wav", "/la.wav",
         "/si.wav", "/high_do.wav"]

print(musical)

data = ''

status = 0
status1 = 0
status2 = 0
status3 = 0
status4 = 0
status5 = 0
status6 = 0
status7 = 0

def do_play():
    while True:
        global status
        while not(status == 1):
            if lst[1] == '1':
                channel1.play(do)
                status = 1
                time.sleep(0.08)
            else:
                print("no")
                status = 0
                time.sleep(0.08)

def re_play():
    while True:
        global status1
        while not(status1 == 1):
            if (lst[3] == '1'):
                channel2.play(re)
                status1 = 1
                time.sleep(0.08)
            else:
                print("no1")
                status1 = 0
                time.sleep(0.08)
        


def mi_play():
    while True:
        global status2
        while not(status2 == 1):
            if (lst[5] == '1'):
                channel3.play(mi)
                status2 = 1
                time.sleep(0.08)
            else:
                print("no2")
                status2 = 0
                time.sleep(0.08)
        

def fa_play():
    while True:
        global status3
        while not(status3 == 1):
            if (lst[7] == '1'):
                channel4.play(fa)
                status3 = 1
                time.sleep(0.08)
            else:
                print("no3")
                status3 = 0
                time.sleep(0.08)
        


def sol_play():
    while True:
        global status4
        while not(status4 == 1):
            if (lst[9] == '1'):
                channel5.play(sol)
                status4 = 1
                time.sleep(0.08)
            else:
                print("no4")
                status4 = 0
                time.sleep(0.08)
            


def la_play():
    while True:
        global status5
        while not(status5 == 1):
            if (lst[11] == '1'):
                channel6.play(la)
                status5 = 1
                time.sleep(0.08)
            else:
                print("no5")
                status5 = 0
                time.sleep(0.08)
        


def si_play():
    while True:
        global status6
        while not(status6 == 1):
            if (lst[13] == '1'):
                channel7.play(si)
                status6 = 1
                time.sleep(0.08)
            else:
                print("no6")
                status6 = 0
                time.sleep(0.08)
        


def high_do_play():
    while True:
        global status7
        while not(status7 == 1):
            if (lst[15] == '1'):
                 channel8.play(high_do)
                status7 = 1
                time.sleep(0.08)
            else:
                print("no7")
                status7 = 0
                time.sleep(0.08)


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
    for i in socket.recv(1024):
        i = i.encode('utf-8')
        data += i
        if i == ']':
            data = list(data)
            print(data)
            data = ''
            time.sleep(0.08)
    day = datetime.datetime.today().weekday()

    if day == 0 and change_st == 1:
        change_st = 0
        random.shuffle(musical)
    if day == 6 and change_st == 0:
        change_st = 1

    do = pygame.mixer.Sound("song" + musical[day] + music[0])
    re = pygame.mixer.Sound("song" + musical[day] + music[1])
    mi = pygame.mixer.Sound("song" + musical[day] + music[2])
    fa = pygame.mixer.Sound("song" + musical[day] + music[3])
    sol = pygame.mixer.Sound("song" + musical[day] + music[4])
    la = pygame.mixer.Sound("song" + musical[day] + music[5])
    si = pygame.mixer.Sound("song" + musical[day] + music[6])
    high_do = pygame.mixer.Sound("song" + musical[day] + music[7])
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
