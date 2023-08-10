import sympy

def check_big_o(expression1, expression2, variable):
    return sympy.limit(expression1 / expression2, variable, sympy.oo) == 0

def check_big_omega(expression1, expression2, variable):
    return sympy.limit(expression1 / expression2, variable, sympy.oo) == sympy.oo

variable = sympy.symbols('n')

expression1 = variable**2 * (variable**2 + 8 * variable**3)
expression2 = variable**5 * sympy.log(variable)

is_big_o = check_big_o(expression1, expression2, variable)
is_big_omega = check_big_omega(expression1, expression2, variable)

if is_big_o:
    print("The first expression is O of the second expression.")
else:
    print("The first expression is not O of the second expression.")

if is_big_omega:
    print("The first expression is Omega of the second expression.")
else:
    print("The first expression is not Omega of the second expression.")
