def highlight(word, line):
    return line.replace(word, '\x1b[31m{}\x1b[0m'.format(word))


def search(word, file):
    '''
    search for a text in a file
    and return latest line with previous lines
    which contains the text
    '''
    current_line = None
    for line in f:
        if word in line:
            current_line = highlight(word, line)
            yield current_line


if __name__ == '__main__':
    word = 'Django'
    with open('sometext.txt') as f:
        for line in search(word, f):
            print(line)
    print('-x-'*30)
