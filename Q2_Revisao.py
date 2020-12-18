'''
Faça um programa que carregue uma lista com os modelos de cinco
carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma
outra lista com o consumo desses carros, isto é, quantos quilômetros cada
um desses carros faz com um litro de combustível. Calcule e mostre:
a. O modelo do carro mais econômico;
b. Quantos litros de combustível cada um dos carros cadastrados
consome para percorrer uma distância de 1000 quilômetros e
quanto isto custará, considerando um que a gasolina custe R$ 4,93
o litro. Abaixo segue uma tela de exemplo. A disposição das
informações deve ser o mais próxima possível ao exemplo. Os
dados são fictícios e podem mudar a cada execução do programa.
'''


modelos=list()
consumo=list()
consumokm=list()


modelos=['uno','celta','corsa','voyage','fusca']
consumo=[5,10,15,20,25]

for i in range(5):
    print("%s\t\t%s\t\t%.2f" %
          (str(i+1), modelos[i], consumo[i]))

economico = max(consumo)
print (economico)

for i in range(5):
    litros = 1000/consumo[i]
    consumo.append(litros*4.93)
    print(i+1, '-', modelos[i], '-', consumo[i],
          '- ', "%.2f" % litros, ' litros', ' - R$ ', "%.2f" % consumo[i])
menor = min(consumo)
modeloconsumo = consumo.index(menor)
print('O modelo que consume menos é o', modelos[modeloconsumo])






