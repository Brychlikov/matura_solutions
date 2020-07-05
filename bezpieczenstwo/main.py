import pandas as pd

szkoly = pd.read_csv('szkoly.txt', sep="\t").set_index('Id_szkoly')
ankiety = pd.read_csv('ankiety.txt', sep="\t")
gminy = pd.read_csv('gminy.txt', sep="\t").set_index('Kod_gminy')

print(szkoly.describe())
print(ankiety.describe())
print(gminy.describe())

print('=====================')

# print(len(ankiety[ankiety['Plec'] == 'k']))
# print(len(ankiety[ankiety['Plec'] == 'm']))

print(ankiety.groupby('Plec').count())

print("\n===================\n")

print(ankiety.join(szkoly, on="Id_szkoly").groupby('Rodzaj_szkoly').mean())

print("\n===================\n")
print(
        ankiety.join(szkoly, on="Id_szkoly").join(gminy, on="Kod_gminy").groupby('Kod_gminy').mean()['pyt6'].sort_values(ascending=False)
)

an_szkol = ankiety.join(szkoly, on="Id_szkoly")
print("\n===================\n")
print(
        an_szkol[an_szkol['pyt3']  == 5][['Rodzaj_szkoly', 'pyt3']].groupby('Rodzaj_szkoly').count()
)

print("\n===================\n")

full = ankiety.join(szkoly, on="Id_szkoly").join(gminy, on="Kod_gminy")
print(
    full.groupby('Kod_gminy').count()['Nr_ankiety'].sort_values(ascending=False).head(1)
)

print(
        an_szkol[an_szkol['pyt1']  == 5][['Rodzaj_szkoly', 'Plec', 'pyt1']].groupby(('Rodzaj_szkoly', 'Plec')).count()
)

print(
        an_szkol[an_szkol['pyt1']  == 5][['Rodzaj_szkoly', 'Plec', 'pyt1']].groupby(('Rodzaj_szkoly', 'Plec')).count()
)
