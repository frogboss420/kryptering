import tools #Giver adgang til funktioner fra tools.py
alfabet = 'abcdefghijklmnopqrstuvwxyzæøå'

#Brugeren vælger nøgle til kryptering ved opstart.
nøgle = tools.vælgnøgle()
nøglealfabet = tools.alfabetkonverter(alfabet, nøgle) #bruges til at definere dictionaries til kryptering/dekryptering.
caesaralfabet = dict(zip(alfabet,nøglealfabet)) #krypterings dictionary
omvendtdict = dict(zip(nøglealfabet,alfabet)) #dekrypterings dictionary

#Løkke for at tillade brugeren til at lave flere kommandoer i en session.
mainloop = True
while mainloop:
    #Brugeren vælger hvilken kommando de vil bruge.
    decision = input('KRYPTER, DEKRYPTER, vælg ny NØGLE eller EXIT.\n')
    decision = str(decision.upper())

    #kryptering
    if decision == 'KRYPTER':
        tools.caesarciffer(caesaralfabet)

    #dekryptering
    elif decision == 'DEKRYPTER':
        tools.caesarciffer(omvendtdict)

    #vælg ny nøgle
    elif decision == 'NØGLE':
        nøgle = tools.vælgnøgle()
        nøglealfabet = tools.alfabetkonverter(alfabet, nøgle)
        caesaralfabet = dict(zip(alfabet, nøglealfabet))
        omvendtdict = dict(zip(nøglealfabet, alfabet))

    #stop løkken
    elif decision == 'EXIT':
        break

    #fejlbesked ved forkert input.
    else:
        print('Vælg venligst en af følgende muligheder:')