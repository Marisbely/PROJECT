python
Copiar código
import numpy as npfrom scipy.optimize import linprog
class LinearProgrammingSolver:
    def __init__(self, objective_coeffs, lhs_ineq, rhs_ineq, lhs_eq=None, rhs_eq=None, bounds=None):
        """
        Inicializa el modelo de programación lineal.

        :param objective_coeffs: Coeficientes de la función objetivo (minimizar c^T x).
        :param lhs_ineq: Coeficientes de las restricciones de desigualdad (A x <= b).
        :param rhs_ineq: Lado derecho de las restricciones de desigualdad (b).
        :param lhs_eq: Coeficientes de las restricciones de igualdad (A_eq x = b_eq).
        :param rhs_eq: Lado derecho de las restricciones de igualdad (b_eq).
        :param bounds: Límites para las variables (por ejemplo, (0, None) para no-negatividad).
        """
        self.objective_coeffs = objective_coeffs
        self.lhs_ineq = lhs_ineq
        self.rhs_ineq = rhs_ineq
        self.lhs_eq = lhs_eq if lhs_eq is not None else []
        self.rhs_eq = rhs_eq if rhs_eq is not None else []
        self.bounds = bounds if bounds is not None else [(0, None)] * len(objective_coeffs)

    def solve(self):
        """
        Resuelve el problema de programación lineal utilizando el método simplex de SciPy.

        :return: Una tupla con la solución, el valor óptimo y el estado.
        """
        result = linprog(
            c=self.objective_coeffs,          # Coeficientes de la función objetivo (c)
            A_ub=self.lhs_ineq,               # Coeficientes de las restricciones de desigualdad (A x <= b)
            b_ub=self.rhs_ineq,               # Lado derecho de las restricciones de desigualdad (b)
            A_eq=self.lhs_eq,                 # Coeficientes de las restricciones de igualdad (A_eq x = b_eq)
            b_eq=self.rhs_eq,                 # Lado derecho de las restricciones de igualdad (b_eq)
            bounds=self.bounds,               # Límites para las variables
            method='simplex'                  # Método simplex
        )

        if result.success:
            return result.x, result.fun, result.status
        else:
            return None, None, result.status

    def display_results(self, solution, optimal_value, status):
        """
        Muestra los resultados obtenidos.

        :param solution: La solución óptima de las variables.
        :param optimal_value: El valor óptimo de la función objetivo.
        :param status: El estado del resultado (éxito o error).
        """
        if status == 0:
            print(f"Solución óptima encontrada:")
            print(f"Valores de las variables: {solution}")
            print(f"Valor óptimo de la función objetivo: {optimal_value}")
        else:
            print(f"Error al resolver el problema. Estado: {status}")
# Ejemplo de uso cambio de la nueva rama
if __name__ == "__main__":
    # Coeficientes de la función objetivo (Maximizar Z = 2000x1 + 3000x2)
    objective_coeffs = [-2000, -3000]  # Usamos valores negativos porque linprog minimiza por defecto.

    # Coeficientes de las restricciones de desigualdad (Ax <= b)
    lhs_ineq = [
        [1, 1.5],    # x1 + 1.5x2 <= 200 (capacidad de fabricación)
        [2, 1]       # 2x1 + x2 <= 175 (capacidad de control de calidad)
    ]
    rhs_ineq = [200, 175]  # Lado derecho de las restricciones

    # Coeficientes de las restricciones de igualdad (en este caso no hay restricciones de igualdad)
    lhs_eq = []
    rhs_eq = []

    # Límites para las variables (ninguna variable puede ser negativa)
    bounds = [(0, None), (0, None)]  # x1, x2 >= 0

    # Crear una instancia del solucionador
    solver = LinearProgrammingSolver(objective_coeffs, lhs_ineq, rhs_ineq, lhs_eq, rhs_eq, bounds)

    # Resolver el problema de programación lineal
    solution, optimal_value, status = solver.solve()

    # Mostrar los resultados
    solver.display_results(solution, optimal_value, status)