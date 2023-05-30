CHORD_MODE_PATTERN = [
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]

]
CHORD_MODE_MAP = (
    'Maj', 'min', 'Maj7', 'min7', '7'
)
ROOT_NOTE_MAP = (
    'A', '#A', 'B', 'C', '#C', 'D', '#D', 'E', 'F', '#F', 'G', '#G'
)


def ctt(pcp_array):
    """
    和弦模式匹配
    :param pcp_array:list PCP向量
    :return: string 和弦匹配结果
    """
    root = 0
    mode = 0
    max_score = 0

    for root_index in range(len(ROOT_NOTE_MAP)):
        for mode_index in range(len(CHORD_MODE_PATTERN)):

            score = mode_score(pcp_array, root_index, mode_index)
            if score > max_score:
                max_score = score
                root = root_index
                mode = mode_index

    chord = ROOT_NOTE_MAP[root] + CHORD_MODE_MAP[mode]

    return chord


def mode_score(pcp, root_index, mode_index):
    s = 0
    for i in range(12):
        s += CHORD_MODE_PATTERN[mode_index][(i - root_index) % 12] * pcp[i]

    return s / sum(CHORD_MODE_PATTERN[mode_index])
