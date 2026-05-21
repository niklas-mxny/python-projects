produkte = ["Gaming-Laptop", "Wireless-Maus", "Mechanische Tastatur", "4K-Monitor", "Webcam"]
print("████████████████████████████████████████████")
print("███           T E C H W O R L D          ███")
print("████████████████████████████████████████████")
print()
for nummer, artikel in enumerate(produkte, start=1):
    print(f"{nummer}. {artikel}")
print("----")
print(f"Anzahl Produkte: ",len(produkte))