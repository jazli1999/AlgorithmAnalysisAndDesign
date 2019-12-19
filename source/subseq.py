def check(s, p):
    # s for sequence, p for pattern
    i = j = 0
    while i < len(s) and j < len(p):
        if s[i] == p[j]:
            j += 1
        i += 1
    if j == len(p):
        return True
    else:
        return False

if __name__ == '__main__':
    s1 = ['Amazon', 'Yahoo', 'eBay', 'Yahoo', 'Yahoo', 'Oracle']
    s2 = ['Yahoo', 'eBay', 'Yahoo', 'Oracle']
    print('{0}\n{1}\n{2}'.format(s1, s2, check(s1, s2)))