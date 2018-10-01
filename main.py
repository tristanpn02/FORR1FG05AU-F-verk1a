##########################
# Tristan Pétur Andersen #
# 23 Ágúst 2018          #
# Æfingaverkefni 1a      #
##########################

import os
from os import system

os.system('cls')

def uppl():
    global karl
    global kona
    global drykkur
    
    karl = input('Hvað heitir karlinn? ')
    kona = input('Hvað heitir konan?' )
    drykkur = input('Hvað drekka þau? ')
    ljod()
    
def ljod():
    os.system('cls')
    global karl
    global kona
    global drykkur
    
    print(str(karl) + ' og' + str(kona) + ' eru hjón')
    print('Óttarlega mikil flón')
    print('Þau eru bæði sæt og fín')
    print('Og þau drekka ' + str(drykkur))
    
    
uppl()