import numpy as np
import matplotlib.pyplot as plt
import torch

def minimisation(f,eta, x0, epsilon, max_iter, batch_size):
    # Algorithme de descente de gradient stochastique
    for i in range(max_iter):
        # Sélectionner un batch aléatoire de données
        x_batch = torch.tensor(np.random.uniform(low=-5, high=5, size=batch_size), requires_grad=False)
        y_batch = f(x_batch)

        # Calculer le gradient approximatif
        y_pred = f(x0)
        gradient = torch.autograd.grad(y_pred, x0, create_graph=True)[0]

        # Mettre à jour les poids
        x_new = x0 - eta * gradient

        # Vérifier la convergence
        if torch.norm(x_new - x0) < epsilon:
            break
        x0.data = x_new.data

    # Affichage des résultats
    x_min = x0.detach().numpy()[0]




#fonction de minimisation en utilisant une descente de gradient stochastique de la fonction f
def minimisation(f, x0, eta, epsilon, max_iter,batch_size):
   # Algorithme de descente de gradient stochastique
    x = x0
    iter = 0
    while iter < max_iter:
        # Sélectionner un batch aléatoire de données
        x_batch = np.random.uniform(low=-5, high=5, size=batch_size)
        y_batch = f(x_batch)

        # Calculer le gradient approximatif
        gradient = np.mean(2*x_batch + 2)

        # Mettre à jour les poids
        x_new = x - eta * gradient

        # Vérifier la convergence
        if abs(x_new - x) < epsilon:
            break
        x = x_new
        iter += 1

    # Affichage des résultats
    print(f"Minimum de la fonction atteint à x = {x}")
    print(f"Valeur minimale de la fonction = {f(x)}")

    # Tracer la fonction
    x_plot = np.linspace(-5, 3, 100)
    y_plot = f(x_plot)
    plt.plot(x_plot, y_plot)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Fonction à minimiser')
    plt.plot(x, f(x), 'ro')
    plt.show()

if __name__ == "__main__":

    # Fonction test à minimiser
    def test(x):
        return x**2
    # Paramètres de l'algorithme
    eta = 0.1    # Taux d'apprentissage
    epsilon = 1e-6  # Tolérance de convergence
    max_iter = 1000 # Nombre maximum d'itérations
    batch_size = 10  # Taille du batch
    x0 = torch.tensor([5], requires_grad=True)  # Point de départ

    x_min=minimisation(test, x0, eta, epsilon, max_iter,batch_size)

    print(f"Minimum de la fonction atteint à x = {x_min}")
    print(f"Valeur minimale de la fonction = {f(x_min)}")

    # Tracer la fonction
    x_range = np.linspace(-5, 5, 100)
    y_range = f(x_range)
    fig, ax = plt.subplots()
    ax.plot(x_range, y_range)
    ax.plot(x_min, f(x_min), 'ro')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Fonction à minimiser')
    plt.show()

