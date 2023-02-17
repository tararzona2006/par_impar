# programa para verificar se um número es par o ímpar

# input
x = int(input("Digite um número: "))

# processamento
r = x % 2
if r == 0:
    msj = "par"
else:
    msj = "ímpar"

# output
print("el número" + str(x) + "es" + msj)

      




