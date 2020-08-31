a = int(input('Escreva um número: '))
b = int(input('Escreva um número: '))
c = int(input('Escreva um numero :'))


if a < c: 
    a, c = c, a 
if a < b: 
    a, b = b, a 
if b < c: 
    b, c = c, b 

    print('A ordem decrescente é, ', a , b , c )