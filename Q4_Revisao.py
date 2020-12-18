'''
Faça um programa que receba a temperatura média de cada mês do ano
e armazene-as em uma lista. Após isto, calcule a média anual das
temperaturas e mostre todas as temperaturas acima da média anual, e
em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 –
Fevereiro, . . . ).
'''


temperatura=list()
meses=list()
meses=['janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
temperatura.append(int(input('Janeiro: ')))
temperatura.append(int(input('Fevereiro: ')))
temperatura.append(int(input('Março: ')))
temperatura.append(int(input('Abril: ')))
temperatura.append(int(input('Maio: ')))
temperatura.append(int(input('Junho: ')))
temperatura.append(int(input('Julho: ')))
temperatura.append(int(input('Agosto: ')))
temperatura.append(int(input('Setembro: ')))
temperatura.append(int(input('Outubro: ')))
temperatura.append(int(input('Novembro: ')))
temperatura.append(int(input('Dezembro: ')))
media = sum(temperatura) / len(temperatura)
print(f'A média anual de temperatura é {media}')
for i in range(12):
    if temperatura[i] > media:
        print("Temperatura acima da média ",
              temperatura[i], "ºC", meses[i])
