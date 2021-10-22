def primo():
    flag = 0
    while(flag == 0):
        n = int(input("Insert the number to be verified:\n"))
        if(n <= 9223372036854775807):
            flag = 1
    divisors = 0
    for i in range(1, n+1):
        if(n % i == 0):
            divisors += 1
    print(f'Divisors: {divisors}')

primo()