
from ppadb.client import Client
import os
import time
os.system('adb start-server')


adb = Client(host='localhost', port=5037)


devices = adb.devices()
if len(devices) == 0:
    print( "No devices found")
device = devices[0]




def findandtap(device):
    try:
        k = device.shell('uiautomator dump /dev/tty')
        count = k.count('inline_retweet')
        for i in range(count):
            i = k.index('inline_retweet')+277
            k=k[i:]
            s = k[:k.index(']')]
            x,y = s.split(',')
            print(x,y)
            tap(device,x,y)
            tap(device,163,2095)
    except Exception as e:
        print("Not found",e)


def swipe(device,xs,ys,xd,yd,time=2000):
    device.shell(f'input swipe {xs} {ys} {xd} {yd} {time}')

def tap(device,x,y):
    device.shell(f"input tap {x} {y}")

while True:
    findandtap(device)
    swipe(device,500 ,2000, 500 ,1500, 100)
