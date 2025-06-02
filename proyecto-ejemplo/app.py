import pyomo.environ as pyo

def solve_simple_lp():
    """
    Resuelve un problema de Programación Lineal (PL) sencillo usando Pyomo y GLPK.

    Maximizar: 2x + 3y
    Sujeto a:
        x + y <= 4
        2x + y <= 5
        x >= 0
        y >= 0
    """
    # 1. Crear un modelo concreto
    model = pyo.ConcreteModel(name="Simple LP Problem")

    # 2. Definir las variables de decisión
    # Se definen como no negativas por defecto, lo cual coincide con x >= 0, y >= 0
    model.x = pyo.Var(domain=pyo.NonNegativeReals)
    model.y = pyo.Var(domain=pyo.NonNegativeReals)

    # 3. Definir la función objetivo
    # Por defecto, Pyomo minimiza. Para maximizar, usamos sense=pyo.maximize.
    model.objective = pyo.Objective(expr=2 * model.x + 3 * model.y, sense=pyo.maximize)

    # 4. Definir las restricciones
    model.constraint1 = pyo.Constraint(expr=model.x + model.y <= 4)
    model.constraint2 = pyo.Constraint(expr=2 * model.x + model.y <= 5)

    print("Modelo de Pyomo creado:")
    model.pprint()
    print("-------------------------------------")

    # 5. Resolver el problema
    # Asegúrate de que el solver 'glpk' esté disponible en el PATH o especifica la ruta.
    # Dentro de nuestro Dockerfile, lo instalaremos.
    solver = pyo.SolverFactory('glpk')
    results = solver.solve(model, tee=True) # tee=True muestra la salida del solver

    print("-------------------------------------")
    print("Resultados de la optimización:")
    # Comprobar el estado de la solución
    if (results.solver.status == pyo.SolverStatus.ok) and \
       (results.solver.termination_condition == pyo.TerminationCondition.optimal):
        print("¡Solución óptima encontrada!")
        print(f"Valor de x: {pyo.value(model.x)}")
        print(f"Valor de y: {pyo.value(model.y)}")
        print(f"Valor óptimo de la función objetivo: {pyo.value(model.objective)}")
    elif results.solver.termination_condition == pyo.TerminationCondition.infeasible:
        print("El problema es infactible.")
    else:
        print(f"Estado del solver: {results.solver.status}")
        print(f"Condición de terminación: {results.solver.termination_condition}")

    return results

if __name__ == '__main__':
    print("Iniciando la resolución del problema de optimización con Pyomo...")
    solve_simple_lp()
    print("Proceso de optimización finalizado.")
