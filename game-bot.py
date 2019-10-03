#!/usr/bin/python3
import time 
import pyautogui
import numpy as np


def get_image(im):
    return im.crop((820, 600, im.width-800,im.height-400))


def action(key):
    pyautogui.press(key)
    pyautogui.press(key)

    
def main():
    n=int(input("Enter the score: ")) // 2

    time.sleep(5)

    flag=0
    for i in range(n):
        im = pyautogui.screenshot()
        c=get_image(im)
        left=c.crop((0,0,c.width/2,c.height))
        right=c.crop((c.width/2,0,c.width,c.height))
        l_val=np.sum(np.array(left.getpixel((left.width/2,left.height/2))))
        r_val=np.sum(np.array(right.getpixel((right.width/2,right.height/2))))

        if(l_val<r_val):
                print("> Tree at left")
                action("right")
        else:
                print("> Tree at right")
                action("left")

        time.sleep(0.15)

if __name__ == "__main__":
	main()
