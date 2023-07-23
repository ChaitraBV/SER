import os
import glob
import tqdm
from IPython.testing.globalipapp import get_ipython
from tqdm.autonotebook import tqdm
from tqdm.autonotebook import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from python_speech_features import mfcc , logfbank
import librosa as lr
import os, glob, pickle
from scipy import signal
import noisereduce as nr
from glob import glob
#All the Required Packages and Libraies are installed.
import soundfile
from sklearn.utils.class_weight import compute_class_weight
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
print("All the Libraries have been Imported now")
#import tensorflow.python.pywrap_tensorflow_internal

os.listdir(path='C:\\Users\\Nethra\\Desktop\\Speech_Emotion_Detection-master\\speech-emotion-recognition-ravdess-data')
def getListOfFiles(dirName):
    listOfFile=os.listdir(dirName)
    allFiles=list()
    for entry in listOfFile:
        fullPath=os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles=allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
    return allFiles

dirName = './speech-emotion-recognition-ravdess-data'
listOfFiles = getListOfFiles(dirName)
print(len(listOfFiles))

"""  
import speech_recognition as sr
r=sr.Recognizer()
for file in range(0 , len(listOfFiles) , 1):
    with sr.AudioFile(listOfFiles[file]) as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(text)
        except:
            print('error')
print("DONE")
"""""
for file in range(0, len(listOfFiles), 1):
    audio, sfreq = lr.load(listOfFiles[file])
    time = np.arange(0, len(audio)) / sfreq

    fig, ax = plt.subplots()
    ax.plot(time, audio)
    ax.set(xlabel='Time (s)', ylabel='Sound Amplitude')
    plt.show()