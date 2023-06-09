import modules.tmf
import subsystem.beats_track

BPM_PREDICT_STEP = 0.1


def tempo(fft_data, timestamp, diff_size=1):
    # * diff_Size定义FFT帧分组大小，默认为1（不分组）

    print('-' * 15)

    print('Please select the tempo range (in BPM) this sample is the most likely to be in:')
    print('1 : 50 - 100')
    print('2 : 75 - 150 (Default)')
    print('3 : 100 - 200')
    print('4 : 150 - 300')

    # TODO For debugging only!

    k = eval(input())
    # k = 2

    if k == 1:
        BPM_PREDICT_START = 50
        BPM_PREDICT_END = 100
    elif k == 3:
        BPM_PREDICT_START = 100
        BPM_PREDICT_END = 200
    elif k == 4:
        BPM_PREDICT_START = 150
        BPM_PREDICT_END = 300
    else:
        BPM_PREDICT_START = 75
        BPM_PREDICT_END = 150

    e = []  # 平均能量谱线
    time_axis = []
    avg_fft_frames = [[]]

    i = 0

    while i < len(fft_data) - diff_size:
        t = fft_data[i: i + diff_size]
        avg_elem = []

        for j in range(len(t[0])):
            s = 0
            for k in range(diff_size):
                s += t[k][j]

            avg_elem.append(s / diff_size)

        avg_fft_frames.append(avg_elem.copy())

        time_axis.append(timestamp[i])

        avg_elem.clear()
        print('\rGenerating Spectrum %d of %d. %.1f%% Completed' % (i, len(fft_data), i / len(fft_data) * 100), end='')
        i += diff_size

    avg_fft_frames.pop(0)

    for i in avg_fft_frames:
        e.append(avg_list(i))

    # e.pop(0)

    # TODO For debugging only!
    #
    # images_path = "./Exp_data/e0_400.jpg"
    #
    # plt.plot(time_axis[1500:2500], e[1500:2500])
    # # plt.savefig(images_path)
    # #
    # plt.show()

    []

    # print(e)
    # TODO For debugging only!
    # beats_frames = subsystem.Beats_Track.track(e, timestamp, 123)

    bpm = BPM_PREDICT_START

    bpm_axis = []
    mtv_list = []
    score_list = []
    print('\nDetecting Tempo ...')

    while bpm <= BPM_PREDICT_END:

        mtv = 0.0
        # timestamp[e.index(max(e))]

        # TODO argument phrase padding test below
        # ! tmf_list = modules.TMF.tmf(bpm, timestamp, phrase)

        tmf_list = modules.tmf.tmf(bpm, timestamp, 0)

        for i in range(len(timestamp)):
            mtv += tmf_list[i] * e[i]

        mtv_list.append(mtv)
        bpm_axis.append(bpm)

        print("\rTesting BPM %.3f , MTV = %.3f (%.1f %% Completed)" %
              (bpm, mtv, (bpm - BPM_PREDICT_START) * 100 / (BPM_PREDICT_END - BPM_PREDICT_START)), end='')

        bpm += BPM_PREDICT_STEP

    avg_mtv = avg_list(mtv_list)

    for i in mtv_list:
        score_list.append(pow((i - avg_mtv), 2))

    # plt.plot(bpm_axis, score_list)
    # plt.show()
    #
    # plt.plot(bpm_axis, mtv_list)
    # plt.show()

    res = round(bpm_axis[score_list.index(max(score_list))])

    # print(score_list)
    print("\nTempo Detection Complete!")
    # print('BPM = %.3f' % bpm_axis[score_list.index(max(score_list))])

    print('BPM = %d' % res)

    beats_frames = subsystem.beats_track.track(e, timestamp, res)

    return res, beats_frames


def avg_list(data):
    s = 0
    count = 0
    for i in data:
        s += i
        count += 1

    return s / count
