import matplotlib.pyplot as plt
import numpy

time = [0]
lapin = [1]
renard = [2]

alpha = 2/3
beta = 4/3
delta = 1
gamma = 1

step = 0.001

for _ in range(0, 100_000):
    new_value_time = time[-1] + step
    new_value_lapin = (lapin[-1] * (alpha - beta * renard[-1])) * step + lapin[-1]
    new_value_renard = (renard[-1] * (delta * lapin[-1] - gamma)) * step + renard[-1]

    time.append(new_value_time)
    lapin.append(new_value_lapin)
    renard.append(new_value_renard)

lapin = numpy.array(lapin)
lapin *= 1000
renard = numpy.array(renard)
renard *= 1000

plt.figure(figsize=(15, 6))
plt.plot(time, lapin, "b-", label='Lapins')
plt.plot(time, renard, "b-", label='Renards')
plt.xlabel('Temps (Mois)')
plt.ylabel('Population')
plt.title('Dynamique des populations Proie-Prédateur')
plt.legend()
plt.show()