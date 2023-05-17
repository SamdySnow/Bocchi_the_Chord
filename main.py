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
import Subsystem.CTT
import pygame as ui
import Subsystem.Alicias_Chord_Generator
import Subsystem.Feature_Vector_Extract
import Subsystem.CTT_KNN


def get_sample():
    path = './TestData/SciAudio/AliciasKeys_Samples_All.wav'
    root_path = './TestData/SciAudio/AliciasKeys_Samples'
    data, sr = librosa.load(path, sr=44100)

    sp = 0
    step = 44100 * 4

    note = 0
    octave = 1

    NOTE_MAP = ['C', '#C', 'D', '#D', 'E', 'F', '#F', 'G', '#G', 'A', '#A', 'B']

    while True:
        try:
            if sp > len(data):
                break

            sample = data[sp:sp + step]
            # sample_array = numpy.array(sample)
            note_name = NOTE_MAP[note % 12] + str(octave)
            file = root_path + '/' + 'AliciasKeys_' + NOTE_MAP[note % 12] + str(octave) + '.wav'
            print('Split Note %s' % (NOTE_MAP[note % 12] + str(octave)))
            sf.write(file, sample, 44100, subtype='PCM_24')
            note += 1
            octave = note // 12 + 1
            sp += step

        except IndexError:
            break

    return None


# Subsystem.Alicias_Chord_Generator.generate_chord_list()


filepath = './TestData/SciAudio/Pn_#FMaj7_DO.wav'

# get_sample()
# Subsystem.Feature_Vector_Extract.feature_vector()


print('Reading Files...')

data, samplerate = librosa.load(filepath, sr=44100)
cqt_data, cqt_timestamp = Subsystem.CQT.cqt(data)
knn_chord = Subsystem.CTT_KNN.ctt_knn(cqt_data)

# print('Performing HPSS...')
# harmonic_data, percussive_data = librosa.effects.hpss(data)
# print('Generating Harmonic Spectrum')
# harmonic_fft_data, harmonic_freq_map, harmonic_timestamp = Subsystem.FFT.get_fft_frames(harmonic_data)
#
# print('Generating percussive Spectrum')
# percussive_fft_data, percussive_freq_map, percussive_timestamp = Subsystem.FFT.get_fft_frames(percussive_data)

# # TODO For Debugging only! Delete After Generation.
# harmonic_array = numpy.array(harmonic_data)
# percussive_array = numpy.array(percussive_data)

# sf.write('./TestData/HPSS_Wave/constellation_harm.wav', harmonic_array, samplerate, subtype='PCM_24')
# sf.write('./TestData/HPSS_Wave/constellation-perc.wav', percussive_array, samplerate, subtype='PCM_24')


cqt_data, cqt_timestamp = Subsystem.CQT.cqt(data)
print('Generating Overall Spectrum')

fft_frames, freq_map, timestamp = Subsystem.FFT.get_fft_frames(data)

# tempo = Subsystem.Tempo.tempo(percussive_fft_data, percussive_timestamp)



pcp = Subsystem.PCP_Basic.pcp_with_fft(fft_frames, freq_map)
cqt_pcp = Subsystem.PCP_Basic.pcp_with_cqt(cqt_data)

chord_pcp = Subsystem.CTT.ctt(pcp)
chord_cqt = Subsystem.CTT.ctt(cqt_pcp)


print(chord_pcp)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
