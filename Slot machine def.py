#Slot Machine Project
#importo la libreria random para elegir valores al azar

import random

#defino las constantes
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

#creamos un diccionario para almacenar los simbolos q apareceran en el slot
symbol_count = {
    "A": 2,
    "K": 3,
    "Q": 3,
    "J": 4
}

#creamos un diccionario para almacenar los valores de los simbolos
symbol_value = {
    "A": 5,
    "K": 3,
    "Q": 2,
    "J": 1
}

#creamos la funcion que realiza el check de las ganacias
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    #creo un bucle que analiza linea por linea los simbolos q contiene
    for line in range(lines):
        symbol = columns[0][line]
        #otro bucle que se encarga de revisar si los valores se repiten en las columnas
        for column in columns:
            symbol_to_check = column[line]
            #un if para q verifica si en la linea no se repiten simbolos
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

#funcion para obtener el giro de la maquina
def get_slot_machine_spin(rows, cols, symbols):
    #lista donde se almacenan los simbolos
    all_symbols = []
    #bucle para recorrer y almacenar los simbolos y la cantidad de veces q aparecen
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
#creamos una lista anidada para poner los simbolos por columna
    columns = []
    #creamos un bucle para agregar valores a nuestra lista anidada
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        #se crea otro bucle para recorrer y eliminar el simbolo elegido y q no vuelva a aparecer en la columna
        for _ in range(rows):
            value = random.choice(current_symbols) #elige un valor al azar de nuestros simbolos
            current_symbols.remove(value) #remueve el valor de la lista
            column.append(value) #agrega el valor a la lista

        columns.append(column)

    return columns

#creamos la funcion para mostrar en pantalla nuestro slot
def print_slot_machine(columns):
    #creamos un bucle para q nuestra lista columna se muestre como columna y no como fila como es normal en una lista
    for row in range(len(columns[0])):
        #el bucle hace q para cada una de nuestras lineas se almacene en columna y se muestre de manera vertical
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()

#Funcion que toma el deposito del usuario
def deposit():
    #while para preguntar continuamente al usuario la cantidad a ingresar hasta ingresar una cantidad valida
    while True:
        amount = input("Indique la cantidad a depositar: \n$")
        #un if para verificar q el valor ingresado sea un numero.
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("La cantidad debe ser mayor a 0.")
        else:
            print("Por favor ingrese un numero.")

    return amount

#defino la funcion q va a solicitar el numero de lineas a jugar por el usuario
def get_number_of_lines():
    #while para preguntar constantemente el valor de lineas a jugar hasta ingresar un valor valido
    while True:
        lines = input(
            "Ingrese la cantidad de lineas a apostar.\n(1-" + str(MAX_LINES) + ")?\n ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Ingrese un numero valido de lineas.")
        else:
            print("Por favor ingrese un numero.")

    return lines

#defino la funcion que obtiene la apuesta del usuario.
def get_bet():
    while True:
        amount = input("Cuanto desea apostar en cada linea? \n$")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"La cantidad debe estar comprendida entre:\n ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Por favor ingrese un numero.")

    return amount

#defino una funcion para devolver los balances del juego actualizados
def spin(balance):
    lines = get_number_of_lines() #obtiene las lineas a jugar
    while True:
        bet = get_bet() #obtiene el valor a apostar
        total_bet = bet * lines #obtiene el valor total a apostar

        if total_bet > balance:
            print(
                f"No dispones de suficiente balance, tu balance es de: ${balance}")
        else:
            break

    print(
        f"Estas jugando ${bet} en {lines} lineas. Tu apuesta total es de: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"Ganaste ${winnings}.")
    print("Ganaste en las lineas:", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Balance Actual: ${balance}")
        answer = input("Presione ENTER para jugar (q para salir).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"Abandonas el juego con ${balance}")


main()