def Euler(dydx, x_span, y0, n):
    """
    Euler Method for solve an ivp ODE

    parameter
    -----------------
        dydx: function to be integrated ATENTION! even don't have dependent variable(y) in dydx use lambda x,y:...
        x_span: [xi, xf] where xi and xf = initial and final values of independent variable
        y0: initial value of dependent variable
        n: number of steps
    
    return
    -----------------
        [1]: List of independent variable (x)
        [2]: List of solution for dependent variable (y)

    """
    xi = x_span[0]; xf = x_span[1]

    if(xf < xi): raise Exception("upper limit must be greater than lower")

    h = (xf-xi)/n

    #initial condition
    y = [y0]; x=[xi]

    for i in range(n):

        x.append(x[i] + h)
        y.append(y[i] + h * dydx(x[i], y[i]))
    
    return x, y