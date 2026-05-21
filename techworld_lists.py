produkte = ["Gaming-Laptop", "Wireless-Maus", "Mechanische Tastatur", "4K-Monitor", "Webcam"]

print("████████████████████████████████████████████")
print("███           T E C H W O R L D          ███")
print("████████████████████████████████████████████")
print()

for nummer, artikel in enumerate(produkte, start=1):
    print(f"{nummer}. {artikel}")

print("----")
print(f"Anzahl Produkte: ",len(produkte))
print()

preise = [1299.00, 49.90, 129.00, 399.00, 89.90]
gesamtpreis = sum(preise)
durschnittspreis = sum(preise) / len(preise)
min = min(preise)
max = max(preise)

print("███████████████████████████████████████")
print("███           P R E I S E           ███")
print("███████████████████████████████████████")
print()

for nummer, preis in enumerate(preise, start=1):
    print(f"{nummer}. {preis:.2f}€")

print("----")
print(f"Gesamtpreis: {gesamtpreis:.2f}€")
print(f"Durchschnittspreis: {durschnittspreis:.2f}€")
print(f"Geringster Preis: {min:.2f}€")
print(f"Höchster Preis: {max:.2f}€")
