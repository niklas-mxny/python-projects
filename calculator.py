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

for i in range (10):
    nummer1 = float(input("Gib die 1. Nummer ein: "))
    nummer2 = float(input("Gib die 2. Nummer ein: "))
    operation = input("Gib die Operation ein (+, -, *, /): ")

    ergebnis = rechnen(nummer1, nummer2, operation)
    print(f"Ergebnis: {ergebnis}")

rechnen()
