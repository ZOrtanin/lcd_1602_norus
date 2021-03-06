import lcddriver2
from gpiozero import CPUTemperature
import datetime
from time import sleep
import os
import socket

lcd = lcddriver2.lcd()

# lcd.lcd_clear()
# lcd.lcd_display_string("Pogoda A",1)
# lcd.lcd_display_string("20" + "C",2)

# sleep(2)
#lcd.lcd_clear()

font_rus = [
        ['А',[0x0E,0x11,0x11,0x11,0x11,0x1F,0x11,0x11]],
        ['а',[0x00,0x0E,0x01,0x01,0x0F,0x11,0x11,0x0F]],
]

fontdata_all = [
        # Смайлик 
        [0x00,0x06,0x04,0x00,0x08,0x07,0x00,0x00],
        [0x00,0x0C,0x04,0x00,0x02,0x1C,0x00,0x00],

        # Туча
        [0x01,0x06,0x0A,0x10,0x10,0x0F,0x00,0x00],
        [0x18,0x04,0x06,0x09,0x01,0x1E,0x00,0x00],

        # Туча с дождем
        [0x01,0x06,0x0A,0x10,0x10,0x0F,0x00,0x0A],
        [0x18,0x04,0x06,0x09,0x01,0x1E,0x00,0x14],

        # Солнце 
        [0x04,0x01,0x03,0x0B,0x03,0x01,0x04,0x00],
        [0x04,0x10,0x18,0x1A,0x18,0x10,0x04,0x00],

        # Луна
        [0x00,0x09,0x02,0x06,0x06,0x02,0x01,0x10],
        [0x00,0x12,0x08,0x00,0x00,0x08,0x12,0x00],

]

fontdata1 = [
        # Char 0 - Upper-left
        [0x1f,0x11,0x11,0x11,0x11,0x11,0x11,0x0],# П        
        [0x0,0x0,0x1e,0x10,0x10,0x10,0x10,0x0],# г
        [0x0,0x0,0xe,0xa,0xa,0xa,0xf,0x11],# д         
]

for x in range(len(fontdata_all)):
    if x % 2 == 0:
        print(x)
        if x != 0:
            fontdata1.pop(-1)
            fontdata1.pop(-1)
        fontdata1.append(fontdata_all[x])
        fontdata1.append(fontdata_all[x+1])

    lcd.lcd_load_custom_chars(fontdata1)

    # Write first three chars to row 1 directly
    # lcd_display_string()
    lcd.lcd_clear()
    lcd.lcd_write(0x80)
    lcd.lcd_write_char(0)
    

    # #lcd.lcd_write(0x0B)
    # lcd.lcd_write(203,0b00000001)
    # lcd.lcd_write(int(0b0011011111),0b00000001)
    # lcd.lcd_write(int(0b0011110100),0b00000001)
    # print(ord('a')) 
    
    # Write next three chars to row 2 directly
    lcd.lcd_write(0xC0)
    #lcd.lcd_write(182,0b00000001)
    lcd.lcd_write_char(3)
    lcd.lcd_write_char(4)
    # lcd.lcd_write_char(10)

    sleep(2)





# Солнце
# [0x00,0x00,0x02,0x00,0x0D,0x09,0x03,0x03],
# [0x04,0x0E,0x00,0x1F,0x1F,0x00,0x00,0x00],
# [0x00,0x00,0x08,0x00,0x16,0x12,0x18,0x18],        
# [0x03,0x03,0x09,0x0D,0x00,0x02,0x00,0x00],
# [0x00,0x00,0x00,0x1F,0x1F,0x00,0x0E,0x04],
# [0x18,0x18,0x12,0x16,0x00,0x08,0x00,0x00],   

# [0x00,0x00,0x00,0x00,0x00,0x01,0x06,0x00],
# [0x03,0x03,0x13,0x13,0x06,0x06,0x0C,0x18],
# [0x0E,0x00,0x00,0x0C,0x02,0x00,0x10,0x0C],
# [0x1F,0x1E,0x00,0x00,0x12,0x12,0x11,0x00],
# [0x01,0x00,0x08,0x08,0x04,0x04,0x00,0x00],
# [0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00],

# #Солнце 2х3
# [0x00,0x00,0x08,0x04,0x00,0x01,0x19,0x03],
# [0x11,0x11,0x00,0x0E,0x1F,0x1F,0x1F,0x1F],
# [0x00,0x00,0x02,0x04,0x00,0x10,0x13,0x18],
# [0x03,0x19,0x01,0x00,0x04,0x08,0x00,0x00],
# [0x1F,0x1F,0x1F,0x1F,0x0E,0x00,0x11,0x11],
# [0x18,0x13,0x10,0x00,0x04,0x02,0x00,0x00],


# [0x10,0x02,0x09,0x05,0x00,0x09,0x13,0x17],
# [0x11,0x10,0x12,0x04,0x00,0x10,0x19,0x1C],
# [0x01,0x10,0x08,0x04,0x02,0x0A,0x10,0x02],
# [0x07,0x03,0x09,0x10,0x01,0x04,0x09,0x11],
# [0x1C,0x19,0x10,0x04,0x12,0x00,0x00,0x0F],
# [0x04,0x04,0x10,0x00,0x04,0x08,0x10,0x00]
