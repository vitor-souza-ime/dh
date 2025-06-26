import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Função para converter graus para radianos
def deg_to_rad(degrees):
    return np.radians(degrees)

# Solicita os parâmetros ao usuário
a1 = float(input("Comprimento do primeiro elo (a1): "))
a2 = float(input("Comprimento do segundo elo (a2): "))
theta1_deg = float(input("Ângulo da junta 1 (θ1, base rotacional) em graus: "))
theta2_deg = float(input("Ângulo da junta 2 (θ2, cotovelo) em graus: "))

# Converte para radianos
theta1 = deg_to_rad(theta1_deg)
theta2 = deg_to_rad(theta2_deg)

# Junta 1 (base)
x0, y0, z0 = 0, 0, 0

# Ponto após primeiro elo
x1 = a1 * np.cos(theta1)
y1 = a1 * np.sin(theta1)
z1 = 0

# Ponto após segundo elo
x2 = x1 + a2 * np.cos(theta1) * np.cos(theta2)
y2 = y1 + a2 * np.sin(theta1) * np.cos(theta2)
z2 =       a2 * np.sin(theta2)

# Exibe posição do ponto final
print(f"Posição final da extremidade (xP, yP, zP): ({x2:.2f}, {y2:.2f}, {z2:.2f})")

# Plot 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot([x0, x1, x2], [y0, y1, y2], [z0, z1, z2], 'bo-', linewidth=4)
ax.scatter(x2, y2, z2, c='r', s=100, label='Ponta do braço')

# Eixos e título
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Braço Robótico em 3D (2DOF)')
ax.legend()
ax.grid(True)
ax.set_box_aspect([1,1,1])  # Deixa proporções iguais

# Define os limites do gráfico
lim = a1 + a2 + 1
ax.set_xlim([-lim, lim])
ax.set_ylim([-lim, lim])
ax.set_zlim([-lim, lim])

plt.show()
