import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt

tree = 1
burning = 2
empty = 0
dim = (100, 100)
treeprob = 0.50
fireprob = 0.01
immune = 0.2

def initialize_forest(dim, treeprob, fireprob, immune):
    forest = np.zeros(shape=dim)

    for i in range(dim[0]):
        for j in range(dim[1]):
            if np.random.rand() < treeprob:
                if np.random.rand() < fireprob and np.random.rand() < (1 - immune):
                    forest[i, j] = burning
                else:
                    forest[i, j] = tree
    return forest

def plot_forest(forest):
    sn.heatmap(forest, cmap='Greens', xticklabels=False, yticklabels=False, annot=False)
    plt.show()

def simulate_fire_spread(forest, immune, num_steps=15):
    for t in range(num_steps):
        new_forest = np.copy(forest)
        for i in range(dim[0]):
            for j in range(dim[1]):
                if (
                    forest[i, j] == tree and (
                        any(forest[x, y] == burning for x, y in [
                            (i - 1, j - 1), (i - 1, j), (i - 1, (j + 1) % dim[1]),
                            (i, j - 1), (i, (j + 1) % dim[1]),
                            ((i + 1) % dim[0], j - 1), ((i + 1) % dim[0], j),
                            ((i + 1) % dim[0], (j + 1) % dim[1])]
                        )
                    )
                ):
                    if np.random.rand() < (1 - immune):
                        new_forest[i, j] = burning
                elif forest[i, j] == burning:
                    new_forest[i, j] = empty

        forest = np.copy(new_forest)
        plot_forest(forest)
        print(f"Step {t+1}")
        print(f"{tree=},{burning=},{empty=} ")
        # Uncomment the line below if you want to pause and observe each step
        # input()

# Initialize the forest
forest = initialize_forest(dim, treeprob, fireprob, immune)

# Plot the initial state
plot_forest(forest)

# Simulate fire spread
simulate_fire_spread(forest, immune, num_steps=15)
