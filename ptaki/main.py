import pandas as pd

gatunki = pd.read_csv('gatunki.txt', sep='\t').set_index('ID_gatunku')
lokalizacje = pd.read_csv('lokalizacje.txt', sep='\t').set_index('ID_lokalizacji')

obserwacje = pd.read_csv('obserwacje.txt', sep='\t')
obserwacje['poczatek'] = pd.to_datetime(obserwacje['poczatek'])
obserwacje['koniec'] = pd.to_datetime(obserwacje['koniec'])

print(
        obserwacje.join(gatunki, on='ID_gatunku').groupby('nazwa_zwyczajowa').count().sort_values('ID_lokalizacji', ascending=False)[:3]
)

print('=========================')

obserwacje['miesiac'] = obserwacje['poczatek'].apply(lambda d: d.month)
# obserwacje = obserwacje.assign(miesiac=obserwacje['miesiac'].apply(lambda d: d.month))

ob_gatunki = obserwacje.join(gatunki, on="ID_gatunku")
print(ob_gatunki[ob_gatunki['nazwa_zwyczajowa'] == 'remiz'].groupby('miesiac').count())


print('=========================')

all_things = ob_gatunki.join(lokalizacje, on="ID_lokalizacji")

is_miasto = lambda s: "miasto" in s['opis']
print(all_things[all_things.mask(is_miasto)])

