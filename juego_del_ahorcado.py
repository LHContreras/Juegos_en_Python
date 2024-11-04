

import random


def obtener_palabra_secreta() -> str:
    palabras = ['python', 'javascript', 'java', 'anglar', 'django', 'tensorflow', 'react', 'typescript', 'git', 'flask',]
    return random.choice(palabras)

def mostrar_progreso(palabra_secreta, letras_adivinadas):
    adivinado = ''

    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            adivinado += letra
        else:
            adivinado += '_'
    return adivinado

def juego_ahorcado():
    palabra_secreta = obtener_palabra_secreta()
    letras_adivinadas = []
    intentos = 7
    juego_terminado = False

    print("¡Bienvenido aal juego del ahorcado!")
    print(f"Tenés {intentos} intentos para adivinar la palabra secreta")
    print(mostrar_progreso(palabra_secreta, letras_adivinadas), "la palabra tiene: ", len(palabra_secreta), "letras" )

    while not juego_terminado and intentos > 0:
        adivinanza = input("Introduce una letra: ").lower()

        if len(adivinanza) != 1 or not adivinanza.isalpha():
            print("Ingrese de a una sola letra a la ves")
        elif adivinanza in letras_adivinadas:
            print("Ya utilizaste esta letra, prueba con otra")
        else:
            letras_adivinadas.append(adivinanza)

            if adivinanza in palabra_secreta:
                print(f"¡Muy bien has acertado, la letra '{adivinanza}' está presente en la palabra")
            else:
                intentos -= 1
                print(f"Lo siento mucho la letra {adivinanza} no está presente en la palabra")
                print(f"Te quedan {intentos} intentos")
        progreso_actual = mostrar_progreso(palabra_secreta, letras_adivinadas)
        print(progreso_actual)

        if "_" not in progreso_actual:
            juego_terminado = True
            palabra_secreta = palabra_secreta.capitalize()
            print(f"¡Felicitaciones has ganado! La palabra es: '{palabra_secreta}'")
    if intentos == 0:
        palabra_secreta = palabra_secreta.capitalize()
        print(f"Lo sentimos mmucho se te han acabado los intentos, la palabra es '{palabra_secreta}'")
    

juego_ahorcado()