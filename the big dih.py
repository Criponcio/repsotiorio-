import random

numero_secreto = random.randint(1, 100)

print("print")
print("advinhe o numero de 1-100")

contador = 7
acertou = False

while contador > 0:

    print(f'voce ta tendo {contador} tentavias ainda meu')

    tentativa = int(input("mete o loco e chuta o numero > "))
    contador -= 1

    if tentativa == numero_secreto:
        print("aaaaa malandro se é bom em")
        acertou = True
        break

    elif tentativa < numero_secreto:
        print("o numero era maior doido")
        
    else:
        print("o numero era menor doido") # Corrigido o "erro" genérico para dar dica certa

if not acertou:
    print("o numero era", numero_secreto, "imbecil kkkkkkkk")