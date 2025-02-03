from random import choice
from string import ascii_letters, digits

merkit = ascii_letters + digits

salasana = ""
pituus = 64

while len(salasana) < pituus:
    salasana += choice(merkit)

print(salasana)
