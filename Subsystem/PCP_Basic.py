import numpy as np
import librosa
import Subsystem.FFT
import Subsystem.Tempo
import cv2
import math
from matplotlib import pyplot as plt
import Subsystem.CQT

# TODO Complete PCP

F_REF = 440

NOTE_AXIS = ['A', '#A', 'B', 'C', '#C', 'D', '#D', 'E', 'F', '#F', 'G', '#G']


def pcp_with_fft(data, freq_map):
    pcp_array = [0] * 12
    for i in data:

        for j in range(1, round(len(i) / 1)):
            index = round(12 * math.log(((freq_map[j] + freq_map[j]) / 2) / F_REF, 2)) % 12
            pcp_array[index] += i[j]

    max_pcp = max(pcp_array)

    for i in range(len(pcp_array)):
        pcp_array[i] = pcp_array[i] / max_pcp

    # plt.bar(NOTE_AXIS, pcp_array)
    # plt.show()

    return pcp_array


def pcp_with_cqt(data):
    raw_pcp_data = [0] * 12

    for i in data:
        for j in range(len(i)):
            raw_pcp_data[(j + 3) % 12] += i[j]

    max_cqt = max(raw_pcp_data)

    pcp_array = [0] * 12

    for i in range(len(raw_pcp_data)):
        pcp_array[i] = raw_pcp_data[i] / max_cqt

    # plt.bar(NOTE_AXIS, pcp_array)
    # plt.show()

    return pcp_array


def smooth_pcp():
    pass
