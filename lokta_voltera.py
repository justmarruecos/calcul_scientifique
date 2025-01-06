import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from itertools import product

#Chargement des données réelles
def load_real_data(file_path):
    " charge données , chemin vers , return les valeur"
    data = pd.read_csv(file_path)
    real_time = range(len(data))
    real_lapins = data['lapin'].values
    real_renards = data['renard'].values
    
    return real_time, real_lapins, real_renards


#Simulation de Lotka-Volterra
def simulate_lotka_volterra(alpha, beta, gamma, delta, step=0.001, number_iterations=100_000):
    time = [0]
    lapin = [1]
    renard = [2]

    for _ in range(number_iterations):
        new_time = time[-1] + step
        new_lapin = (lapin[-1] * (alpha - beta * renard[-1])) * step + lapin[-1]
        new_renard = (renard[-1] * (delta * lapin[-1] - gamma)) * step + renard[-1]

        time.append(new_time)
        lapin.append(new_lapin)
        renard.append(new_renard)

    return np.array(time), np.array(lapin) * 1000, np.array(renard) * 1000


#Calcul de l'erreur (MSE)
def calculate_mse(simulated_lapins, simulated_renards, real_lapins, real_renards):
    "mean calcul la moyenne arithmétique"
    lapins_error = ((simulated_lapins - real_lapins) ** 2).mean()
    renards_error = ((simulated_renards - real_renards) ** 2).mean()
    return lapins_error + renards_error


#Optimisation des paramètres
def optimize_parameters(real_time, real_lapins, real_renards, param_grid, step=0.001, number_iterations=100_000):
    best_params = None
    lowest_error = float('inf')

    for alpha, beta, gamma, delta in product(param_grid['alpha'], param_grid['beta'], param_grid['gamma'], param_grid['delta']):
        _, simulated_lapins, simulated_renards = simulate_lotka_volterra(alpha, beta, gamma, delta, step, number_iterations)
        mse = calculate_mse(simulated_lapins[:len(real_time)], simulated_renards[:len(real_time)], real_lapins, real_renards)

        if mse < lowest_error:
            lowest_error = mse
            best_params = (alpha, beta, gamma, delta)

    return best_params, lowest_error


#Visualisation
def plot_results(real_time, real_lapins, real_renards, simulated_time, simulated_lapins, simulated_renards):
    plt.figure(figsize=(15, 6))
    plt.plot(simulated_time, simulated_lapins, "b-", label="Lapins simulés")
    plt.plot(simulated_time, simulated_renards, "r-", label="Renards simulés")
    plt.scatter(real_time, real_lapins, c="blue", label="Lapins réels", marker="o")
    plt.scatter(real_time, real_renards, c="red", label="Renards réels", marker="x")
    plt.xlabel("Temps (Mois)")
    plt.ylabel("Population")
    plt.title("Comparaison des populations simulées et réelles")
    plt.legend()
    plt.grid()
    plt.show()


#Main
if __name__ == "__main__":
    #données réelles
    real_time, real_lapins, real_renards = load_real_data("populations_lapins_renards.csv")
    #grille de paramètres
    param_grid = {
        'alpha': [1/3, 2/3, 1, 4/3],
        'beta': [1/3, 2/3, 1, 4/3],
        'gamma': [1/3, 2/3, 1, 4/3],
        'delta': [1/3, 2/3, 1, 4/3]
    }
    # Optimiser les paramètres
    best_params, lowest_error = optimize_parameters(real_time, real_lapins, real_renards, param_grid)

    print(f"Meilleurs paramètres : alpha={best_params[0]}, beta={best_params[1]}, gamma={best_params[2]}, delta={best_params[3]}")
    print(f"Erreur minimale : {lowest_error}")

    # Simuler avec les meilleurs paramètres
    simulated_time, simulated_lapins, simulated_renards = simulate_lotka_volterra(*best_params) # * décompose le tuple best_params = (alpha, beta, gamma, delta)

    # Visualiser les résultats
    plot_results(real_time, real_lapins, real_renards, simulated_time, simulated_lapins, simulated_renards)
