
num = float(input("Informe um número: "))

if num % 3 == 0 and num % 5 == 0:
    print("É mutiplo de 3 e 5.")
elif num % 3 == 0:
    print("É mutiplo de 3.")
elif num % 5 == 0:
    print("É mutiplo de 5.")
else:
    print("Não é mutiplo de 3 nem de 5.")