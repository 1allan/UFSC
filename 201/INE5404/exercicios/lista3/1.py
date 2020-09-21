texto = None

path = input('Caminho para o arquivo: ')

with open(path, 'r') as f:
    texto = f.read()

def frequencia(txt):
    palavras = dict()
    txt = txt.split()
    for t in txt:
        if t not in palavras.keys():
            palavras[t] = 1
        else:
            palavras[t] += 1
    
    return palavras

frequencia(texto)
