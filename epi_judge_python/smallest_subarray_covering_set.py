import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_subarray_covering_set(paragraph, keywords):
    # TODO - you fill in here.

    print(f'PARAG {paragraph, keywords}')
    count = len(keywords)
    l, r = 0, 0
    m_diff = float('inf')
    j, k = 0, 0
    while r < len(paragraph):
        cur = paragraph[r]
        if cur in keywords:
            count -= 1
        r += 1
        while count == 0:
            l_cur = paragraph[l]
            diff = r - l
            if diff < m_diff:
                m_diff = diff
                j, k = l, r
            if l_cur in keywords:
                count += 1
            l += 1

    return Subarray(j, k)


@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure("Index out of range")

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure("Not all keywords are in the range")

    return end - start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "smallest_subarray_covering_set.py",
            "smallest_subarray_covering_set.tsv",
            find_smallest_subarray_covering_set_wrapper))
