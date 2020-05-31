#!/usr/bin/env python
# coding: utf-8

# In[8]:


import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import IPython.display as ipd

################################################
class Furie:

    def fourier2canales(self, Nombreaudio)

        nombreaudio=Nombreaudio

        audio= %nombreaudio'.wav'' #Variable de entrada, audio en formato .wav. Obviar las comillas dobles ("")
        fs, data = wavfile.read(audio)

        #Datos un audio
        data=data[:,0] #El código en esta parte difiere de un audio de 2 o 1 canal. Como se encuentra actualmente está
        #para 2 canales. En caso de que se reciba audios de 1 canal, habrà que cambiar data=data[:,0] por data=data.
        tamdata = data.size
        duration = tamdata/fs
        dt = duration/tamdata
        t = np.arange(0,duration,dt)

        datosprom=np.sum(data)/tamdata
        data=data-datosprom

        dataft = np.fft.fftshift(np.fft.fft(np.fft.fftshift(data)))*dt
        freq = np.arange(-1/(2*dt),1/(2*dt),1/(dt*tamdata))

        x=abs(dataft)
        x=list(x)
        maxi=x.index(np.max(x))
        frecuencia = abs(freq[maxi]) #Variable de salida, frecuencia máxima luego de mantener una estabilidad en el hablar.

        return frecuencia
        #print("La frecuencia característica es de:"'%.2f' %frecuencia) #Sistema de redonde, 2 cifra significativas

    def fourier1canal(self,Nombreaudio)

        nombreaudio=Nombreaudio

        audio= %nombreaudio'.wav'' #Variable de entrada, audio en formato .wav. Obviar las comillas dobles ("")
        fs, data = wavfile.read(audio)

        #Datos un audio
        data=data #El código en esta parte difiere de un audio de 2 o 1 canal. Como se encuentra actualmente está
        #para 2 canales. En caso de que se reciba audios de 1 canal, hasbrà que cambiar data=data[:,0] por data=data.
        tamdata = data.size
        duration = tamdata/fs
        dt = duration/tamdata
        t = np.arange(0,duration,dt)

        datosprom=np.sum(data)/tamdata
        data=data-datosprom

        dataft = np.fft.fftshift(np.fft.fft(np.fft.fftshift(data)))*dt
        freq = np.arange(-1/(2*dt),1/(2*dt),1/(dt*tamdata))

        x=abs(dataft)
        x=list(x)
        maxi=x.index(np.max(x))
        frecuencia = abs(freq[maxi]) #Variable de salida, frecuencia máxima luego de mantener una estabilidad en el hablar.

        return frecuencia
        #print("La frecuencia característica es de:"'%.2f' %frecuencia) #Sistema de redonde, 2 cifra significativas
