import heapq


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item {!r}'.format(self.name)


class PriorityQueue:
    def __init__(self):
        self._heap = list()
        # _index is used to act as tie breaker
        # if two priorities are equal. E.g. two tuples
        # (1, 'a') and (1, 'b') can't be compared truly
        # Hence we use index on top of priority to preserve
        # the order of addition of task
        self._index = 0

    def push(self, item, priority):
        # tup1 = (1, 1, 'a')
        # tup2 = (1, 2, 'a')
        # tup1 < tup2 -> True
        # tup1 == tup2 -> False
        heapq.heappush(self._heap, (-priority, self._index, item))
        self._index += 1

    def heapMin(self):
        return self._heap[0][-1]

    def extractHeapMin(self):
        return heapq.heappop(self._heap)[-1]

    def __repr__(self):
        output = ''
        for i in self._heap:
            output += 'P\"{}\" [{}] {}\n'.format(i[0], i[1], i[2])
        return output


if __name__ == '__main__':
    item1 = Item('1')
    item2 = Item('2')
    item6 = Item('6')
    item3 = Item('3')
    item4 = Item('4')
    item5 = Item('5')
    pq = PriorityQueue()
    pq.push(item1, 10)
    pq.push(item2, 12)
    pq.push(item6, 10)
    pq.push(item3, 3)
    pq.push(item4, 5)
    pq.push(item5, 1)
    print(pq)
    print(pq.extractHeapMin())
    print(pq)
    print(pq.extractHeapMin())
    print(pq)
    print(pq.extractHeapMin())
    print(pq)
