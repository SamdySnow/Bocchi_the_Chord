# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import librosa
import numpy
from matplotlib import pyplot as plt

import Subsystem.FFT
import Subsystem.Tempo
import Subsystem.PCP_Basic
import Subsystem.CQT
import soundfile as sf

filepath = './TestData/test2.mp3'

print('Reading Files...')

data, samplerate = librosa.load(filepath, sr=44100)

print('Performing HPSS...')
harmonic_data, percussive_data = librosa.effects.hpss(data)

# # TODO For Debugging only! Delete After Generation.
# harmonic_array = numpy.array(harmonic_data)
# percussive_array = numpy.array(percussive_data)

# sf.write('./TestData/HPSS_Wave/constellation_harm.wav', harmonic_array, samplerate, subtype='PCM_24')
# sf.write('./TestData/HPSS_Wave/constellation-perc.wav', percussive_array, samplerate, subtype='PCM_24')


cqt_data, cqt_timestamp = Subsystem.CQT.cqt(data)
print('Generating Overall Spectrum')
fft_frames, freq_map, timestamp = Subsystem.FFT.get_fft_frames(data)

print('Generating Harmonic Spectrum')
harmonic_fft_data, harmonic_freq_map, harmonic_timestamp = Subsystem.FFT.get_fft_frames(harmonic_data)

print('Generating percussive Spectrum')
percussive_fft_data, percussive_freq_map, percussive_timestamp = Subsystem.FFT.get_fft_frames(percussive_data)

tempo = Subsystem.Tempo.tempo(percussive_fft_data, percussive_timestamp)

pcp = Subsystem.PCP_Basic.pcp_with_fft(fft_frames, freq_map)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
