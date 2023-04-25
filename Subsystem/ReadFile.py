import librosa
import numpy


def read_file(path):
    data, sample_rate = librosa.load(path, sr=44100)

    return data, sample_rate
