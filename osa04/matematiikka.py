from math import floor


def pyorista(luku: float) -> int:
    """
    Pyöristää annetun luvun "normaalien" pyöristyssääntöjen mukaan,
    eli aina puolikkaasta ylöspäin ja poispäin nollasta.

    >>> pyorista(0)
    0

    >>> pyorista(2.5)
    3

    >>> pyorista(3.5)
    4

    >>> pyorista(9.9)
    10

    >>> pyorista(-2.5) # rounds "away from zero"
    -3

    >>> pyorista(-9.9)
    -10
    """
    pyoristetty = int(floor(abs(luku) + 0.5))
    if luku >= 0:
        return pyoristetty
    else:
        return -1 * pyoristetty
