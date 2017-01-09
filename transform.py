
"""
    Burrows-Wheeler Transform

    This algoritm rearranges the text for regrouped the similar characters

"""

import sys

def bwt(txt):
    """
        suffixArray(txt)
        - txt = text
        The first loop transform text in list with the text and index.
        The list sorted by the first argument list so the text
        The second loop recover the second argument for found index minus one and found the key
    """
    matrice = list()
    t = list()

    for i in range(0, len(txt)):
        matrice.append((''.join(txt[i:]), i))

    matrice = sorted(matrice)

    for i in range(0, len(matrice)):
        t.append(txt[matrice[i][1] - 1])
        if matrice[i][0] == txt:
            print("Key is", i)
    return ''.join(t)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(" --------------------------------------------------------------\n",
                "Usage: python3 bwt_transform.py <input> <output>\n",
                " - input = file original\n",
                " - output = file transformed\n"
                "--------------------------------------------------------------")
    else:
        fdin = open(sys.argv[1], 'r')
        result = bwt(fdin.read())

        fdout = open(sys.argv[2], 'w+')
        fdout.write(result)

        fdin.close()
        fdout.close()
