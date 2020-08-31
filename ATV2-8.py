produto1 = float(input("VALOR DO PRIMEIRO PRODUTO: "))
produto2 = float(input("VALOR DO SEGUNDO PRODUTO: "))
produto3 = float(input("VALOR DO TERCEIRO PRODUTO: "))

MENOR = produto1

if (produto2 < MENOR ):
    MENOR = produto2

if (produto3 < MENOR ):

     MENOR = produto3

print ("O PRODUTO QUE VOCE DEVE COMPRAR É O DE VALOR  ", MENOR)