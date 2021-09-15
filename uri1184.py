operacao = input()
soma = 0

matriz = 12*[0]
for i in range(len(matriz)):
    matriz[i] = 12*[0]

for i in range(len(matriz)):
    for j in range(len(matriz)):
        matriz[i][j] = float(input())

for i in range(1, len(matriz)):
    for j in range(0, i):
        soma += matriz[i][j]
        #print(f'Somando {(soma-matriz[i][j])} com {matriz[i][j]} temos {soma}')

if(operacao == 'M'):
    soma /= ((len(matriz)*len(matriz[0]))-len(matriz))/2

print(f'{soma:.1f}')