import numpy


def get_fft_frames(x, nfft=1024, cross=256, samplerate=44100):

    """
    得到一个原始采样信号的FFT结果与频率点位映射表
    :param x: list 原始采样信号
    :param nfft: int FFT大小，默认为1024
    :param cross: int 分帧交叉大小
    :param samplerate: int 采样频率
    :return: list[list],list,list FFT帧，频率映射表，FFT帧的时间戳（ms，毫秒）
    """

    tile = len(x) - numpy.floor(len(x) / (nfft - cross)) * (nfft - cross)
    padding = int(numpy.floor(nfft - tile))  # 计算补零个数

    data = numpy.array(x)
    data = numpy.append(data, numpy.zeros(padding))  # 数据补零

    # 数据分帧与加窗

    nf = numpy.floor((len(data) - nfft)/(nfft - cross)) + 1

    frames = [[]]
    windows = numpy.hanning(nfft)  # 窗口函数（汉宁窗）

    timestamp = []  # 时间戳，单位为毫秒（ms）

    for i in range(int(nf)):

        f = data[i * (nfft - cross): i * (nfft - cross) + nfft]
        print("\rsplit frame: %d of %d complete  (%.1f%%)" % (i, nf, i/nf * 100), end='')
        frames.append(f)
        timestamp.append(i * (nfft - cross) * 1000 / samplerate)

    print('\nFrame Splitting Complete!')

    frames.pop(0)
    timestamp.pop()

    fft_frames = [[]]
    max_fft_res = 0

    for i in range(len(frames)):  # 快速傅里叶变换

        x = frames[i] * windows
        a = numpy.fft.rfft(x)

        e = abs(a)

        if max(e) > max_fft_res:
            max_fft_res = max(e)

        fft_frames.append(e)

        print("\rFFT frame: %d of %d complete  (%.1f%%)" % (i, nf, i/nf * 100), end='')

    fft_frames.pop(0)
    print('\nFFT Completed!')

    normalized_fft_frames = [[]]

    for i in range(len(fft_frames)):

        normalized_fft_frames.append(fft_frames[i]/max_fft_res)
        print("\rNormalizing FFT frame: %d of %d complete  (%.1f%%)" % (i, nf, i / nf * 100), end='')

    normalized_fft_frames.pop(0)
    print('\nNormalizing FFT Completed!')

    freq_map = numpy.fft.rfftfreq(nfft, 1/samplerate)

    return normalized_fft_frames, freq_map, timestamp

