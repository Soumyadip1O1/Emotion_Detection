from importlib.metadata import files
import cv2 
import numpy as np 
import mediapipe as mp 
from keras.models import load_model 
import time
import os
import random

import playsound

model  = load_model("model.h5")
label = np.load("labels.npy")



holistic = mp.solutions.holistic
holis = holistic.Holistic()
drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
now = time.time()

global text

while True:
    
    lst = []
    _, frm = cap.read()
    frm = cv2.flip(frm, 1)
    res = holis.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))
    if res.face_landmarks:
                for i in res.face_landmarks.landmark:
                        lst.append(i.x - res.face_landmarks.landmark[1].x)
                        lst.append(i.y - res.face_landmarks.landmark[1].y)
                lst = np.array(lst).reshape(1,-1)
                text = label[np.argmax(model.predict(lst))]
                print(text)
                text=text.title()
                cv2.putText(frm, text, (50,50),cv2.FONT_ITALIC, 1, (255,0,0),2)
    drawing.draw_landmarks(frm, res.face_landmarks, holistic.FACEMESH_CONTOURS)
    cv2.imshow("window", frm)
    key = cv2.waitKey(30)& 0xff
    future=time.time()
    diff=future-now

    if diff>5 :
            try:
                cv2.destroyAllWindows()
                cap.release()
                if text == 'Happy':
                        folder_path = os.path.abspath("C:/Users/s/Desktop/Emotion Based Music/Happy/")
                        songs = os.listdir(folder_path)
                        random_song = random.choice(songs)
                        song_path = os.path.join(folder_path, random_song)
                        playsound(song_path)
                        # music_files = [file for file in os.listdir(folder_path) if file.endswith('.mp3') or file.endswith('.wav')]
                        # mf=random.choice(music_files)
                        # for mf in mf:
                        #         music_file_path = os.path.join(folder_path, mf)
                        #         print(f"Playing {mf}...")
                        #         playsound.playsound(music_file_path)
                               
                elif text == 'Sad':
                        folder_path = os.path.abspath("C:/Users/s/Desktop/Emotion Based Music/Sad/")
                        music_files = [file for file in os.listdir(folder_path) if file.endswith('.mp3') or file.endswith('.wav')]
                        for music_file in music_files:
                                music_file_path = os.path.join(folder_path, music_file)
                                print(f"Playing {music_file}...")
                                playsound.playsound(music_file_path)
                
                elif text == 'Nutral':
                        folder_path = os.path.abspath("C:/Users/s/Desktop/Emotion Based Music/Nutral/")
                        music_files = [file for file in os.listdir(folder_path) if file.endswith('.mp3') or file.endswith('.wav')]
                        for music_file in music_files:
                                music_file_path = os.path.join(folder_path, music_file)
                                print(f"Playing {music_file}...")
                                playsound.playsound(music_file_path)
                break
            except:
                print()
                break

            
   
                
    if key == 27:
                cv2.destroyAllWindows()
                cap.release()
                break
                
                            