import os

#Variáveis globais
dir:str=''
arq:str=''
lista=[]
arq_ent:str=''
arq_saida:str=''

def leitura(entrada):
    lista_num=[]
    file=''
    linha:str=''
    numero:int=0

    if(os.path.exists(entrada) and os.path.isfile(entrada)):
        
        with open(entrada,'r',encoding='utf-8') as file:
            #FOR EACH
            for linha in file:

                linha=linha.strip() #Tirando o \n

                #Verificando se há os termos 'maior' ou 'menor'
                if ('maior' not in linha and 'menor' not in linha):
                    numero = int(float(linha)) #Convertendo de string pra int

                    #Verificando se é múltiplo de 5 
                    if(numero % 5 ==0):
                        lista_num.append(numero)
                    #Fim-condicional 3
                #Fim-condicional 2
            #Fim-loop que percorre a lista
        #Fim with open
        return lista_num
    #Fim-condicional 1
#Fim-leitura

def grava(lis,saida):
    file:str=''
     
    with open(saida,'w',encoding='utf-8') as file:
        for n in lis:
            file.write(str(n)+'\n') #Gravando a nova lista
        #Fim-loop
    #Fim with open
#Fim-grava

def main():
    global dir,arq,lista,arq_ent,arq_saida

    dir = '/tmp/exercicios/' #Caminho

    #Verificando se já existe e dando permissão
    os.makedirs(dir, exist_ok=True)
    os.chmod(dir, 0o744)

    arq = 'multiplos5.txt'

    arq_ent = '/tmp/exercicios/ex38.txt' #Arquivo de entrada
    arq_saida = dir + arq  #/tmp/exercicios/multiplos5.txt

    lista = leitura(arq_ent) #Retorno dentro da variável lista
    grava(lista,arq_saida)
#Fim-main

if (__name__ == '__main__'):
    main()
#Chamando o main
