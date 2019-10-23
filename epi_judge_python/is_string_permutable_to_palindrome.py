from test_framework import generic_test
import collections


def can_form_palindrome(s):
    if not s: return True # edified
    dic = collections.Counter(s) # dic {e:2, d:2,i:2,f:1
    flag = True if len(s) % 2 else False # True

    for k, v in dic.items():
        if v % 2:
            if flag:
                flag = False
            else:
                return False

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
