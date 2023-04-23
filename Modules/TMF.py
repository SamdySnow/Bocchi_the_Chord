import math
from matplotlib import pyplot as plt


def tmf(bpm, timestamp, phrase):

    tmf_list = []

    T = 60000 / bpm
    w = 2 * math.pi / T

    for i in timestamp:
        tmf_list.append(tmf_function(i, w, phrase=phrase))

    # tmf_list.pop(0)

    # plt.plot(tmf_list[:400])
    # plt.show()

    # print(tmf_list)


    return tmf_list

def tmf_function(time, w, phrase = 0.0):

    A = 0.5

    tmf_value = A*math.cos(phrase + w*time) + A

    return tmf_value



