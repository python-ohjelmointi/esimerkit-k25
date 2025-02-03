vuosi = 2026

print("<label>Vuosi: </label><select>")
while vuosi >= 1900:
    print(f"<option>{vuosi}</option>")

    if vuosi <= 1980:
        vuosi -= 10
    else:
        vuosi -= 1
print("</select>")

hinta = 100

print("<label>Hinta: </label><select>")
while hinta <= 1_000_000:
    hinta_str = f"{hinta:_}".replace("_", " ")
    print(f"<option value='{hinta}'>{hinta_str}</option>".replace("_", " "))

    if hinta < 1_000:
        hinta += 100
    elif hinta < 10_000:
        hinta += 1_000
    elif hinta < 100_000:
        hinta += 5_000
    elif hinta < 200_000:
        hinta += 50_000
    else:
        hinta += 100_000
print("</select>")
