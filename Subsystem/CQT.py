import librosa
import numpy


def cqt(data):
    Sample_rate = 44100
    Hop_size = 1024

    ces = librosa.cqt(data, sr=Sample_rate, hop_length=Hop_size)
    abs_ces = numpy.abs(ces)
    cqt_frames = numpy.transpose(abs_ces)

    cqt_timestamp = []

    for i in range(numpy.shape(cqt_frames)[0]):
        cqt_timestamp.append(i * 1000 * Hop_size / Sample_rate)  # CQT帧时间戳，单位为毫秒（ms）

    return cqt_frames, cqt_timestamp
