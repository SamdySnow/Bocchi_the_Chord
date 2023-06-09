# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import librosa
import soundfile as sf

import subsystem.chord_song
import subsystem.cqt
import subsystem.ctt
import subsystem.fft
import subsystem.pcp
import subsystem.tempo


def get_sample():
    path = './TestData/SciAudio/AliciasKeys_Samples_All.wav'
    root_path = './TestData/SciAudio/AliciasKeys_Samples'
    raw_data, sr = librosa.load(path, sr=44100)

    sp = 0
    step = 44100 * 4

    note = 0
    octave = 1

    NOTE_MAP = ['C', '#C', 'D', '#D', 'E', 'F', '#F', 'G', '#G', 'A', '#A', 'B']

    while True:
        try:
            if sp > len(raw_data):
                break

            sample = raw_data[sp:sp + step]
            # sample_array = numpy.array(sample)
            NOTE_MAP[note % 12] + str(octave)
            file = root_path + '/' + 'AliciasKeys_' + NOTE_MAP[note % 12] + str(octave) + '.wav'
            print('Split Note %s' % (NOTE_MAP[note % 12] + str(octave)))
            sf.write(file, sample, 44100, subtype='PCM_24')
            note += 1
            octave = note // 12 + 1
            sp += step

        except IndexError:
            break

    return None


# subsystem.Alicias_Chord_Generator.generate_chord_list()


# filepath = './TestData/SciAudio/Pn_#FMaj7_DO.wav'
# filepath = './TestData/test2.mp3'
# filepath = './TestData/SciAudio/Pn_A3_440Hz.wav'
# filepath = './TestData/SciAudio/Pn_DMaj.wav'
# filepath = './TestData/SciAudio/Pn_DMaj_-1Oct.wav'
# filepath = './TestData/SciAudio/Pn_DMaj_-2Oct.wav'
# filepath = './TestData/SciAudio/Pn_DMaj_DO.wav'
# filepath = './TestData/Song_clip/01.wav'

filepath = './TestData/Song_clip/Act_data/Easy.wav'

# get_sample()

# subsystem.Feature_Vector_Extract.feature_vector()


print('Reading Files...')

data, samplerate = librosa.load(filepath, sr=44100)

cqt_data, cqt_timestamp = subsystem.cqt.cqt(data)

fft_frames, freq_map, timestamp = subsystem.fft.get_fft_frames(data)
tempo, betas_frames = subsystem.tempo.tempo(fft_frames, timestamp)
subsystem.chord_song.chord_song_with_cqt(betas_frames, cqt_data, cqt_timestamp)

# subsystem.Chord_Song.chord_song_with_pcp(betas_frames, fft_frames, timestamp, freq_map)

cqt_data, cqt_timestamp = subsystem.cqt.cqt(data)
# knn_chord = subsystem.CTT_KNN.ctt_knn(cqt_data)


# print('Performing HPSS...')
# harmonic_data, percussive_data = librosa.effects.hpss(data)
# print('Generating Harmonic Spectrum')
# harmonic_fft_data, harmonic_freq_map, harmonic_timestamp = subsystem.FFT.get_fft_frames(harmonic_data)
#
# print('Generating percussive Spectrum')
# percussive_fft_data, percussive_freq_map, percussive_timestamp = subsystem.FFT.get_fft_frames(percussive_data)

# # TODO For Debugging only! Delete After Generation.
# harmonic_array = numpy.array(harmonic_data)
# percussive_array = numpy.array(percussive_data)

# sf.write('./TestData/HPSS_Wave/constellation_harm.wav', harmonic_array, samplerate, subtype='PCM_24')
# sf.write('./TestData/HPSS_Wave/constellation-perc.wav', percussive_array, samplerate, subtype='PCM_24')



print('Generating Overall Spectrum')

# tempo = subsystem.Tempo.tempo(percussive_fft_data, percussive_timestamp)


pcp = subsystem.pcp.pcp_with_fft(fft_frames, freq_map)
cqt_pcp = subsystem.pcp.pcp_with_cqt(cqt_data)

chord_pcp = subsystem.ctt.ctt(pcp)
chord_cqt = subsystem.ctt.ctt(cqt_pcp)

print(chord_pcp)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
