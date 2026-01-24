import pyomo.environ as pyo
def resolve_modelo(k,alpha,n,weight,value,capacity):
    # Creates the pyomo model
    model = pyo.ConcreteModel()
    # Bounds of i and j indices
    model.I = pyo.RangeSet(0,n-1)
    model.J = pyo.RangeSet(0,k-1) if k>0 else pyo.RangeSet(0,0)

    # Defines Xij in [0,2^k]
    if k>1:
        model.x = pyo.Var(model.I, model.J, bounds=(0,2**(k)))
    else:
        model.x = pyo.Var(model.I,model.J, bounds=(0,1))
    #Obs: Xi belongs to [0,2^(k+1)-1] because its a sum of the variables Xij

    #Objective Function
    def func_obj(m):
        return sum(value[i]*m.x[i,j] for i in m.I for j in m.J) + alpha*sum(m.x[i,j]*(m.x[i,j]-2**j) for i in m.I for j in m.J) #"Linear" penalization
        #return sum(v[i]*m.x[i,j] for i in m.I for j in m.J) - alpha*sum((m.x[i,j]*(m.x[i,j]-2**j))**2 for i in m.I for j in m.J) #Quadratic penalization
    model.obj = pyo.Objective(rule=func_obj, sense=pyo.maximize)

    #Capacity Constrain
    def restricao_weight(m):
        return sum(weight[i]*m.x[i,j] for i in m.I for j in m.J) <= capacity
    model.cap = pyo.Constraint(rule=restricao_weight)

    #Quadratic Constrains
    def restricoes_quadraticas(m):
        return sum(m.x[i,j]*(m.x[i,j]-2**j) for i in m.I for j in m.J) == 0
    model.quad_global = pyo.Constraint(rule=restricoes_quadraticas)
    return model
    #Solves and print solution
