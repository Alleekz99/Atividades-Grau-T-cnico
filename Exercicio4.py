n1 = float(input("Insira a 1º nota: "))
n2 = float(input("Insira a 2º nota: "))
n3 = float(input("Insira a 3° nota: "))
n4 = float(input("Insira a 4° nota: "))

media = (n1 + n2 + n3 + n4) // 4

if media >= 7:
    print("você passou")
else:
    print("você não passou")


print ("A média das notas é: ", media)