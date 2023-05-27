import numpy
from matplotlib import pyplot
import librosa
import soundfile
import Subsystem.PCP_Basic
import Subsystem.CTT


def chord_song_with_pcp(beats_frames, fft_frames, timestamp, freq_map):
    chord_count = 0
    p_timestamp = 1
    left = 0
    previous_chord = None
    output_buffer = ' ' * 4
    bar_count = 1
    print_ruler(bar_count)
    for right in range(1, len(fft_frames)):
        chord = ''
        if p_timestamp >= len(beats_frames):
            break
        if timestamp[right] >= beats_frames[p_timestamp]:
            p_timestamp += 1
            clip = fft_frames[left:right]
            pcp = Subsystem.PCP_Basic.pcp_with_fft(clip, freq_map)
            chord = Subsystem.CTT.ctt(pcp)

            if chord == previous_chord:
                output_buffer += '-' * 6 + '|'
            else:
                output_buffer += format_chord_label(chord) + '|'

            left = right
            chord_count += 1
            previous_chord = chord

            if chord_count % 4 == 0:
                print(output_buffer)
                output_buffer = ' ' * 4
                bar_count += 1
                print_ruler(bar_count)

    print(output_buffer)

    return 0


def chord_song_with_cqt(beats_frames, cqt_frames, timestamp):
    chord_count = 0
    p_timestamp = 2
    left = 0
    previous_chord = None
    output_buffer = ' ' * 4
    bar_count = 1
    print_ruler(bar_count)
    for right in range(1, len(cqt_frames)):
        chord = ''
        if p_timestamp >= len(beats_frames):
            break
        if timestamp[right] >= beats_frames[p_timestamp] - 35:
            p_timestamp += 1
            clip = cqt_frames[left:right]
            pcp = Subsystem.PCP_Basic.pcp_with_cqt(clip)
            chord = Subsystem.CTT.ctt(pcp)

            if previous_chord == chord:
                output_buffer += '-' * 6 + '|'
            else:
                output_buffer += format_chord_label(chord) + '|'

            left = right
            chord_count += 1
            previous_chord = chord

            if chord_count % 4 == 0:
                print(output_buffer)
                output_buffer = ' ' * 4
                bar_count += 1
                print_ruler(bar_count)

    print(output_buffer)

    return 0


def chord_song_with_knn(beats_frames, cqt_frames, timestamp):
    pass


def format_chord_label(label):
    return label + ' ' * (6 - len(label))


def print_ruler(bar_count):
    print('{:>3d} 1     |2     |3     |4     |'.format(bar_count))
