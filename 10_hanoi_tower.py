def move(n, source, dest, inter):
    if n >= 1:
        move(n-1, source, inter, dest)
        print('move {} --> {}'.format(source, dest))
        move(n-1, inter, dest, source)

move(3, 'A', 'C', 'B')