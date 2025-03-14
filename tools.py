#tvinger brugeren til at vælge en numerisk nøgle
def vælgnøgle():
    active = True
    while active:
        out = input('selekt nøgle\n')
        if out.isnumeric() == False:
            print('Valgte nøgle er ikke validt! Vælg et nummer!\n')
        else:
            print('thank\n')
            active = False
            return int(out)

def alfabetkonverter(alfabet, nøgle):
    out = []
    for i in range(len(str(alfabet))):


def caesarciffer(nøgle):
    out = []
    active = True
    while active:
        besked = input('Indtast besked til kryptering!!!!\n')
        if besked.isalpha():
            for i in range(len(besked)):
                out.append(besked[i])
            print(out)
            break
        else: print('Beskeden er ikke kun bogstaver!! Prøv igen!!!')

