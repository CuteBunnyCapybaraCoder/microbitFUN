from microbit import *
def setl(l):
    for r in range(5):
        for c in range(5):
            if r == c or r + c == 4:
                display.set_pixel(c, r, l)

brightn = 0
needto = True
while True:
    if needto == True:
        brightn += 1
        if brightn == 9:
            needto = False
    elif needto == False:
        brightn -= 1
        if brightn == 0:
            needto = True
    sleep(100)     
    setl(brightn)        
            
    
    
    
    

            