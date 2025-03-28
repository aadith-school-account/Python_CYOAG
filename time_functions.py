import random, time, sys, os

def pause(msg = "Press enter to continue", delay = 0):
    #can specify msg and delay, if not specified than it will be base
    if delay > 0:
        #imported from time
        time.sleep(delay)
    input(msg)
    #built in delay lol

def countdown_timer(countdown_duration, speed):
    while countdown_duration > 0:
        # ANSI red text, reference link at start
        print("\033[0;31mTime left: " + str(countdown_duration) + " seconds\033[0m")
        time.sleep(speed)
        countdown_duration -= 1
    print("Times up!")
