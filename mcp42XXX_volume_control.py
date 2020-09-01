#!/usr/bin/python

import alsaaudio as audio
import spidev
import time

scanCards = audio.cards()
print("cards: ",scanCards)
for card in scanCards:
    scanMixers = audio.mixers(scanCards.index(card))
    print('mixers: ',scanMixers,' card_index: ',scanCards.index(card))
spi = spidev.SpiDev()
old_output = 0
current_volume = [0]
while True:
    m = audio.Mixer('PCM')
    
    resistor_output = 255-round((2.5*(4*math.sqrt(x))/100*255))
    if old_output != resistor_output:
        print('resistor_output ',resistor_output)
        print('current_volume ',current_volume[0])
        spi.open(0,0)
        spi.max_speed_hz = 1000000
        spi.xfer([0x13,resistor_output])
        spi.close()
    current_volume = m.getvolume()
    old_output = resistor_output


    #time.sleep(1)
