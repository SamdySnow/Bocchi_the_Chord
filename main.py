# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import librosa
import numpy as np
from matplotlib import pyplot as plt

import Subsystem.ReadFile
import Subsystem.FFT
import Subsystem.Tempo
import Subsystem.PCP_Basic
import Subsystem.CQT

filepath = 'TestData/SciAudio/Pn_CMaj.wav'

data, samplerate = Subsystem.ReadFile.read_file(filepath)

data_cqt = Subsystem.CQT.cqt(data)

fft_frames, freq_map, timestamp = Subsystem.FFT.get_fft_frames(data)

pcp = Subsystem.PCP_Basic.pcp_with_fft(fft_frames, freq_map)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
