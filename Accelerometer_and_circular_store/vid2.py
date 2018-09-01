import cv2
import os
import subprocess
image_folder = 'images_1'
video_name = 'video.mp4'

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, -1, 1, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()

c = 'ffmpeg.exe -y -i ' + 'video.mp4' + ' -r 30 -s 112x112 -c:v libx264 -b:v 3M -strict -2 -movflags faststart '+'video_2.mp4'


subprocess.call(c, shell=True)