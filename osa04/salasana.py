from random import choice
from string import ascii_letters, digits

merkit = ascii_letters + digits


def arvo_salasana(pituus):
    salasana = ""
    while len(salasana) < pituus:
        salasana += choice(merkit)

    return salasana


if __name__ == "__main__":
    # "pääohjelma":
    print("# salasana.py")
    salasanan_pituus = int(input("Anna salasanoille pituus: "))
    print(
        f"INSERT INTO user (username, pwd) VALUES ('matti', '{arvo_salasana(salasanan_pituus)}')")
    print(
        f"INSERT INTO user (username, pwd) VALUES ('teppo', '{arvo_salasana(salasanan_pituus)}')")
