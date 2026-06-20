#Exercicios-lab-06-05-26

# utilitários
def printar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end="  ")
        print('')
def matrizpersonalizada():
    matriz=[[6,2,3],
            [4,5,80000],
            [66,8,9]]
    return matriz

#1) Escreva uma função que crie uma matriz de inteiros de ordem m x n, contendo valores aleatórios entre 0 e k
def matriz_random():
    import random
    m,n=map(int,input().split())
    k=int(input())
    matriz=[]
    for i in range(m):
      matriz.append([])
      for j in range(n):
         matriz[i].append(random.randint(0,k))
    return matriz

#2) Escreva uma função em Python que receba uma matriz A e retorne a sua cópia.
def copy_matriz(matriz):
    copia=[]
    for i in range(len(matriz)):
        copia.append([])
        for j in range(len(matriz[0])):
            copia[i].append(matriz[i][j])
    return copia

#3) Escreva uma função que receba uma matriz de float A de ordem n x m, e verifique se ela é diagonal dominante, isto é, 
#   se o valor de cada elemento na diagonal principal é maior que a soma da magnitude dos elementos na linha a que ele pertence.
def matriz_diagdom(matriz):
    dom=True
    for i in range(len(matriz)):
        soma=0
        for j in range(len(matriz[0])):
            soma+=abs(matriz[i][j])
        soma-=matriz[i][i]
        if matriz[i][i]<=soma:
            dom=False
    return dom

#4) Escreva uma função em Python que receba uma matriz A e um vetor b, ambos de float, e retorne seu produto.
def vetorxmatriz(vetor,matriz):
    resultado=[]
    for i in range(len(matriz)):
        conta=0
        for j in range(len(matriz[0])):
            conta+=(matriz[j][i]*vetor[j])
        resultado.append(conta)
    return resultado

def matrizxmatriz(mat1,mat2):
    resultado=[]
    for i in range(len(mat1)): #percorre as x linhas da primeira matriz
        resultado.append([])
        for k in range(len(mat2[0])): #percorre as z colunas da segunda matriz
            conta=0
            for j in range (len(mat1[0])): #percorre as y colunas da primeira matriz
                conta+=(mat1[i][j]*mat2[j][k])
            resultado[i].append(conta)
    return resultado

def maior_visinho(matriz):
    maiores=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            maior=True
            for x in range(i-1,i+2):
                if x>=0 and x<len(matriz):
                    for y in range(j-1,j+2):
                        if y>=0 and y<len(matriz[0]):
                            if matriz[i][j]<=matriz[x][y] and (x!=i or y!=j):
                                maior=False
            if maior==True:
                maiores.append((i,j))
    return maiores

def caca_palavras(matriz,palavras):
    posicao=[]
    #para cada palavra, ver se letra bate com palavra
    for palavra in palavras:
        for n in range(len(matriz)):
            for m in range(len(matriz[0])):

    #excessão caso palavra tenha só uma letra                 
                if palavra[0]==matriz[n][m]:
                    if len(palavra)==1:
                        if (f"{palavra}: {n} {m}") not in posicao:
                            posicao.append((n,m))
                        continue

    #se letra bate ver se alguma das letras ao redor bate
                    for x in range(n-1,n+2):
                        if x>=0 and x<len(matriz):

                            for y in range(m-1,m+2):
                                if y>=0 and y<len(matriz[0]):

    #pular a verificação de si mesmo, para evitar que palavras com letras repetidas considerem a msm posicao 2x
                                    if x==n and y==m:
                                        continue

                                    if palavra[1]==matriz[x][y]:

    #se bate, verificar se prox letra na mesma direcao bate
                                        flag=True
                                        a,b=x,y
                                        deltan,deltam=x-n,y-m
                                        for k in range(2,len(palavra)):
                                            if a+deltan<0 or b+deltam<0 or a+deltan>=len(matriz) or b+deltam>=len(matriz[0]):
                                                flag=False
                                                break
                                            if matriz[a+deltan][b+deltam]!=palavra[k]:
                                                flag=False
                                                break
                                            a+=deltan
                                            b+=deltam
                                        if flag:
                                            if (f"{palavra}: {n} {m}") not in posicao:
                                                posicao.append(f"{palavra}: {n} {m}")
    return posicao
#------------AREA DE TESTES-------------
matriz=[
        ["a","b","c","d"],
        ["t","e","s","g"],
        ["h","a","m","o"],
        ["y","l","m","a"]]
palavras=["te","amo","yas"]

print(caca_palavras(matriz,palavras))