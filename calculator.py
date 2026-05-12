nummer1 = float(input("Gib die 1. Nummer ein: "))
nummer2 = float(input("Gib die 2. Nummer ein: "))
operation = input("Gib die Operation ein (+, -, *, /): ")

if operation == "+":
    ergebnis = nummer1 + nummer2
elif operation == "-":
    ergebnis = nummer1 - nummer2
elif operation == "*":
    ergebnis = nummer1 * nummer2
elif operation == "/":
    ergebnis = nummer1 / nummer2
else:    ergebnis = "Falscher Operator"

print(f"Ergebnis: {ergebnis}")