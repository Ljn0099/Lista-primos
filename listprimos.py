primoa = False

def primo(apri):
    comprobar = 1
    comprobado = 0
    while comprobar != apri:
        comprobar = comprobar + 1
        if apri % comprobar == 0:
            comprobado = comprobado + 1
    if comprobado == 1:
        global primoa
        primoa = True
    else:
        primoa = False

def listprimo(longa):
    comprobar = 0
    alistprimos = []
    while comprobar < longa:
        comprobar = comprobar + 1
        primo(comprobar)
        if primoa == 1:
            alistprimos.extend([comprobar])
    print(alistprimos)

listprimo(10)
