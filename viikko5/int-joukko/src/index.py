import unittest
from int_joukko import IntJoukko


def main():
    joukko = IntJoukko()

    joukko.lisaa(10)
    joukko.lisaa(3)
    joukko.poista(3)
    print(joukko.kuuluu(3))
    print(joukko.mahtavuus(), 1)

    # joukko.lisaa(1)
    # joukko.lisaa(2)
    # joukko.lisaa(3)
    # joukko.lisaa(2)
    # joukko.poista(10)

    print(joukko)


if __name__ == "__main__":
    main()
