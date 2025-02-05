import cv2


cam=cv2.VideoCapture(0)


frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))


fourcc = cv2.VideoWriter_fourcc(*'mpv4')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0,
(frame_width,frame_height))


for i in range(10):
    ret, frame = cam.read()
    out.write(frame)
    cv2.imshow('Camera', frame)
    cv2.imwrite(f'videoframe{i}.png',frame)
    if cv2.waitKey(1) == ord('q'):
        break


cam.release()
out.release()
cv2.destroyAllWindows()

#1. save each frame of the video 1 by 1😭
#2. pass each frame through photo.py and convert it 🤔
#3. play it frame by frame like an animation 👌