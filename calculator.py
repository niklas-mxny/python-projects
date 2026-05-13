ergebnisse = []
def menu():
    print("🆃🅰🆂🅲🅷🅴🅽🆁🅴🅲🅷🅽🅴🆁")
    print()
    print("1. Rechnen")
    print("2. Ergebnisse anzeigen")
    print("3. Programm beenden")
    return int(input("Wähle eine Option: "))


def rechnen(nummer1, nummer2, operation):
    
    if operation == "+":
        return nummer1 + nummer2
    elif operation == "-":
        return nummer1 - nummer2
    elif operation == "*":
        return nummer1 * nummer2
    elif operation == "/":
        return nummer1 / nummer2
    else:
        return "Falscher Operator"

while True:
    auswahl = menu()
    if auswahl == 1:
        nummer1 = float(input("Gib die 1. Nummer ein: "))
        nummer2 = float(input("Gib die 2. Nummer ein: "))
        operation = input("Gib die Operation ein (+, -, *, /): ")

        ergebnis = rechnen(nummer1, nummer2, operation)
        ergebnisse.append(ergebnis)
        print(f"Ergebnis: {ergebnis}")
    elif auswahl == 2:
        print(f"Ergebnisse bisher: {ergebnisse}")
    elif auswahl == 3:
        print("Programm wird beendet.")
        exit()
    else:
        print("Ungültige Option. Bitte versuche es erneut.")


    else:
        print("Ungültige Option. Bitte versuche es erneut.")


