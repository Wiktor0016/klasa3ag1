#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  baza.py
import csv


def czytaj_dane(plik, separator=","):
    with open(plik, newline='', encoding='utf-8') as plikcsv:
        tresc = csv.reader(plikcsv, delimiter=separator)
    print(tresc)


def main(args):
    czytaj_dane('nazwiska.txt', ' ')
    # dokończyć konwersję pliku nazwiska.txt!!! i dopiero testować
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
