#tvinger brugeren til at vælge en numerisk nøgle
def vælgnøgle():
    active = True
    while active:
        out = input('selekt nøgle\n')
        if out.isnumeric() == False:
            print('Valgte nøgle er ikke validt! Vælg et nummer!')
        else:
            print('thank')
            return int(out)