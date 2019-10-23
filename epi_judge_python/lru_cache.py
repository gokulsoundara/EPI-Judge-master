from test_framework import generic_test
from test_framework.test_failure import TestFailure


class ListNode():
    def __init__(self, val=None, key=None, nex=None, prev=None):
        self.val = val
        self.key = key
        self.next = nex
        self.prev = prev


class LruCache:
    def __init__(self, capacity):
        self.c = capacity
        self.head = self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dic = {}

    def lookup(self, isbn):
        print(f'dici {self.dic, isbn}')
        if isbn not in self.dic:
            return -1
        node = self.dic[isbn]
        self._remove_node(node)
        self._add_node(node)
        return node.val

    def insert(self, isbn, price):
        if isbn in self.dic:
            node = self.dic[isbn]
            del self.dic[isbn]
            self._remove_node(node)
        else:
            node = ListNode(price, isbn)
        self.dic[isbn] = node
        if len(self.dic) >= self.c:
            mru = self.head.next
            self._remove_node(mru)
            del self.dic[mru.key]
        self._add_node(node)

    def erase(self, isbn):
        if isbn not in self.dic: return False
        node = self.dic[isbn]
        del self.dic[isbn]
        self._remove_node(node)
        return True

    def _add_node(self, node):
        temp = self.tail.prev
        temp.next, node.prev = node, temp
        self.tail.prev, node.next = node, self.tail

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


def run_test(commands):
    if len(commands) < 1 or commands[0][0] != 'LruCache':
        raise RuntimeError('Expected LruCache as first command')

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == 'lookup':
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure(
                    'Lookup: expected ' + str(cmd[2]) + ', got ' + str(result))
        elif cmd[0] == 'insert':
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == 'erase':
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure(
                    'Erase: expected ' + str(cmd[2]) + ', got ' + str(result))
        else:
            raise RuntimeError('Unexpected command ' + cmd[0])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lru_cache.py", 'lru_cache.tsv',
                                       run_test))
