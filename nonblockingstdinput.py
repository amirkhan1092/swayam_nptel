
import keyboard  # using module keyboard
import time

keys = [
    "down arrow",
    "up arrow",
    "left arrow",
    "right arrow",
    "w",
    "s",
    "a",
    "d",
    "1",
    "2",
    "3",
    "4",
    "q",
    "e",
    "f"
]

value = 0
while True:
    if keyboard.is_pressed('right arrow'):
##        print(keyboard.key_to_scan_codes('right arrow'))
        value += 1
    elif  keyboard.is_pressed('left arrow'):
##        print(keyboard.key_to_scan_codes('left arrow'))
        value -= 1

##    print(value )
    print(' '*value+'*')
    
    time.sleep(0.02)
    
        
        
##            for key in keys:
##                if keyboard.is_pressed(key):
##                    print(keyboard.key_to_scan_codes(key))
##                    print(f"{key} pressed")
##                   
##                else:
##                    pass
##
##            if keyboard.is_pressed('esc'):
##                print(key + " pressed")
                

            
