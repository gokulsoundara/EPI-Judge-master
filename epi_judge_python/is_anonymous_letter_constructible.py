from test_framework import generic_test
import collections

def is_letter_constructible_from_magazine(letter_text, magazine_text):
    # TODO - you fill in here.
    # print(f'letter_text, magazine_text, {letter_text, magazine_text}')
    l, m = collections.Counter(letter_text), collections.Counter(magazine_text)

    for k,v in l.items():
        if k not in m or v > m.get(k,-1):
            return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
