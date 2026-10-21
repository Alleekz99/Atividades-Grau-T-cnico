peso = float(input("Digite o peso total dos peixes em kg: "))

limite = 50.0

multa = 4.00

if peso > limite:
    excesso = peso - limite
    valormulta = excesso * multa
    print(f"Peso excedente: {excesso:.2f} kg")
    print(f"Valor da multa: R$ {valormulta:.2f}")
else: 
    print("Não há excesso de peso, logo, não há multa.")
