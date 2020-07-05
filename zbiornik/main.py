import datetime as dt
import matplotlib.pyplot as plt

timestamp = dt.date(2014, 5, 1)

volume = 2_500_000

water_spending = 500 * 100 * 2

with open('deszcz.txt') as file:
    rain_data = []
    _ = file.readline()
    for line in file:
        data = line.split()
        rain_data.append((dt.date.fromisoformat(data[0]), data[1] == "1"))
    
zad_1_counter = 0
zad_2 = 0
min_vol = float('inf')
min_day = None

zestawienie = open('zestawienie.txt', 'w')
zestawienie.write("data\todprowadzono\tdolano\n")
labels = []
values = []

for day, is_raining in rain_data:

    if volume < min_vol:
        min_vol = volume
        min_day = day
    # print(volume)
    if day == dt.date(2014, 6, 1):
        print(volume)

    if not is_raining:
        volume -= water_spending

    if is_raining:
        volume *= 1.03
    else:
        volume *= 0.99

    drained = 0
    if volume > 2_500_000:
        drained = volume - 2_500_000
        volume = 2_500_000

        zad_1_counter += 1

    if day.weekday() == 5:  # sobota
        new_volume = min((volume + 500_000, 2_500_000))
        zad_2 += new_volume - volume

        if day.month == 5:
            zestawienie.write("{}\t{}\t{}\n".format(
                day.isoformat(), round(drained), round(new_volume - volume) 
            ))
            labels.append(day.isoformat())
            values.append(new_volume - volume)
        volume = new_volume


print("ZADANIE 1", zad_1_counter)
print("ZADANIE 2", round(zad_2))
print("ZADANIE 3", min_day.isoformat(), round(min_vol))
print("WYKRES")
plt.bar(labels, values)
plt.title("Woda dolewana w soboty")
plt.ylabel("litry wody")
plt.show()


