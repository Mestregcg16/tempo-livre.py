import matplotlib.pyplot as plt
import numpy as np

# Valores ou porcentagens do grafico
porcentagem = np.array([35, 25, 20, 15, 5])

# definir os itens do graficos
itens = ['Python', 'javaScript', 'php', 'java', 'ruby']

# Espaçamemto entre as linhas
espaco = [0.2, 0, 0, 0]

# Monstrar o grafico e depois mostrar
plt.pie(porcentagem, labels=itens, explode=espaco, shadow=True)
plt.show()