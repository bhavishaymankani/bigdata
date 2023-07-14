from numpy import where
from numpy import unique
from sklearn.datasets import make_classification
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

X, y = make_classification(n_samples=1000, n_features=2, n_informative=2, 
n_redundant=0, n_clusters_per_class=1, random_state=4)

for class_value in range(2):
    row_ix = where(y == class_value)
    plt.scatter(X[row_ix, 0], X[row_ix, 1])

plt.show()

