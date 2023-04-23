# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import librosa
import numpy as np
from matplotlib import pyplot as plt

import Subsystem.ReadFile
import Subsystem.FFT
import Subsystem.Tempo

filepath = 'TestData/test2.mp3'

data, samplerate = Subsystem.ReadFile.read_file(filepath)

fft_frames, freq_map, timestamp = Subsystem.FFT.get_fft_frames(data)

Subsystem.Tempo.tempo(fft_frames, freq_map, timestamp)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
