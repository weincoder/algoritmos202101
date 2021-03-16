import time
tiempInicial = time.time()
print('hola a todos')
time.sleep(2)
tiempoFinal = time.time()
delta = tiempoFinal -tiempInicial
print(delta)

#-----inicio conteo----#
tiempInicial = time.time()
#---instrucciones----#
print('hola a todos')
x = 8
for i in range(x):
    print(i)
#---cierre de conteo--#
tiempoFinal = time.time()
delta = tiempoFinal -tiempInicial
print(delta)


#-----inicio conteo----#
tiempInicial = time.time()
#---instrucciones----#
print('hola a todos')
x = 123
for i in range(x):
    for j in range(x):
        print(j)
#---cierre de conteo--#
tiempoFinal = time.time()
delta = tiempoFinal -tiempInicial
print(delta)

