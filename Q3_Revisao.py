'''
Sua organização acaba de contratar uma estagiária para trabalhar no
Suporte de Informática, com a intenção de fazer um levantamento nas
sucatas encontradas nesta área. A primeira tarefa dela é testar todos os
cerca de 10 mouses que se encontram lá, testando e anotando o estado
de cada um deles, para verificar o que se pode aproveitar deles.
a. Foi requisitado que você desenvolva um programa para registrar este
levantamento. O programa deverá receber um número indeterminado
de entradas, cada uma contendo: um número de identificação do
mouse o tipo de defeito:
b. necessita da esfera;
c. necessita de limpeza; a.necessita troca do cabo ou
conector; a.quebrado ou inutilizado. Uma identificação igual a zero
encerra o programa. Ao final o programa deverá emitir o seguinte
relatório:

'''
mouse=list()
situacao=''
situacao1=7
situacao2=1
situacao3=1
situacao4=1
perc1=0
perc2=0
perc3=0
perc4=0
total=10

mouse = ['1','necessita da esfera','2','necessita da esfera','3','necessita de limpeza','4','necessita troca do cabo ou conector',
'5','quebrado ou inutilizado','6','necessita da esfera','7','necessita da esfera','8','necessita da esfera','9','necessita da esfera','10','necessita da esfera']
print(mouse)



while True:
    adicionar = str(input('Deseja adicionar novo mouse? (s/n)')).upper()
    if adicionar != 'S':
        break
    total+=1
    indentificacao= int(input('Insira o ID: '))
    if indentificacao == 0:
        break
    mouse.append(indentificacao)
    situacao=str(input('''Insira a situação ou 0 para sair:: 
                                ''1-necessita da esfera
                                  2- necessita de limpeza
                                  3- necessita troca do cabo ou conector
                                  4- quebrado ou inutilizado.                            
                                   >_ '''))
    if situacao == '1':
        mouse.append("necessita da esfera") 
        situacao1+=1
    if situacao == '2':
        mouse.append("necessita de limpeza") 
        situacao2+=1
    if situacao == '3':
        mouse.append("necessita troca do cabo ou conector") 
        situacao3+=1
    if situacao == '4':
        mouse.append("quebrado ou inutilizado")
        situacao4+=1 


perc1=((situacao1*100)/total)
perc2=((situacao2*100)/total)
perc3=((situacao3*100)/total)
perc4=((situacao4*100)/total)

print('Quantidade de mouses:',total)
print('Situação                             Quantidade                Percentual')
print('1-necessita da esfera'                ,'\t\t\t',situacao1,'\t\t\t',perc1, '%')
print('2-necessita de limpeza'               ,'\t\t\t',situacao2,'\t\t\t',perc2, '%')
print('3-necessita troca do cabo ou conector','\t',situacao3,'\t\t\t',perc3, '%')
print('4-quebrado ou inutilizado'            ,'\t\t',situacao4,'\t\t\t',perc4, '%')
#continuar = str(input('Deseja continuar?(S/N) ')).upper()
#if continuar != 'S':
#break



 
