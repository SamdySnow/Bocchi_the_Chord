import json

import numpy
from matplotlib import pyplot as plt
import math
import Subsystem.Feature_Vector_Extract

K = 10


def ctt_knn(data):
    dist_map = [[]]
    with open('./TestData/data.json', 'r') as f:
        feature_map = json.load(f)

    print(feature_map)
    data_feature = Subsystem.Feature_Vector_Extract.smooth_feature(data)

    for i in feature_map:
        label = i[0]
        feature = i[1:]
        dm_ele = [label, l2_dist(data_feature, feature)]
        dist_map.append(dm_ele)

    dist_map.pop(0)

    shorted_dm = [[]]
    l = len(dist_map)

    for i in range(l):
        min_i = 0
        for j in range(len(dist_map)):
            if dist_map[j][1] < dist_map[min_i][1]:
                min_i = j

        shorted_dm.append(dist_map[min_i])
        dist_map.pop(min_i)

    shorted_dm.pop(0)

    print(shorted_dm)





def l2_dist(list1, list2):
    dist = 0
    for i in range(len(list1)):
        dist += math.pow((list1[i] - list2[i]), 2)

    return math.pow(dist, 0.5)
