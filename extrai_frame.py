import cv2
import os
vidcap = cv2.VideoCapture('videos/video.mp4')
success,image = vidcap.read()

#fps = vidcap.get(cv2.cv.CV_CAP_PROP_FPS)
#print fps
#print fps

count = 0
success = True
cont = 1
while success:
  success, image = vidcap.read()
  if cont > 27: ###Salta de 27 em 27 frames
    cv2.imwrite("frames/frame%d.jpg" % count, image)     # save frame as JPEG file
    cv2.imshow('img', image) #Apresenta o frame na tela.
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    count += 1
    cont = 0
  cont = cont + 1


