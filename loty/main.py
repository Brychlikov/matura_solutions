import pandas as pd

loty = pd.read_csv('loty.txt', sep='\t').set_index('id_lotu')
loty['data'] = pd.to_datetime(loty['data'])
pasazerowie = pd.read_csv('pasazerowie.txt', sep='\t').set_index('id_pasazera')

bilety = pd.read_csv('bilety.txt', sep='\t')

print(loty.groupby(('miejsce_docelowe', 'data')).count().groupby('miejsce_docelowe').count()[:3])


print('===============')

bil_pas = bilety.join(pasazerowie)
flight_counts = bil_pas.groupby('id_pasazera').count()["id_lotu"]
pasazerowie['liczba_lotow'] = flight_counts
# print(flight_counts[flight_counts > 15].sort_values(ascending=False))
print(pasazerowie[pasazerowie['liczba_lotow'] > 15])

print('=================')

bil_pas = bilety.join(pasazerowie)
print(bil_pas)
bil_pas['miesiac'] = bil_pas.apply(lambda d: d.month)

print(
    bil_pas
)

