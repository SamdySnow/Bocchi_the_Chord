import math


def gaussian_blur(data, sigma):
    """
    一维高斯滤波器（低通滤波）
    :param data: list 输入的数据序列（一维）
    :param sigma:  float 标准差
    :return:  list 滤波后的数据序列
    """
    length = len(data)

    res = []

    for i in range(length):

        left_clip = data[0:i]
        right_clip = data[i + 1:length]

        s = data[i] * kernel(0, sigma)

        for e in range(len(left_clip)):
            index = e - len(left_clip)
            s += kernel(index, sigma) * left_clip[e]

        for e in range(len(right_clip)):
            index = e + 1
            s += kernel(index, sigma) * right_clip[e]

        res.append(s)
        print('\rSmoothing Spectrum %d of %d (%.2f %% Completed)' % (i, length, (i / length) * 100), end='')
    print('\n', end='')
    return res


def kernel(index, sigma):
    return (1 / math.sqrt(2 * math.pi * math.pow(sigma, 2))) * math.exp(-math.pow(index, 2) / (2 * math.pow(sigma, 2)))
    pass
