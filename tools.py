#Tvinger brugeren til at vælge en numerisk nøgle
def vælgnøgle():
    active = True
    while active:
        out = input('selekt nøgle\n')
        if not out.isnumeric():
            print('Valgte nøgle er ikke validt! Vælg et nummer!\n')
        else:
            print('du har valgt '+str(out)+' som nøgle!')
            return int(out)

#Rykker bogstaverne af alfabetet afhængende af nøglens værdi.
def alfabetkonverter(alfabet, nøgle):
    out = []
    #tjekker om et bogstav skal loop tilbage til begyndelsen af alfabetet før den konverterer bogstavet.
    for i in range(len(str(alfabet))):
        superindeks = i + nøgle
        if superindeks > len(alfabet)-1:
            superindeks %= len(alfabet)
        out.append(alfabet[superindeks])
    return out

#Krypterer eller dekrypterer, afhængende af dictionary brugt.
def caesarciffer(dictionary):
    out = []
    active = True
    while active:
        besked = input('Indtast besked!\n').lower()
        if besked.replace(' ', '').isalpha(): #tjekker input om den kun indeholder bogstaver og mellemrum.
            for i in range(len(besked)):
                if besked[i] == ' ': #beholder mellemrum fra input til output.
                    out.append(' ')
                else: out.append(dictionary[besked[i]])
            out = ''.join(out) #sammensætter elementerne fra 'out' til 1 string.
            print(out)
            break
        else: print('Beskeden må kun indholde bogstaver og mellemrum!! Prøv igen!!!')