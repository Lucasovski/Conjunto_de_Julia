import numpy as np
import matplotlib.pyplot as plt

def orbit_behavior(c, max_iter=1000):
    z = 0
    for i in range(max_iter):
        z = z*z + c
        if abs(z) > 2:
            return i
    return -1

def julia_set(c, width=800, height=800, max_iter=1000):
    x = np.linspace(-2, 2, width)
    y = np.linspace(-2, 2, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j*Y
    image = np.zeros(Z.shape, dtype=int)
    mask = np.ones(Z.shape, dtype=bool)
    
    for i in range(max_iter):
        Z[mask] = Z[mask]**2 + c
        diverged = (abs(Z) > 2) & mask
        image[diverged] = i
        mask[diverged] = False
    
    image[mask] = max_iter
    return image

def main():
    c_input = input("Digite o número complexo c (ex: 0.3+0.5j): ")
    try:
        c = complex(c_input)
    except ValueError:
        print("Formato de número complexo inválido. Saindo.")
        return
    
    orbit_result = orbit_behavior(c)
    
    if orbit_result == -1:
        print(f"A órbita de 0 não escapa. O conjunto de Julia preenchido está conectado.")
    else:
        print(f"A órbita de 0 escapa após {orbit_result} iterações. O conjunto de Julia preenchido está desconectado.")
    
    plt.figure(figsize=(8, 8))
    plt.imshow(julia_set(c), cmap='hot', extent=(-2, 2, -2, 2))
    plt.colorbar(label='Iterações para divergir')
    plt.title(f"Conjunto de Julia Preenchido para c = {c}")
    plt.xlabel('Real')
    plt.ylabel('Imaginário')
    plt.show()

if __name__ == "__main__":
    main()
