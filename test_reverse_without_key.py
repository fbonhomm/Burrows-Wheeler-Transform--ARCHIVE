
import sys

"""
    Usage: python3 test_reverse_without_key.py <txt>
"""

def table1(txt):
    occ = dict()
    info = list()

    for i in range(0, len(txt)):
        if txt[i] in occ:
            occ[txt[i]] += 1
        else:
            occ[txt[i]] = 0
        info.append((i, txt[i], occ[txt[i]]))
    return info, sorted(occ.items())

def table2(occ):
    table = dict()
    i = 0
    for c, count in occ:
        table[c] = i
        i += (count + 1)
    return table

def reverse(info, pos, txt):
    size = len(txt) - 1

    c = txt[size]
    i = 0
    result = ''

    while size >= 0:
        i = pos[c] + info[i][2]
        c = txt[i]
        result = c + result
        size -= 1
    return result

if __name__ == '__main__':
    info, occ = table1(sys.argv[1])
    pos = table2(occ)
    result = reverse(info, pos, sys.argv[1])
    print(result)
