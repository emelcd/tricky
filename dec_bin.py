def decimal_binary(n):
    binary = ""
    nm = n
    while n != 0:
        b = n%2
        n = n//2
        binary += str(b)

        print(n, b)
    print(str(nm) +" en binario es "+binary[::-1])

def binary_decimal(n):
    lim_exp = len(str(n))
    exp = 0
    num = []
    num_dec = [ ]
    total = 0
    for i in str(n):
        num += i
    num1 = num[::-1]
    while exp!=lim_exp:
        y = int(num1[exp])
        x = (2**exp)*y
        # print(2**exp)
        num_dec.append(str(x))
        exp += 1
        # print(exp, y, x)
    for number in num_dec:
        total += int(number)
        
    print(num_dec)
    
    print(total)
        
        
    
        
numeroD = int(input("número decimal: "))
decimal_binary(numeroD)
numeroB = int(input("número binario: "))
binary_decimal(numeroB)
