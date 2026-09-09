import random

numero_secreto = random.randint(1, 100)

print("print")
print("advinhe o numero de 1-100")

contador = 7
acertou = False


while contador > 0:
    print(f'voce ta tendo {contador} tentavias ainda')

    entrada = input("mete o loco e chuta o numero > ").strip()

    if not entrada.isdigit():
        print("o retardado é numero nao letra")
        continue

    tentativa = int(entrada)

    contador -= 1

    if tentativa == numero_secreto:
        tentativa_usada = 7 - contador
        print("aaaaa malandro se é bom em")
        print(f'acertou en {tentativa_usada}, vai tomano')
        acertou = True
        break

    elif tentativa < numero_secreto:
        print("o numero era maior doido")

    else:
        print("o numero era menor doido")

if not acertou:
    print("o numero era", numero_secreto, "imbecil kkkkkkkk")