import os

#Variáveis globais
dir:str=''
arq:str=''
arquivo:str=''

def calc_fat(num:int):
    i:int=0
    fatorial = 1

    for i in range(1,num+1):
        fatorial *= i
    #Fim-loop
    return fatorial
#Fim cálculo do fatorial

def calc_div(serie,fat):
    serie += (1/fat)

    return serie
#Fim cálculo divisão

def grava(t,somatorio):
    global arquivo

    with open(arquivo,'a',encoding='utf-8') as file:
        file.write(f'Termo = {t:.6f} e o somatório = {somatorio:.6f}\n')
    #Fim with open

def main():
    global dir,arq,arquivo

    valor:int=0
    cont:int=0
    fatorial:int=0
    termo:int=0
    soma:float=0.0

    dir = '/tmp/exercicios/'

    #Verificando se existe e dando permissão
    os.makedirs(dir, exist_ok=True)
    os.chmod(dir,0o744)

    arq = 'ex36.txt'
    arquivo = dir + arq #/tmp/exercicios/ex36.txt

    #Recebendo o valor
    valor = int(input('Insira um valor: '))

    #Loop que calcula a série
    for cont in range(1,valor+1):
        fatorial = calc_fat(cont)
        termo = 1/fatorial
        soma = calc_div(soma,fatorial) #Soma vai acumular a série
        grava(termo,soma)
#Fim-main

if (__name__ == '__main__'):
    main()
#Chamando o main


