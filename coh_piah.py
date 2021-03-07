import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def n_palavras(texto):
    return len(separa_palavras(texto))

def caracteres_palavras(texto):
    '''Preenche arrays de frases e palavras'''
    sentencas = separa_sentencas(texto)
    frases = list()
    for i in sentencas:
        x = separa_frases(i)
        frases += x
    palavras = list()
    for i in frases:
        x = separa_palavras(i)
        palavras += x
    ''' Soma caracteres(sem pontuacao) do array das palavras'''
    return sum(len(s) for s in palavras)

def lista_palavras(texto):
    sentencas = separa_sentencas(texto)
    frases = list()
    for i in sentencas:
        x = separa_frases(i)
        frases += x
    palavras = list()
    for i in frases:
        x = separa_palavras(i)
        palavras += x
    return palavras

def n_sentencas(texto):
    return(len(separa_sentencas(texto)))

def caracteres_sentencas(texto):
    return sum(len(s) for s in separa_sentencas(texto))

def n_frases(texto):
    sentencas = separa_sentencas(texto)
    frases = list()
    for i in sentencas:
        x = separa_frases(i)
        frases += x
    return len(frases)

def caracteres_frases(texto):
    sentencas = separa_sentencas(texto)
    frases = list()
    for i in sentencas:
        x = separa_frases(i)
        frases += x
    return sum(len(s) for s in frases)
    

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    soma = 0
    for i in range(0, 6):
        soma += abs(as_a[i] - as_b[i])
    return soma/6
    pass

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    # Tamanho Médio da Palavra
    media_palavra = caracteres_palavras(texto)/n_palavras(texto)
    # Type - Token
    type_token = n_palavras_diferentes(lista_palavras(texto))/n_palavras(texto)
    # Hapax Legomana
    hapax_legomana = n_palavras_unicas(lista_palavras(texto))/n_palavras(texto)
    # Tamanho Médio da Sentença
    media_sentenca = caracteres_sentencas(texto)/n_sentencas(texto)
    # Complexidade da Sentença
    complex_sentenca = n_frases(texto)/n_sentencas(texto)
    # Tamanho Médio da Frase
    media_frase = caracteres_frases(texto)/n_frases(texto)

    # Retorna array contendo os traços de assinatura
    return [media_palavra, type_token, hapax_legomana, media_sentenca, complex_sentenca, media_frase]
        
    pass

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    # Cria Lista com Traços de cada texto
    lista_tracos = []
    for i in (textos):
        lista_tracos.append(calcula_assinatura(i))
    # Compara assinatura de entrada com assinatura dos textos
    lista_final = []
    for j in lista_tracos:
        lista_final.append((compara_assinatura(ass_cp, j)))
    # Devolve numero de texto com maior similiradidade com assinatura dada(menor valor)
    return lista_final.index(min(lista_final)) + 1
    
    pass


'''Função Main'''

ass_cp = le_assinatura()
textos = le_textos()
print("O autor do texto", avalia_textos(textos, ass_cp), "está infectado com COH-PIAH")
