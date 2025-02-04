alfabet = 'abcdefghijklmnopqrstuvwxyzæøå'
nøglealfabet = ''

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

nøgle = vælgnøgle()

#main løkke
mainloop = True
while mainloop:
    decision = input('ENKRYPT, DEKRYPT, vælg NØGLE eller EXIT.')
    decision = str(decision.upper())
    if decision == 'ENKRYPT':
        print('yay')
    elif decision == 'DEKRYPT':
        print('yayy')
    elif decision == 'NØGLE':
        nøgle = vælgnøgle()
    elif decision == 'EXIT':
        break
    else:
        print('man what the hell man')