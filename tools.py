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
        superindeks = i + nøgle
        if superindeks > len(alfabet)-1:
            superindeks %= len(alfabet)
        out.append(alfabet[superindeks])
    return out


def caesarciffer(dictionary):
    out = []
    active = True
    while active:
        besked = input('Indtast besked til kryptering!!!!\n')
        if besked.isalpha():
            for i in range(len(besked)):
                out.append(dictionary[besked[i]])
            print(out)
            break
        else: print('Beskeden er ikke kun bogstaver!! Prøv igen!!!')

