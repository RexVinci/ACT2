try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None
    print("matplotlib is not installed. Install it with 'pip install matplotlib' to see the plot.")

# Definir vector de tiempo (de -5 a 5 segundos)
t = [-5 + i * (10 / 999) for i in range(1000)]

# Crear la función escalón unitario
escalon = [1.0 if x >= 0 else 0.0 for x in t]

# Graficar
if plt is not None:
    plt.figure(figsize=(8, 3))
    plt.plot(t, escalon, label='$u(t)$', color='blue', linewidth=2)
    plt.title('Función Escalón Unitario')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.ylim(-0.2, 1.2)
    plt.legend()
    plt.show()
else:
    print("No se puede graficar porque matplotlib no está disponible.")