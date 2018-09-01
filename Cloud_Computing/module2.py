from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, my_twilio
import geocoder
import numpy
import os
import re
import pickle
import timeit
import glob
import cv2
from numpy import shape
from skimage import transform
import skimage
from skimage import io
from numpy import *
import sklearn
from sklearn.model_selection import train_test_split   ### import sklearn tool
import threading
import requests
import json
import keras
from keras.preprocessing import image as image_utils
from keras.callbacks import ModelCheckpoint

def crash():
    os.system('{} {}'.format('python',cxd))
    

#def sos():
    #os.system('{} {}'.format('python',cyd))

def load_set(videofile):
    '''The input is the path to the video file - the training videos are 99 frames long and have resolution of 720x1248
       This will be used for each video, individially, to turn the video into a sequence/stack of frames as arrays
       The shape returned (img) will be 99 (frames per video), 144 (pixels per column), 256 (pixels per row))
    '''
    ### below, the video is loaded in using VideoCapture function
    vidcap = cv2.VideoCapture(videofile)
    ### now, read in the first frame
    success,image = vidcap.read()
    count = 0       ### start a counter at zero
    error = ''      ### error flag
    success = True  ### start "sucess" flag at True
    all_frames = []
    img = []        ### create an array to save each image as an array as its loaded 
    while success: ### while success == True
        success, img = vidcap.read()  ### if success is still true, attempt to read in next frame from vidcap video import
        count += 1  ### increase count
        frames=[]
          ### frames will be the individual images and frames_resh will be the "processed" ones
        for j in range(0,99):
            try:
                success, img = vidcap.read()
                ### conversion from RGB to grayscale image to reduce data
                tmp = skimage.color.rgb2gray(numpy.array(img))
                ### ref for above: https://www.safaribooksonline.com/library/view/programming-computer-vision/9781449341916/ch06.html
                
                ### downsample image
                tmp = skimage.transform.downscale_local_mean(tmp, (5,5))
                frames.append(tmp)
                count+=99
            
            except:
                count+=1
                pass#print 'There are ', count, ' frame; delete last'        read_frames(videofile, name)
    
        ### if the frames are the right shape (have 99 entries), then save
        #print numpy.shape(frames), numpy.shape(all_frames)
        if numpy.shape(frames)==(99, 144, 256):
            all_frames.append(frames)
        ### if not, pad the end with zeros
        elif numpy.shape(frames[0])==(144,256):
            #print shape(all_frames), shape(frames), shape(concatenate((all_frames[-1][-(99-len(frames)):], frames)))
            #print numpy.shape(all_frames), numpy.shape(frames)
            all_frames.append(numpy.concatenate((all_frames[-1][-(99-len(frames)):], frames)))
        elif numpy.shape(frames[0])!=(144,256):
            error = 'Video is not the correct resolution.'
    vidcap.release()
    del frames; del image
    return all_frames, error

import keras
from keras.preprocessing import image
from keras.models import load_model
from keras.models import Model
from keras.layers import Input, Dense, TimeDistributed
from keras.layers import LSTM


model=load_model('model.hdf5')
t = load_set('headon1.mp4')
tt = numpy.array(t[0][0])
tt = tt.reshape((1,99,144,256))

j = model.predict(tt)
print(j)

k=j.ravel()

#import matplotlib.pyplot as plt
#plt.imshow(tt[0][98])
#plt.show()

for i in k:
    url  = 'https://api.myjson.com/bins/ph58c'
    url1 = 'https://api.myjson.com/bins/1gx21o'
    cxd = os.path.join(os.getcwd(), "circular.py")
    cyd = os.path.join(os.getcwd(), "send_sms.py")
    while(True):
        if i >= 0.5:
            print('Crashed')
            r = requests.put(url1, json=[{"alarm":0,"accident":1}])
            t = threading.Thread(target = crash, name = 'thread1')
            t.start()
            break
        elif i <= 0.4:
            #print('Safe')
            break
    while(True):
        if i <= 0.5:
            #print('Safe')
            break
        elif i > 0.5:
            print('SOS!!')
            g = geocoder.ip('me')
            c = g.latlng
            a = str(c[0])
            b = str(c[1])


# Find these values at https://twilio.com/user/account
            client = Client(account_sid, auth_token)

            my_msg = "Your Friend " + my_cell + " is drowsy while driving at Lat:- " + a + " Long:- " + b

            message = client.messages.create(to=my_cell, from_=my_twilio, body=my_msg)
            print ( "SMS sent")
            #r = requests.put(url, json=[{"drowsybutton":0,"alarm":0,"accident":0,"sos":0}])
            #t = threading.Thread(target = SOS, name = 'thread2')
            #t.start()
            break


