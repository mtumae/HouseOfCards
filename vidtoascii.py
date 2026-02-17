import cv2
from PIL import Image
import os
import random
from bisect import bisect

root =  os.path.dirname(os.path.abspath(__file__))
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
zonebounds=[36,72,108,144,180,216,252]


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

fourcc = cv2.VideoWriter_fourcc(*'mpv4')
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = 20.0

out = cv2.VideoWriter(os.path.join(root, 'output.mp4'), fourcc, 20.0,
(frame_width,frame_height))

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    out.write(frame)
    frame_number = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
    cv2.imwrite(os.path.join(root, f'frames/videoframe{frame_number}.jpeg'),frame)

    # write to cli at the same time
    # I wish i could read directly from the frame variable instead of having to save and read again, but this is fine for now
    im=Image.open(os.path.join(root, f'frames/videoframe{frame_number}.jpeg'), mode='r')
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

    cv2.imshow('Recording', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
out.release()
cv2.destroyAllWindows()