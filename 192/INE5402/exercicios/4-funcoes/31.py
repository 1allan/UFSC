a025 = 0
a2650 = 0
a5175 = 0
a76100 = 0

while True:
    n = float(input('Digita um número aí: '))

    if n in range(25):
        a025 += 1
    elif n in range(26, 51):
        a2650 += 1
    elif n in range(51, 76):
        a5175 += 1
    elif n in range(76, 101):
        a76100 += 1
    elif n < 0 :
        break

print(f'[0-25]: {a025}')
print(f'[26-50]: {a2650}')
print(f'[51-7  5]: {a5175}')
print(f'[76-100]: {a76100}')