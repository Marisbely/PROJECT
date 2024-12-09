from scipy.optimize import linprog
def main():
    print("=== Resolutor de Programación Lineal ===")
    # Ingresar la función objetivo
    print("\n1. Ingresar la función objetivo:")
    print("Ejemplo: Para maximizar z = 3x + 2y, ingresa los coeficientes separados por espacios: 3 2")
    c = list(map(float, input("Coeficientes de la función objetivo: ").split()))
    # Ingresar las restricciones
    print("\n2. Ingresar las restricciones:")
    print("Ejemplo: Para 2x + y <= 8 y x + 2y <= 6, ingresa los coeficientes en cada fila y luego el lado derecho.")
    num_restricciones = int(input("Número de restricciones: "))
    A = []  # Lista que contendrá los coeficientes de las restricciones.
    b = []  # Lista que contendrá los lados derechos de las restricciones.

    for i in range(num_restricciones):
        print(f"\nRestricción {i + 1}:")
        coeficientes = list(map(float, input("Coeficientes (ejemplo: 2 1): ").split()))
        A.append(coeficientes)
        lado_derecho = float(input("Lado derecho (ejemplo: 8): "))
        b.append(lado_derecho)
         # Ingresar límites de las variables
    print("\n3. Ingresar límites de las variables:")
    print("Ejemplo: Para x >= 0, y >= 0, los límites son (0, None) para cada variable.")
    limites = []  # Lista para almacenar los límites de las variables.
    
    for i in range(len(c)):  # Recorremos el número de variables (basado en el número de coeficientes de la función objetivo).
        print(f"Límites para la variable {i + 1} (en formato: inferior superior, ejemplo: 0 None):")
        limite = input("Límite: ").split()
        limites.append((float(limite[0]), None if limite[1] == "None" else float(limite[1])))
        # Resolver el problema de programación lineal
    print("\nResolviendo el problema...")
    resultado = linprog(c, A_ub=A, b_ub=b, bounds=limites, method='highs')

    if resultado.success:
        print("\nSolución encontrada:")
        print(f"Valor óptimo de la función objetivo: {-resultado.fun}")
        for i, var in enumerate(resultado.x):
            print(f"Valor de la variable {i + 1}: {var}")
    else:
        print("\nNo se pudo encontrar una solución.")
        if __name__ == "__main__":
    main()