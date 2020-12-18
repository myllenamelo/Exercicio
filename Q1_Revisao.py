faixaSal = [[200, 299], [300, 399], [400, 499], [500, 599], [600, 699],[700, 799], [800, 899], [900, 999]]
cont = [0] * len(faixaSal)
vendas = 0
salario= 0
i=0


def CalculaSal (venda):
   return ((venda * 9)/100) + 200


print("Insira um valor negativo para sair. ")
while vendas != -1:
    vendas = float(input("Valor das vendas: R$ "))
    if vendas != -1:
        salario = CalculaSal(vendas)
    if salario < 1000:
        for i in range(8):
            if (salario > faixaSal[i][0]) and (salario < faixaSal[i][1]):
                cont[i] += 1
    else:
        cont[8] += 1
    vendas = int(input("Digite o valor das vendas:"))


print("Quantidade de vendedores nos intervalos de valores:")
for i in range(0, len(faixaSal)) :
    print(faixaSal[i]," : ", cont[i])
