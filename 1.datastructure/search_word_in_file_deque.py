'''
Keeping a limited history is a perfect use for a
collections.deque. For example, the following code performs
a simple text match on a sequence of lines and yields the
matching line along with the previous N lines of context when found:
'''

from collections import deque


def highlight(word, line):
    return line.replace(word, '\x1b[31m{}\x1b[0m'.format(word))


def search(word, file, n=5):
    '''
    search for a text in a file
    and return latest line with previous n lines
    which contains the text
    '''
    prev_lines = deque(maxlen=n)
    for line in f:
        if word in line:
            current_line = highlight(word, line)
            yield current_line, prev_lines
            prev_lines.append(current_line)


if __name__ == '__main__':
    word = 'the'
    n = 3
    with open('sometext.txt') as f:
        for line, prev_lines in search(word, f, n):
            for pline in prev_lines:
                print(pline)
            print(line)
            print('-x-'*30)
