import math


def tmf(bpm, timestamp, phrase):
    tmf_list = []

    T = 60000 / bpm
    w = 2 * math.pi / T

    for i in timestamp:
        tmf_list.append(tmf_function(i, w, phrase=phrase))

    return tmf_list


def tmf_real(bpm, timestamp, phrase):
    tmf_list = []

    T = 60000 / bpm
    w = 2 * math.pi / T

    for i in timestamp:
        tmf_list.append(tmf_function_real(i, w, phrase=phrase))

    return tmf_list


def tmf_function(time, w, phrase=0.0):
    A = 0.5

    tmf_value = A * math.cos(phrase + w * time) + A

    return tmf_value


def tmf_function_real(time, w, phrase=0.0):
    A = 1.0

    tmf_value = A * math.cos(phrase + w * time)

    return tmf_value
