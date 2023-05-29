import modules.filters
import modules.tmf


def track(spectrum, timestamp, tempo):
    step = 60000 / tempo  # 步长，单位为毫秒（ms）

    max_score = 0
    head_timestamp = 0
    top = 35

    smoothed_spectrum = modules.filters.gaussian_blur(spectrum, 3.0)

    onset_index, onset_timestamp, onset_energy = onset(smoothed_spectrum, timestamp)

    score_list = []

    for shift in range(top):
        if shift >= len(onset_index):
            break

        phrase = onset_timestamp[shift]

        tmf = modules.tmf.tmf_real(tempo, timestamp, phrase=-phrase)
        score = 0

        for i in range(len(smoothed_spectrum)):
            score += smoothed_spectrum[i] * tmf[i]

        if score > max_score:
            max_score = score
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

    frame_pointer = first_frame
    # TODO For Debugging Only! Only For Beats Synced Sample!
    # frame_pointer = step
    beats_frame.append(0)

    for i in timestamp:
        if i > frame_pointer:
            beats_frame.append(i)
            frame_pointer += step

    return beats_frame


def onset(smoothed_spectrum, timestamp):
    onset_index = []
    onset_timestamp = []
    onset_energy = []

    for i in range(1, len(smoothed_spectrum) - 1):
        if smoothed_spectrum[i - 1] < smoothed_spectrum[i] and smoothed_spectrum[i + 1] < smoothed_spectrum[i]:
            onset_index.append(i)
            onset_timestamp.append(timestamp[i])
            onset_energy.append(smoothed_spectrum[i])

    return onset_index, onset_timestamp, onset_energy
