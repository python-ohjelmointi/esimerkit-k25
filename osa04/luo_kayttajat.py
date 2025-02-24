from salasana import arvo_salasana


salasanan_pituus = 32

print("# luo_kayttajat.py")
print(
    f"INSERT INTO user (username, pwd) VALUES ('jenni', '{arvo_salasana(salasanan_pituus)}')")
print(
    f"INSERT INTO user (username, pwd) VALUES ('ushma', '{arvo_salasana(salasanan_pituus)}')")
print(
    f"INSERT INTO user (username, pwd) VALUES ('susanna', '{arvo_salasana(salasanan_pituus)}')")
