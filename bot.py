import pyautogui
import time
import random
#if you want to get fancy, help me out and make a pull request to also check for weeks and months, altho nobody will be running this script for that long(probably)
import datetime

runTime=0

#type and enter
def write(ni):
    pyautogui.typewrite(ni)
    pyautogui.hotkey('enter')

while True:
    #this goes first, so you don't have to have move your mouse as fast as fuck
    sleepTime = random.randint(40, 49) + random.random()
    #keeps track of how much time this shitty script has been running
    runTime+=sleepTime

    time.sleep(sleepTime)
    #list of commands
    #remove pls search for no chance of risk, pls search can get you killed according to the docs
    list = ["pls fish", "pls hunt", "pls dig", "pls beg", "pls pm", "pls dep all", "pls highlow", "pls search"]
    #shuffles, there are 40320 combos, so you shouldn't run out for a while
    random.shuffle(list)

    #check for daily
    #because let's face it, our functions aren't running on a 50000 dollar mac pro x mega ultra with i420 cores and 69 cpus
    dayTime=60*60*24+5
    rrTime=round(runTime)
    if rrTime>dayTime:
        write('pls daily')


    #this types everything out
    for i in list:
        #typing out the command
        write(i)
        #choiciing the memes
        if i=="pls pm":
            pmWaitTime=random.randint(1,5)+random.random()
            runTime+=pmWaitTime
            time.sleep(pmWaitTime)
            write(random.choice(['f','r','i','c','k']))

        #gambling for highlow
        if i=="pls highlow":
            highlowWaitTime=random.randint(1,6)+random.random()
            runTime+=highlowWaitTime
            time.sleep(pmWaitTime)
            write(random.choice(["high", "low", "jackpot"]))

        waitTime=random.randInt(1,7)+random.random()
        runTime+=waitTime
        time.sleep(waitTime)
