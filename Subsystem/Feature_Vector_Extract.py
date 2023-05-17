import json

import librosa
import numpy
from matplotlib import pyplot as plt
import pandas
import os
import random

import Subsystem.CQT

ROOT_PATH = './TestData/SciAudio/AliciasKeys_Samples/'
ROOT_NAME = 'AliciasKeys_'
DATA_PATH = './TestData/Datasets/'
JSON_DATA_PATH = './TestData/Datasets/Chord_data.json'

KEY_MAP = ['A', '#A', 'B', 'C', '#C', 'D', '#D', 'E', 'F', '#F', 'G', '#G']

CHORD_MODE_MAP = (
    'Maj', 'min', 'Maj7', 'min7', '7'
)

CHORD_MODE_PATTERN_FROM_ROOT = [
    [4, 7],
    [3, 7],
    [4, 7, 11],
    [3, 7, 10],
    [4, 7, 10]
]


def feature_vector():
    feature_data = [[]]
    for octave in range(3, 5):  # 循环八度
        for root_note_index in range(12):  # 循环根音
            for chord_mode_index in range(2):  # 循环和弦类型（三和弦）

                chord_name = KEY_MAP[root_note_index] + CHORD_MODE_MAP[chord_mode_index]

                for r in range(3):
                    file_name = chord_name + '_Octave_' + str(octave) + '_' + str(r) + '.wav'
                    file_path = DATA_PATH + file_name

                    data, sr = librosa.load(file_path, sr=44100)
                    data_cqt, timestamp = Subsystem.CQT.cqt(data)

                    s = [chord_name]
                    for i in smooth_feature(data_cqt):
                        s.append(i)

                    feature_data.append(s)
                    print('\r Eval Chord %s' % file_name,end='')

    feature_data.pop(0)
    with open('./TestData/data.json', 'w') as f:
        json.dump(feature_data,f)


    return 0


def smooth_feature(data):
    res = []
    for i in range(len(data[0])):
        ele = 0
        for j in range(len(data)):
            ele += data[j][i]
        res.append(ele)

    max_f = 0

    for i in res:
        if i > max_f:
            max_f = i

    nor_res = res/max_f

    return nor_res

