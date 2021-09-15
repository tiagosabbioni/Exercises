V = int(input())
outputNum = []

while(V // 16 != 0):
    outputNum.append(V % 16)
    V //= 16

outputNum.append(V % 16)
outputNum.reverse()

for i in range(len(outputNum)):
    if(outputNum[i] > 9):
        if(outputNum[i] == 10):
            outputNum[i] = 'A'
        elif(outputNum[i] == 11):
            outputNum[i] = 'B'
        elif(outputNum[i] == 12):
            outputNum[i] = 'C'
        elif(outputNum[i] == 13):
            outputNum[i] = 'D'
        elif(outputNum[i] == 14):
            outputNum[i] = 'E'
        else:
            outputNum[i] = 'F'

print(''.join(str(i) for i in outputNum))