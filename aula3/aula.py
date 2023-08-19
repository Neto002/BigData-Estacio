# 1 - Implemente o exemplo da 3 fase do MapReduce, inserindo em um dicionário a soma dos valroes de suas respectivas chaves.

dicionario = {
    "cat": [3, 4, 1], 
    "mouse": [1, 2]
}

dicionario_somas = {
    "cat": sum(dicionario["cat"]),
    "mouse": sum(dicionario["mouse"])
}

print(dicionario_somas)

# 2 - Leia o arquivo "mapa.txt" e faça a contagem de palavras do arquivo, inserindo esses dados em um dicionário chamado "contador".

with open('arquivos teste/mapa.txt', 'r') as file:
    lista_palavras = file.read().split()
    contador = {}
    for i in lista_palavras:
        contador[i] = lista_palavras.count(i)
    print(contador)

 
# 3 - Leia o resultado de um mapeamento gerado em um arquivo mapa_ 2.txt e faça a classificação (Sort) das chaves de forma ascendente e descendente.

import json

def ordena_chave(d: dict, reverse = False):
    return dict(sorted(d.items(), reverse=reverse))

arquivo = open('./arquivos teste/mapa_2.txt', 'r', encoding='utf-8')
aux = arquivo.read()
estudantes = json.loads(aux)

print(f'Dicionário original: {estudantes}')

print(f"Ordem crescente pela chave: {ordena_chave(estudantes)}")

print(f"Ordem decrescente pela chave: {ordena_chave(estudantes, reverse=True)}")


# 4 - Um mapeamento foi gerado, porém seus pares-chaves ficaram isolados em dois arquivos: "keys.txt" e "values.txt". Deseja-se unificar esses itens em um dicionário.

with open('./arquivos teste/keys.txt', 'r', encoding='utf-8') as file:
    keys = file.read().split()

with open('./arquivos teste/values.txt', 'r', encoding='utf-8') as file:
    values = file.read().split()

dicionario = dict(zip(keys, values))
print(dicionario)
