import numpy
import librosa
import soundfile
import Modules.TMF
from matplotlib import pyplot
import math


def track(spectrum, timestamp, tempo):
    step = 60000 / tempo  # 步长，单位为毫秒（ms）

    max_score = 0
    head_index = 0
    head_timestamp = 0
    top = 35

    onset_index, onset_timestamp, onset_energy = onset(spectrum, timestamp)

    score_list = []

    for shift in range(top):
        phrase = onset_timestamp[shift]

        tmf = Modules.TMF.tmf_real(tempo, timestamp, phrase=-phrase)
        score = 0
        for i in range(len(spectrum)):
            score += spectrum[i] * tmf[i]
        if score > max_score:
            max_score = score
            max_shift = shift
            head_index = onset_index[shift]
            head_timestamp = onset_timestamp[shift]
        score_list.append(score)

    # avg_score = numpy.average(score_list)
    # variance = []
    # for i in score_list:
    #     variance.append(pow((i - avg_score), 2))
    #
    # head_timestamp = onset_timestamp[variance.index(max(variance))]

    # pyplot.bar(range(top), score_list)
    # pyplot.show()

    # print(head_timestamp)

    # head_timestamp = 0

    beats_frame = []  # 节拍时间戳，单位为毫秒（ms）
    m = 1
    while True:
        if head_timestamp - step * m <= 0:
            break
        else:
            m += 1

    mus = head_timestamp - step * m
    first_frame = step + mus

    # frame_pointer = first_frame
    # TODO For Debugging Only! Only For Beats Synced Sample!
    frame_pointer = step
    beats_frame.append(0)

    for i in timestamp:
        if i > frame_pointer:
            beats_frame.append(i)
            frame_pointer += step

    return beats_frame


def onset(spectrum, timestamp):
    onset_index = []
    onset_timestamp = []
    onset_energy = []

    for i in range(1, len(spectrum) - 1):
        if spectrum[i - 1] < spectrum[i] and spectrum[i + 1] < spectrum[i]:
            onset_index.append(i)
            onset_timestamp.append(timestamp[i])
            onset_energy.append(spectrum[i])

    return onset_index, onset_timestamp, onset_energy
