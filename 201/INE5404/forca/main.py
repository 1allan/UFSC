from random import randint

from stickman import state

alphabet = list('abcdefghijklmnopqrstuvwxyz')
word = [alphabet[randint(0, 25)] for _ in range(randint(3, 15))]
placeholder = ['_'] * len(word)

print('\nTente descobrir a palavra e libertá-lo-ei >:^)')

gone_letters = []
fails = 0
while True:
    print(word)
    print(state[4 - fails])
    print('Palavra:', ''.join(placeholder))
    print('Letras digitadas:', ', '.join(gone_letters))
    print('Erros:', fails)
    letter = input('Letra: ')

    if letter not in gone_letters:
        gone_letters.append(letter)
    
    if letter in word:
        for i in range(len(word)):
            if letter == word[i]:
                placeholder[i] = letter
    else:
        fails += 1

    if fails == 5:
        print('\nA cadeira foi puxada. Estás morto.')
        print('"Press "F" to pay respect" :^)')
        # Please, tell me you understood the reference >:(
        # youtube.com/watch?v=TtMzTGfs-fc

        if input().upper() == 'F':
            print('Não há respeito para infratores >:^)')
        
        break

    if '_' not in placeholder:
        print('\nEscapaste da forca! :o')
        print('clap clap clap clap clap')
        break

    print('\n')