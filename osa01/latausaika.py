# 27,3 MB (28 688 288 bytes)        tavut (8 bittiä)
# 21 Mbps                           bitit

# Esimerkki 1: "levytila"
tavut = 28_688_288
kilot = tavut / 1024
megat = kilot / 1024
print(f"{tavut=} {megat=} {kilot=}")

# Esimerkki 2: "nettiyhteys"
tavut = 399 * 1024**3
bitit = tavut * 8
nopeus = 21 * 1000 * 1000

print(f"Bittejä siirretään {bitit}")

sekunnit = bitit / nopeus

tunnit = (sekunnit // 60) // 60
minuutit = (sekunnit // 60) % 60

print(f"{tunnit:.0f} tuntia ja {minuutit:.0f} minuuttia")
