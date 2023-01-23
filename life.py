import time
import os

def matriz_inicial():
    return [
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,1,0,0,0,0],
        [0,0,0,1,1,1,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
    ]

os.system("clear")

def desenha(m):
    D = {0: '\U0001F480', 1:'\U0001F600'}
    for i in range(len(m)):
        m[i]
        print(''.join([D[e] for e in m[i]]))

def countvv(m, i, j):
    dcvs = [
        (-1,-1),(-1,0),(-1,1),
        (0,-1),(0,1),
        (1,-1),(1,0),(1,1),
    ]
    cvs = [(i+dcv[0], j+dcv[1])for dcv in dcvs if 0<= i+dcv[0] < len(m) and 0<= j+dcv[1] < len(m[0])]
    return len([1 for cv in cvs if m[cv[0]][cv[1]] == 1])

def atualiza(m):
    nm = [[0 for e in linha] for linha in m]
    for i in range(len(m)):
        for j in range(len(m[i])):
            count_vv = countvv(m, i, j)
            if m[i][j] == 1:
                if count_vv in {0,1}:
                    nm[i][j] = 0
                elif count_vv >= 4:
                    nm[i][j] = 0
                else:
                    nm[i][j] = 1
            else:
                if count_vv == 3:
                    nm[i][j] = 1
                else:
                    nm[i][j] = 0
    return nm

def dorme():
    time.sleep(1)

m = matriz_inicial()

while True:
    desenha(m)
    dorme()
    m = atualiza(m)