
"""
    Burrows-Wheeler Transform

    This algoritm rearranges the text for regrouped the similar characters

"""

import sys

def reverseBwt(txt):
    """
        reverseBwt(txt)
        - txt = text
        The first loop set the list at 0
        The imbricated loop set the list with text and the sorted
    """

    table = list()

    """ Initialize matrice """
    for j in range(0, len(txt)):
        table.append('')

    #for i in range(0, len(txt)):
    #    table = sorted(i + j for i, j in zip(txt, table))

    """ Heart of reverse algorithm """
    for i in range(0, len(txt)):
        for j in range(0, len(txt)):
            table[j] = txt[j] + table[j]
        table = sorted(table)
    return table

def write(path, txt):
    """
        write(path, txt)
        - path = path of output
        - txt = text
        Write in output file
    """
    fdout = open(path, 'w+')
    fdout.write(txt)
    fdout.close()

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print(" --------------------------------------------------------------\n",
                "Usage: python3 bwt_reverse.py <input> <output> <<key> or 'all'>\n",
                " - input = file transformed\n",
                " - output = file original, for 'all' put a folder\n"
                " - key = key is index of final array give by the transformation, if not know test all\n",
                "--------------------------------------------------------------")
    else:
        fdin = open(sys.argv[1], 'r')
        result = reverseBwt(fdin.read())
        if sys.argv[3] == 'all':
            for i in range(0, len(result)):
                write(sys.argv[2] + '/key.' + str(i), result[i])
        elif sys.argv[3].isdigit():
            write(sys.argv[2], result[int(sys.argv[3], 10)])

        fdin.close()
