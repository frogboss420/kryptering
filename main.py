import tools
alfabet = 'abcdefghijklmnopqrstuvwxyzæøå'
nøglealfabet = ''

nøgle = tools.vælgnøgle()

nøglealfabet = tools.alfabetkonverter(alfabet, nøgle)
caesaralfabet = dict(zip(alfabet,nøglealfabet))
omvendtdict = dict(zip(nøglealfabet,alfabet))

print(nøglealfabet)
print(caesaralfabet)
#main løkke
mainloop = True
while mainloop:
    decision = input('ENKRYPT, DEKRYPT, vælg NØGLE eller EXIT.')
    decision = str(decision.upper())
    if decision == 'ENKRYPT':
        tools.caesarciffer(caesaralfabet)
    elif decision == 'DEKRYPT':
        tools.caesarciffer(omvendtdict)
    elif decision == 'NØGLE':
        nøgle = tools.vælgnøgle()
        nøglealfabet = tools.alfabetkonverter(alfabet, nøgle)
        caesaralfabet = dict(zip(alfabet, nøglealfabet))
        omvendtdict = dict(zip(nøglealfabet, alfabet))
    elif decision == 'EXIT':
        break
    else:
        print('man what the hell man')