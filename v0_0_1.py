import random


def obtener_palabra_secreta() -> str:
    palabras = ['python', 'javascript', 'java', 'angular', 'django', 'tensorflow', 'react', 'typescript', 'git', 'flask']
    return random.choice(palabras)

def mostrar_progreso(palabra_secreta, letras_adivinadas):
    adivinado = ''

    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            adivinado += letra
        else:
            adivinado += "_"

    return adivinado


def juego_ahorcado():
    palabra_secreta = obtener_palabra_secreta()
    letras_adivinadas = []
    intentos = 7
    juego_terminado = False

    print("¡Bienvenido al juego del ahorcado!")
    print(f"Tienes {intentos} intentos para adivinar la palabra secreta.")
    print(f"{mostrar_progreso(palabra_secreta, letras_adivinadas)} (La palabra tiene {len(palabra_secreta)} letras)")

    while not juego_terminado and intentos > 0:
        adivinanza = input("Introduce una letra: ").lower()

        if len(adivinanza) != 1 or not adivinanza.isalpha():
            print("Por favor, introduce una letra válida (solo una letra).")
        elif adivinanza in letras_adivinadas:
            print("Ya has utilizado esa letra, prueba con otra.")
        else:
            letras_adivinadas.append(adivinanza)

            if adivinanza in palabra_secreta:
                print(f"¡Muy bien! Has acertado, la letra '{adivinanza}' está presente en la palabra.")
            else:
                intentos -= 1
                print(f"Lo siento, la letra '{adivinanza}' no está presente en la palabra secreta.")
                print(f"Te quedan {intentos} intentos.")

        progreso_actual = mostrar_progreso(palabra_secreta, letras_adivinadas)
        print(progreso_actual)

        if "_" not in progreso_actual:
            juego_terminado = True
            palabra_secreta = palabra_secreta.capitalize()
            print(f"¡Felicitaciones, has ganado! La palabra completa es: '{palabra_secreta}'.")

    if intentos == 0:
        palabra_secreta = palabra_secreta.capitalize()
        print(f"Lo sentimos, se te han acabado los intentos. La palabra secreta era '{palabra_secreta}'.")


juego_ahorcado()