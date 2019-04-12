import heapq

portfolio = [{'name': 'IBM', 'shares': 100, 'price': 91.1},
             {'name': 'AAPL', 'shares': 50, 'price': 543.22},
             {'name': 'FB', 'shares': 200, 'price': 21.09},
             {'name': 'HPQ', 'shares': 35, 'price': 31.75},
             {'name': 'YHOO', 'shares': 45, 'price': 16.35},
             {'name': 'ACME', 'shares': 75, 'price': 115.65}]


def sorter(s):
    return s['price']


nlargest = heapq.nlargest(2, portfolio, key=lambda s: s['price'])
nsmallest = heapq.nsmallest(2, portfolio, key=lambda s: s['price'])
print(nlargest)
print(nsmallest)

lt = list([84, 64, 44, 11, 21, 43, 23, 25])
heapq.heapify(lt)
print(lt)

# Use heapq only when n is very small to size of list
