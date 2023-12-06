import numpy as np
import matplotlib.pyplot as plt
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C

# Criar dados de treinamento
rng = np.random.default_rng(seed=42)
X = rng.uniform(0, 5, 20)[:, np.newaxis]
y = np.sin(X).ravel() + rng.normal(0, 0.1, X.shape[0])

# Definir o kernel (usando kernel RBF)
kernel = C(1.0, (1e-3, 1e3)) * RBF(1.0, (1e-2, 1e2))
gp = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=10)

# Treinar o modelo
gp.fit(X, y)

# Criar dados de teste
X_test = np.linspace(0, 5, 1000)[:, np.newaxis]

# Fazer previsões
y_pred, sigma = gp.predict(X_test, return_std=True)

# Plotar resultados
plt.figure(figsize=(8, 4))
plt.scatter(X, y, c='r', s=50, zorder=10, edgecolors=(0, 0, 0))
plt.plot(X_test, y_pred, 'k', label='Previsão')
plt.fill_between(X_test[:, 0], y_pred - 1.96 * sigma, y_pred + 1.96 * sigma, alpha=0.2, color='k')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Processo Gaussiano')
plt.legend()
plt.show()
