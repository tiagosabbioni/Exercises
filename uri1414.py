while True:
    T, N = map(int, input().split(" ", 2))
    if(T == 0):
        break
    maxPontos = N*3
    totalPontos = 0
    for i in range(T):
        time, pontosTime = input().split(" ", 2)
        pontosTime = int(pontosTime)
        totalPontos += pontosTime
    empates = (maxPontos - totalPontos)
    print(empates)