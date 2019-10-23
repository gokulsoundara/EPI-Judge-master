from test_framework import generic_test
import collections


def find_nearest_repetition(paragraph):
    # TODO - you fill in here.
    dic = collections.defaultdict(list)
    for i, w in enumerate(paragraph):
        dic[w].append(i)

    gdist = float('inf')
    for w, l in dic.items():
        if len(l) < 2:
            continue
        f = l[0]
        for i in l[1:]:
            diff = i - f
            gdist = min(gdist, diff)
            f = i
    return gdist if gdist != float('inf') else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("nearest_repeated_entries.py",
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
