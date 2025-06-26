import numpy as np
import matplotlib.pyplot as plt

# Função para criar a matriz de transformação DH clássica
def dh_classico(theta, d, a, alpha):
    ct = np.cos(theta)
    st = np.sin(theta)
    ca = np.cos(alpha)
    sa = np.sin(alpha)
    return np.array([
        [ct, -st * ca,  st * sa, a * ct],
        [st,  ct * ca, -ct * sa, a * st],
        [0,       sa,      ca,      d],
        [0,        0,       0,      1]
    ])

# Entrada do usuário
a1 = float(input("Comprimento do primeiro elo (a1): "))
a2 = float(input("Comprimento do segundo elo (a2): "))
theta1_deg = float(input("Ângulo da junta 1 (θ1) em graus: "))
theta2_deg = float(input("Ângulo da junta 2 (θ2) em graus: "))

# Conversão para radianos
theta1 = np.radians(theta1_deg)
theta2 = np.radians(theta2_deg)

# Parâmetros DH clássicos (α = 0, d = 0)
T1 = dh_classico(theta1, 0, a1, 0)
T2 = dh_classico(theta2, 0, a2, 0)

# Transformação total: base → junta 2 → ponta
T_final = T1 @ T2

# Extrai as posições
x0, y0 = 0, 0
x1, y1 = T1[0, 3], T1[1, 3]
x2, y2 = T_final[0, 3], T_final[1, 3]

# Exibe resultado
print(f"Posição final da extremidade (xP, yP): ({x2:.2f}, {y2:.2f})")

# Gráfico
plt.figure(figsize=(8, 6))
plt.plot([x0, x1, x2], [y0, y1, y2], 'bo-', linewidth=4)
plt.scatter(x2, y2, c='r', s=100, label='Ponta do braço')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Braço Robótico com DH Clássico (2 DOF)')
plt.legend()
plt.grid(True)
plt.axis('equal')
lim = a1 + a2 + 1
plt.xlim([-lim, lim])
plt.ylim([-lim, lim])
plt.show()
