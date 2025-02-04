import tools
alfabet = 'abcdefghijklmnopqrstuvwxyzæøå'
nøglealfabet = ''


nøgle = tools.vælgnøgle()

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
        nøgle = tools.vælgnøgle()
    elif decision == 'EXIT':
        break
    else:
        print('man what the hell man')