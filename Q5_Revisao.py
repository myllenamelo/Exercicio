'''
Construa uma função que receba uma string como parâmetro e devolva
outra string com os carateres embaralhados. Por exemplo: se função
receber a palavra python, pode retornar npthyo, ophty ou qualquer outra
combinação possível, de forma aleatória. Padronize em sua função que
todos os caracteres serão devolvidos em caixa alta ou caixa baixa,
independentemente de como foram digitado.
'''

import random

def embaralhando(palavra):
    novaPalavra = ''
    novaPalavra = random.sample(palavra.lower(), len(palavra))  
    print('Palavra invertida: ',''.join(novaPalavra))


embaralhando('BANANA')