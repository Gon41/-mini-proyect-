
contador = 0
lsta_numero_elegidos = []
numero_ordenador = 15

import random

while contador < 5:

    contador += 1

    numero_maquina = random.randit(0,21)

    if numero_maquina > numero_ordenador:

        numero_maquina2 = random.randit(numero_maquina,21)
        print(numero_maquina2)
    
    