#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwerendy.py
import sqlite3

def kwerenda1(cur):
    cur.execute("""
        SELECT nazwisko, imie1, dzien, miesiac, rok
        FROM nazwiska
        INNER JOIN dane_osobowe
        ON nazwiska.nr_ucznia=dane_osobowe.nr_ucznia
        WHERE nazwiska.nr_ucznia=9201
    """)
    # SELECT * FROM nazwiska WHERE nazwisko LIKE 'G%'
    wyniki = cur.fetchall()  # pobranie wszystkich rekordów na raz
    for row in wyniki:
        print(tuple(row))


def main(args):
    ### KONFIGURACJA ###
    baza_nazwa = 'szkola'
    tabele = ['nazwiska', 'dane_osobowe', 'oceny']
    ####################
    
    con = sqlite3.connect(baza_nazwa + '.db')
    cur = con.cursor()  # obiekt tzw. kursora

    kwerenda1(cur)

    con.commit()
    con.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
