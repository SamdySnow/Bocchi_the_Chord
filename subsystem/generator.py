SAMPLE_RATE = 44100
BIT_DEPTH = 24


def chord_templet_generator():
    """
    和弦生成器，用于随机生成一个指定的和弦
    :return: list 生成的信号采样
    """
    pass


def osc(adsr=None):
    """
    振荡器，生成一个震荡信号,支持adsr包络控制
    :param adsr: list 长度为4 控制生成信号的ADSR包络
    :return:list 生成的信号
    """
    if adsr is None:
        [-1, -1, -1, -1]
    pass


def synth():
    """
    信号合成器
    :return:list 合成的信号采样
    """
    pass
