import librosa
import numpy


def cqt(data):
    Sample_rate = 44100
    Hop_size = 1024

    ces = librosa.cqt(data, sr=Sample_rate, hop_length=Hop_size)
    abs_ces = numpy.abs(ces)
    max_cqt_value = numpy.max(abs_ces)
    cqt_frames = numpy.transpose(abs_ces)

    cqt_timestamp = []

    normalized_cqt_frame = [[]]

    for i in range(numpy.shape(cqt_frames)[0]):
        cqt_timestamp.append(i * 1000 * Hop_size / Sample_rate)  # CQT帧时间戳，单位为毫秒（ms）

    for i in range(numpy.shape(cqt_frames)[0]):
        frame = cqt_frames[i,:]
        normalized_frame = frame/max_cqt_value
        normalized_cqt_frame.append(normalized_frame)

    normalized_cqt_frame.pop(0)

    return normalized_cqt_frame, cqt_timestamp
