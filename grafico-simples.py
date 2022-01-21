from matplotlib import pyplot as plt
import numpy as np


#Quantidades de vendas para o produto A
valores_produto_A = [6, 7, 8, 4, 4]

#Quantidades de vendas  para o produto B
valores_produto_B = [3, 12, 3, 4.1, 6]

#Criar eixo x para produto A e prduto B com uma separação de 0.25 entre as baras
x1 = np.arange(len(valores_produto_A))
x2 = [x + 0.25 for x in x1]

#PLota de barras
plt.bar(x1, valores_produto_A, width=0.25, label = 'Produto A', color = 'deepskyblue')
plt.bar(x2, valores_produto_B, width=0.25, label = 'Produto B', color = 'mediumseagreen')

#Colocar o nome dos meses como label do eixo x
meses = ['Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
plt.xticks([x + 0.25 for x in range(len(valores_produto_A))], meses)

plt.legend()

plt.title("Quantidade de Vendas")
plt.show
