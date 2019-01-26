import numpy as np
from matplotlib.pyplot import *
import scipy.io.wavfile as wave
from numpy.fft import fft
import wave
import numpy as np
import matplotlib.pyplot as plt

 

class prosodie:

    def lancement(self):
        fe,data = wave.read('video4.wav')
        N = data.size
        T = 1.0*N/fe
        data =data/data.max()
        
    def analyse_spectrale(self):
    #fais chier
    #et l'analyse du son et encore plus dure
    #comprend ca 

yo = prosodie()
yo.analyse_spectrale()












