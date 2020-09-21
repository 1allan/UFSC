from .util import STOP_WORDS

def apaga(dicionario):
    for key, value in dicionario.items()
        if key in STOP_WORDS:
            del key[value]