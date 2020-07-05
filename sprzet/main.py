import pandas as pd

sprzet = pd.read_csv('new_sprzet.txt', sep='\t').set_index("ID_sprzetu")
klienci = pd.read_csv('new_klienci.txt', sep='\t').set_index("Nr_dowodu_osoby")
wynajem = pd.read_csv('new_wynajem.txt', sep='\t')


print(wynajem.join(klienci))
