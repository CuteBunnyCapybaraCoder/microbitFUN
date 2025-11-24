from microbit import *
import music
while True:
    if microphone.current_event() == SoundEvent.LOUD:
        sleep(100)
        if microphone.current_event() == SoundEvent.QUIET:
            sleep(200)
            music.play(['c','g','d','a' ])