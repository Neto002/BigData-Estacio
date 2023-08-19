'''from collections import Counter
print(Counter("mississipi"))'''


'''from collections import Counter

itens = Counter('mississipi')
itens = Counter(itens)

print(itens)

itens.update("missouri")
print(itens)'''

'''from collections import Counter

print(Counter(['B', 'B', 'A', 'B', 'C']))
print(Counter(A = 3, B = 5, C = 2))'''

'''from collections import Counter
lista = Counter(['B', 'B', 'A', 'B', 'C'])

frequente = lista.most_common(2)

print(f'Elemento mais comum: {frequente}')'''

# 1 - Leia os arquivos "contar1.txt" e "contar2.txt" faça a contagem de palavaras dos arquivos, somando as contagens das chaves em comum.

'''from collections import Counter
import json

contar1 = {}

with open("./arquivos teste/contar1.txt", "r", encoding='utf-8') as file:
    contar1 = Counter(json.loads(file.read()))
    print(contar1)

with open("./arquivos teste/contar2.txt", "r", encoding='utf-8') as file:
    contar1.update(Counter(json.loads(file.read())))

print(contar1)'''

'''from collections import ChainMap

dictA = {'a':1, 'b':2}
dictB = {'c':3, 'd':4}

dict_maps = ChainMap(dictA, dictB)

print(dict_maps)

dictD = {'e':5, 'f':6}

cadeia = dict_maps.new_child(dictD)

print(cadeia)'''

'''from collections import ChainMap
import json

arquivo = open("./arquivos teste/contar1.txt", "r", encoding='utf-8')
contador1 = arquivo.read()
contador1 = json.loads(contador1)

arquivo = open("./arquivos teste/contar2.txt", "r", encoding='utf-8')
contador2 = arquivo.read()
contador2 = json.loads(contador2)

print(ChainMap(contador1, contador2))'''

'''import math

lista1 = [1, 4, 9, 16, 25]
lista2 = map(math.sqrt, lista1)
# equivalente a lista2 = [math.sqrt(x) for x in lista1]

print(list(lista2))'''

'''def maior_zero(x):
    return x > 0

valores = [100, 8, -1, 3, 5, -9, 12]
print(list(filter(maior_zero, valores)))

# equivalente a print([x for x in valores if x > 0])'''

'''valores = [100, 8, -1, 3, 5, -9, 12]
print(list(filter(lambda x: x > 0, valores)))'''

'''numbers = [10, 12, 21, 33, 45, 55]
mapped_numbers = list(map(lambda x: x*2 + 3, numbers))
print(mapped_numbers)'''