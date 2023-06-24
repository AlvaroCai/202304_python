for i in range(151):
    print (i)

for i in range(5, 1001):
    if i % 5 == 0:
        print(i)


for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)
 
impares = 0
for i in range(1, 500001, 2):
    impares += i
print("La suma de los enteros impares del 0 al 500,000 es:", impares)

for numero in range(2018, -1, -4):
    print(numero)

lowNum = 2
highNum = 9
mult = 3

for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)
