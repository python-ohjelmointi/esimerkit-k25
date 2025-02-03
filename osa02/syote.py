summa = 0

while True:
    syote = input("syötä seuraava luku (tyhjä lopettaa): ")

    if syote == "":  # "guard clause"
        break

    luku = int(syote)
    summa += luku

print(f"Summa on {summa}")
