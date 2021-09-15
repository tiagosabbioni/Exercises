X = int(input())
listaNum = X*[None]

for i in range(X):
    listaNum[i] = int(input())

listaOrdenada = X*[None]
listaOrdenada = sorted(set(listaNum))

for i in range(len(listaOrdenada)):
    print(f'{listaOrdenada[i]} aparece {listaNum.count(listaOrdenada[i])} vez(es)')