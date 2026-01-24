import pyomo.environ as pyo
print(pyo.SolverFactory('scip').available())  # Check if SCIP solver is available
def solve_model(model):    
    solver = pyo.SolverFactory("scip")
    solver.options["limits/gap"] = 0.1 # Minimum gap between primal/dual (Stopping criterion)!!
    result = solver.solve(model, tee=True)
    #Imprime resultados
    print("Status:", result.solver.status)
    print("Objetivo máximo:", pyo.value(model.obj)) 
