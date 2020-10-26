print("")
print("")

#####################################   ELECCIÓN DEL Nº AL AZAR    ################################
print("*Vamos a jugar a adivinar un número")

print("*Instrucciones: El ordenador va a elegir un número al azar entre 0 y 20. Tu deberás adivinar el número que ha elegido el ordenador")

# El ordenador elige un número

from random import randint

numero_ordenador = randint(0,20)

print("")
print("")

#########################################    Ocultar   ############################################



####################################    TURNO JUGADOR   ##############################################

# Lista de número elegidos

def juego():
    contador = 0
    lsta_numero_elegidos = []



    while contador < 5:

        contador += 1


        numero_jugador = int(input("Elige un número entero del 1 al 20: "))

        lsta_numero_elegidos.append(numero_jugador)

        orden = sorted(lsta_numero_elegidos)

        print("Has elegido :", numero_jugador)
        
        
        print("Has utilizado los siguientes números: ", orden)

        print("")
        print("")

        if numero_jugador > numero_ordenador:
            print("INCORRECTO, elige un número más pequeño")
        
        if numero_jugador < numero_ordenador:
            print("INCORRECTO, elige un número más grande")
    
        if numero_jugador == numero_ordenador:
                print("¡¡HAS ACERTADO!!, el número a adivinar era el", numero_jugador)

                break
        
        if contador == 5:
            print("¡Has perdido!. Te has pasado del número de intentos. El número era el:", numero_ordenador)

juego()


###############################      TURNO DE LA MÁQUINA       #######################################

print("")
print("")
print("")

print("Ahora a ver si el ordenador tarda menos que tú")

print("")

def maquina():

    print("Se ha elegido por azar el:", numero_ordenador)


    contador_ordenador = 0
    lsta_numero_elegidos_ordenador = []

    while contador_ordenador < 5:

        contador_ordenador += 1

        numero_ordenador2 = randint(0,20)

            

        lsta_numero_elegidos_ordenador.append(numero_ordenador2)

        orden_ordenador = sorted(lsta_numero_elegidos_ordenador)

        print("El ordenador ha elegido :", numero_ordenador2)
        
        
        print("El ordenador ha elegido los siguientes números: ", orden_ordenador)

        print("")

        if numero_ordenador2 > numero_ordenador:
            print("INCORRECTO, elige un número más pequeño")
        
        if numero_ordenador2 < numero_ordenador:
            print("INCORRECTO, elige un número más grande")
    
        if numero_ordenador2 == numero_ordenador:
                print("¡¡El ordenador ha acertado!!, el número a adivinar era el", numero_jugador)

                break
        
        if contador_ordenador == 5:
            print("¡El ordenador ha perdido!. Se ha pasado del número de intentos. El número era el:", numero_ordenador)


    print("")
    print("")
    print("")

maquina()


##############     marcar contadoresss     #########################################################

if contador > contador_ordenador:
    print("Eres más listo que el ordenador")

elif contador < contador_ordenador:
    print("Lo siento pringao, no eres más listo que un ordenador")

elif contador == contador_ordenador:
    print("La máquina no ha podido contigo, soys igual de listos")

