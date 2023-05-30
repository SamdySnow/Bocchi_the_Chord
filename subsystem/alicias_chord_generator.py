import random
import librosa
import numpy
import soundfile

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


def generate_chord_list():
    # 构建7个八度上的和弦列表
    for octave in range(1, 8):  # 循环八度
        for root_note_index in range(12):  # 循环根音
            for chord_mode_index in range(2):  # 循环和弦类型（三和弦）

                chord_name = KEY_MAP[root_note_index] + CHORD_MODE_MAP[chord_mode_index]

                root_note_name = ROOT_NAME + KEY_MAP[root_note_index] + str(octave) + '.wav'
                third_note_name = ROOT_NAME + KEY_MAP[
                    (root_note_index + CHORD_MODE_PATTERN_FROM_ROOT[chord_mode_index][0]) % 12] + str(
                    octave) + '.wav'
                fifth_note_name = ROOT_NAME + KEY_MAP[
                    (root_note_index + CHORD_MODE_PATTERN_FROM_ROOT[chord_mode_index][1]) % 12] + str(
                    octave) + '.wav'

                root_note_path = ROOT_PATH + root_note_name
                third_note_path = ROOT_PATH + third_note_name
                fifth_note_path = ROOT_PATH + fifth_note_name

                root_note, srr = librosa.load(root_note_path, sr=44100)
                third_note, srt = librosa.load(third_note_path, sr=44100)
                fifth_note, srf = librosa.load(fifth_note_path, sr=44100)

                for r in range(3):  # 每个和弦随机生成2个音符力度不同的样本

                    file_name = chord_name + '_Octave_' + str(octave) + '_' + str(r) + '.wav'
                    file_path = DATA_PATH + file_name

                    rs = []
                    tv = random.uniform(0.6, 1)
                    fv = random.uniform(0.4, 1)

                    for i in range(len(root_note)):
                        rs.append(
                            root_note[i] + third_note[i] * tv + fifth_note[i] * fv)

                    audio_array = numpy.array(rs)
                    soundfile.write(file_path, audio_array, 44100, subtype='PCM_24')
                    print('\rGenerate Chord %s' % file_name)

    for octave in range(1, 8):  # 循环八度
        for root_note_index in range(12):  # 循环根音
            for chord_mode_index in range(2, 5):  # 循环和弦类型（七和弦）

                chord_name = KEY_MAP[root_note_index] + CHORD_MODE_MAP[chord_mode_index]

                root_note_name = ROOT_NAME + KEY_MAP[root_note_index] + str(octave) + '.wav'
                third_note_name = ROOT_NAME + KEY_MAP[
                    (root_note_index + CHORD_MODE_PATTERN_FROM_ROOT[chord_mode_index][0]) % 12] + str(
                    octave) + '.wav'
                fifth_note_name = ROOT_NAME + KEY_MAP[
                    (root_note_index + CHORD_MODE_PATTERN_FROM_ROOT[chord_mode_index][1]) % 12] + str(
                    octave) + '.wav'
                seventh_note_name = ROOT_NAME + KEY_MAP[
                    (root_note_index + CHORD_MODE_PATTERN_FROM_ROOT[chord_mode_index][2]) % 12] + str(
                    octave) + '.wav'

                root_note_path = ROOT_PATH + root_note_name
                third_note_path = ROOT_PATH + third_note_name
                fifth_note_path = ROOT_PATH + fifth_note_name
                seventh_note_path = ROOT_PATH + seventh_note_name

                root_note, srr = librosa.load(root_note_path, sr=44100)
                third_note, srt = librosa.load(third_note_path, sr=44100)
                fifth_note, srf = librosa.load(fifth_note_path, sr=44100)
                seventh_note, srs = librosa.load(seventh_note_path, sr=44100)

                for r in range(3):  # 每个和弦随机生成2个音符力度不同的样本

                    file_name = chord_name + '_Octave_' + str(octave) + '_' + str(r) + '.wav'
                    file_path = DATA_PATH + file_name

                    rs = []
                    tv = random.uniform(0.6, 1)
                    fv = random.uniform(0.4, 1)
                    sv = random.uniform(0.4, 1)

                    for i in range(len(root_note)):
                        rs.append(
                            root_note[i] + third_note[i] * tv + fifth_note[i] * fv + seventh_note[i] * sv)

                    audio_array = numpy.array(rs)
                    soundfile.write(file_path, audio_array, 44100, subtype='PCM_24')
                    print('\rGenerate Chord %s' % file_name)

    # 构建随机加入和弦內音的三和弦
    for additional_note_count in range(1, 5):
        pass
