n1 = int(input("primeiro valor: "))
n2 = int(input("segundo valor: "))
n3 = int(input(" terceiro valor: "))

MAIOR = n1

if (n2 > MAIOR ):
    MAIOR = n2

if (n3 > MAIOR ):
    MAIOR = n3

print ("MAIOR: ", MAIOR)

MENOR = n1

if (n2 < MENOR ):
    MENOR = n2

if (n3 < MENOR ):
     MENOR = n3

print ("MENOR: ", MENOR)