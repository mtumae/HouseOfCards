import cv2
from PIL import Image
import random
import os
from bisect import bisect
import time

root =  os.path.dirname(os.path.abspath(__file__))



#----------------------------------------------------------
# greyscale.. the following strings represent
# 7 tonal ranges, from lighter to darker.
# for a given pixel tonal level, choose a character
# at random from that range.
 #---------------------------------------------------------
 
greyscale = [
            " ",
            " ",
            ".,-",
            "_ivc=!/|\\~",
            "gjez2]/(YL)t[+T7Vf",
            "mdK4ZGbNDXY5P*Q",
            "W8KMA",
            "#%$"
        ]

#----------------------------------------------------------
# using the bisect class to put luminosity values
# in various ranges.
# these are the luminosity cut-off points for each
# of the 7 tonal levels. At the moment, these are 7 bands
# of even width, but they could be changed to boost
# contrast or change gamma, for example.
# ---------------------------------------------------------
 
zonebounds=[36,72,108,144,180,216,252]
cam=cv2.VideoCapture(0, cv2.CAP_DSHOW)

frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'mpv4')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0,
(frame_width,frame_height))


for i in range(30):
    ret, frame = cam.read()
    out.write(frame)
    cv2.imshow('Camera', frame)
    cv2.imwrite(os.path.join(root, 'videoframe{i}.jpeg'),frame)

cam.release()
out.release()
cv2.destroyAllWindows()


#frames_root = os.path.join(root, 'frames')

while True:
    # open frame buffer, check if it has files, if not throw error
    for i in range(30-1):
        im=Image.open(os.path.join(root, "videoframe{i}.jpeg"), mode='r')
        im=im.resize((200, 100),Image.BILINEAR)# 300, 190
        im=im.convert("L")
        str=""
        for y in range(0,im.size[1]):
            for x in range(0,im.size[0]):
                lum=255-im.getpixel((x,y))
                row=bisect(zonebounds,lum)
                possibles=greyscale[row]
                str=str+possibles[random.randint(0,len(possibles)-1)]
            str=str+"\n"   
        print(str)
        os.system('cls' if os.name == 'nt' else 'clear') 

