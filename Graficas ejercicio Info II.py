import numpy as np
import matplotlib.pyplot as plt


vec= np.random.rand(720)

mat= vec.reshape(120, 6)

mat_TF= np.transpose(mat.copy(order='F'))
mat_TC= np.transpose(mat.copy(order='C'))

fig= plt.figure(figsize=(12, 8))

ax1= plt.subplot2grid((3, 4), (0, 0), colspan=2)
ax2= plt.subplot2grid((3, 4), (0, 2), colspan=2)
ax3= plt.subplot2grid((3, 4), (1, 0), colspan=2)
ax4= plt.subplot2grid((3, 4), (1, 2), colspan=2)
ax5= plt.subplot2grid((3, 4), (2, 0), colspan=2)
ax6= plt.subplot2grid((3, 4), (2, 2), colspan=2)

fila= mat[0, :]

ax1.plot(fila, marker='o', label="Línea")
ax1.set_title("Gráfico de Línea")
ax1.legend()
ax1.grid(True)

ax2.scatter(range(len(fila)), fila, c='red', label="Scatter")
ax2.set_title("Diagrama de dispersión")
ax2.legend()
ax2.grid(True)

ax3.bar(range(len(fila)), fila, label="Barras")
ax3.set_title("Gráfico de Barras")
ax3.legend()
ax3.grid(True)

ax4.hist(mat.flatten(), bins=20, color="green", alpha=0.7, label="Histograma")
ax4.set_title("Histograma")
ax4.legend()
ax4.grid(True)

ax5.pie(fila / fila.sum(), labels=[f"Col {i}" for i in range(len(fila))], autopct='%1.1f%%')
ax5.set_title("Gráfico Circular")

ax6.fill_between(range(len(fila)), np.cumsum(fila), alpha=0.5, label="Área")
ax6.set_title("Área acumulada")
ax6.legend()
ax6.grid(True)

plt.tight_layout()

plt.show()
