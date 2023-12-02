from machine import Pin, I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
import utime
import math

# Pin de la thermistance
thermistor = machine.ADC(28)

# ecran lcd 
I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16
i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

# Fonction temperature

    
while True:
    temperature_value = thermistor.read_u16()
    Vr = 3.3 * float(temperature_value) / 65535
    Rt = 10000 * Vr / (3.3 - Vr)
    temp = 1/(((math.log(Rt / 10000)) / 3950) + (1 / (273.15+25)))
    Cel = temp - 273.15
    utime.sleep(10)
    cel = str(round(Cel,1))
    lcd.backlight_on()
    lcd.move_to(0,0)
    lcd.putstr(f"La temp est de \n{cel} C")