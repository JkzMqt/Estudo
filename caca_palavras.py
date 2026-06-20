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
                            posicao.append(f"{palavra}: {n} {m}")
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