import numpy
import librosa
from matplotlib import pyplot as plt
import cv2
import math

SAMPLE_RATE = 44100
BIT_DEPTH = 24


def chord_templet_generator(chord, length, sample_rate=SAMPLE_RATE, bit_depth=BIT_DEPTH):
    """
    和弦生成器，用于随机生成一个指定的和弦
    :param chord: string 指定生成的和弦类型
    :param length: int 指定生成的信号长度
    :param sample_rate: int 指定生成信号的采样频率，默认为44100
    :param bit_depth: int 指定生成信号的采样深度，默认为24
    :return: list 生成的信号采样
    """
    pass


def osc(freq=440, length=220500, phrase=0, sample_rate=SAMPLE_RATE, bit_depth=BIT_DEPTH, osc_type='sin', adsr=None):
    """
    振荡器，生成一个震荡信号,支持adsr包络控制
    :param adsr: list 长度为4 控制生成信号的ADSR包络
    :param freq:int 震荡频率
    :param length:int 生成信号的长度
    :param phrase:int 生成信号的相位，单位为采样
    :param sample_rate:int 生成信号的采样频率，默认为44100
    :param bit_depth:int 生成信号的采样深度，默认为24
    :param osc_type:string 指定生成信号的函数类型，默认为sin'(正弦函数)
    :return:list 生成的信号
    """
    if adsr is None:
        adsr = [-1, -1, -1, -1]
    pass


def synth(osc_list=None):
    """
    信号合成器
    :param osc_list: list[list]二位列表，各震荡信号列表
    :return:list 合成的信号采样
    """
    pass
