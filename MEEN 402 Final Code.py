import RPi.GPIO as GPIO
import time as t
from datetime import datetime
import csv
import os
import dweepy
#Setup of pin numbering system and pull doen resistors
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setwarnings(False)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)

def main():
    z = [8,10,12,16,18,22]
    x = [11,13,15,29,31,37]
    csv_file = 'Data_' + str(datetime.now().strftime('%Y_%m_%d_%H_%M'))+'.csv'
    q, f, g = 1, 2, 3
    y = [0,0,0,0,0,0,0,0]
    q = 0
    csvRow = [q, f, g]
    csvfile = csv_file
    with open (csvfile, "a") as fp:
                wr = csv,writer(fp, dialect='excel')
                wr.writerow(['time','S1', 'S2', 'S3', 'S4', 'S5', 'S6'])
    while True:
            t.sleep(1)
            for b in  range(0,6):
                y[0] = str(datetime.now().strftime('%Y_%m_%d_%H_%M'))
                if GPIO.input(x[b]) == GPIO.HIGH:
                    GPIO.output(y[b], GPIO.HIGH)
                    wl = 3 + 0.5*b
                    y[b+1] = 1
                    dweepy.dweet_for('FlashFloodWL{}'.format(b),{'some_key': 'Water Detection'})
                else:
                    GPIO.output(z[b], GPIO.LOW)
                    y[b+1] = 0
                    dweepy.dweet_for('FlashFloodWL{}'.format(b),{'some_key': 'No Water'})

            with open (csvfile, "a") as fp:
                wr = csv.writer(fp, dialect='excel')
                wr.writerow(y)
            q = q+0.1
            dweepy.dweet_for('402SystemOnOff',{'some_key': q})
            t.sleep(9)

    print('out of loop')
main()