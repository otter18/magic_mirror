#import RPi.GPIO as pin
#pin.setmode(pin.BCM)    #устанавливаем режим нумерации


import pygame
def keyPressed(inputKey):
    keysPressed = pygame.key.get_pressed()
    if keysPressed[inputKey]:
        return True
    else:
        return False
#check_on = 1
#check_off = 1
import plot_drawer_v4
plot_drawer_v4.plot_get()
plot_timer = 0
mainLoop = True

import window_drawer

window_drawer.unit()
good_word = ["Hello!", "You look nice!", "Have a good day!", "You can do it!"]

import random
word = good_word[random.randint(0, len(good_word)-1)]
while mainLoop:
    # print( datetime.datetime.today().strftime("%H:%M:%S") )
#    signal = pin.input(8)             #считываем сигнал с GPIO 8 в переменную signal
#    if signal:
#        if check_on:
#              subprocess.call("sudo /opt/vc/bin/tvservice -p",shell=True)
#              word = good_word[random.randint(0, len(good_word)-1)]
#              check_on = 0
        window_drawer.main_loop(word)
        
        if plot_timer == 10*60*60:
            plot_drawer_v4.plot_get()
            plot_timer = 0
            
        if  keyPressed(pygame.K_q):
               mainLoop = False
               
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                mainLoop = False    
                
        from time import sleep
        sleep(0.1)
        plot_timer+=1
#        check_off = 1
#    if not signal:
#        if check_off:
#            subprocess.call("sudo /opt/vc/bin/tvservice -o",shell=True)
#            check_off = 0
#        check_on = 1
pygame.quit() 





    
     














