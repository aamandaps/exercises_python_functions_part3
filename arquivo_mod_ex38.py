import os

#Variáveis globais
dir:str=''
arq:str=''
valor:float=0.0
menor:float=0.0
maior:float=0.0

def entrada():
    global valor

    valor = float(input('Insira um número: '))
#Fim-entrada

def calculo(num):
    global maior,menor

    #Verificando e atualizando os valores
    if num>maior and num>=0:
        maior=num
    #Fim-condicional maior
    if num<menor and num>=0:
        menor=num
    #Fim-condicional menor
#Fim-calculo

def grava(lista,arqv,n,ma,me):
    file:str=''

    with open(arqv,'w',encoding='utf-8') as file:
        #FOR EACH
        for n in lista:   
            file.write(str(n)+'\n') #Convertendo pra string e colocando quebra de linha
        #Fim-loop que percorre a lista

        file.write(f'O maior é: {ma}'+'\n')
        file.write(f'O menor é: {me}'+'\n')
    #Fim with open
#Fim-grava


def main():
    global dir,arq,valor,maior,menor

    arquivo:str=''
    armazenamento=[] 
    i:int=0

    dir = '/tmp/exercicios/' #Caminho

    #Verificando se já existe e dando permissão 
    os.makedirs(dir, exist_ok=True)
    os.chmod(dir,0o744)

    arq='ex38.txt'
    arquivo= dir + arq  #/tmp/exercicios/ex38.txt

    entrada() #Entrada que define os primeiros valores
    armazenamento.append(valor) #Vai guardar os valores para serem passados como parâmetros depois 
    maior = valor
    menor = valor


    #Loop que chama a entrada e o calculo
    for i in range (1,10):
        entrada()
        armazenamento.append(valor)
        calculo(valor)
    #Fim-loop

    grava(armazenamento,arquivo,valor,maior,menor)

#Fim-main

if (__name__ == '__main__'):
    main()
#Chamando o main
