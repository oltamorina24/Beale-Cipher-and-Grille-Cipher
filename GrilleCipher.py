
import random

def gjenero_grille(n):
    vrimat = set()
    perdorur = set()

    while len(vrimat) < (n*n)//4:
        r = random.randint(0, n-1)
        c = random.randint(0, n-1)

        poz = [(r, c)]
        for _ in range(3):
            r, c = c, n - 1 - r
            poz.append((r, c))
        if all(p not in perdorur for p in poz):
            vrimat.add(poz[0])
            for p in poz:
                perdorur.add(p)

    return list(vrimat)

def rrotullo(vrimat, n):
    return [(c, n-1-r) for r, c in vrimat]

def enkripto(mesazhi, n, vrimat):
    mesazhi = mesazhi.ljust(n*n, 'X')
    matrica = [['']*n for _ in range(n)]

    index = 0
    aktuale = vrimat.copy()

    for _ in range(4):
        for r, c in aktuale:
            matrica[r][c] = mesazhi[index]
            index += 1
        aktuale = rrotullo(aktuale, n)

    return "".join("".join(r) for r in matrica)

def dekripto(cipher, n, vrimat):
    matrica = [list(cipher[i:i+n]) for i in range(0, len(cipher), n)]

    rezultat = ""
    aktuale = vrimat.copy()

    for _ in range(4):
        for r, c in aktuale:
            rezultat += matrica[r][c]
        aktuale = rrotullo(aktuale, n)

    return rezultat.rstrip('X')

vrimat_global = None
n_global = None
