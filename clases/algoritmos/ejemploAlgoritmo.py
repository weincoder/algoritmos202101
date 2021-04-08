#4,5,7,11,19
#numero 1 --->4 (2**0)+3
#numero 2 --->5 (2**1)+3
#numero 3 --->7 (2**2)+3
#numero 4 --->11 (2**3)+3
#numero 5 --->19 (2**4)+3

def sucesion(n):
    return (2**(n-1)) + 3 
print(sucesion(5))