import tools
alfabet = 'abcdefghijklmnopqrstuvwxyzæøå'
nøglealfabet = ''


nøgle = tools.vælgnøgle()
nøglealfabet = tools.alfabetkonverter(alfabet, nøgle)
caesaralfabet = dict(zip(alfabet,nøglealfabet))
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
        print('yayy')
    elif decision == 'NØGLE':
        nøgle = tools.vælgnøgle()
    elif decision == 'EXIT':
        break
    else:
        print('man what the hell man')