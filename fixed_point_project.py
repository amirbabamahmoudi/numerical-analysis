'''

Amir Babamahmoudi	9713006


Golshid Shokoofandeh 9513422


pouria Soltani 9712028

'''


import sympy
from sympy import solveset, sympify, diff


x = sympy.Symbol('x')
func = input("please enter your function with symbol 'x': ")  #for example : 3 * (x ** 2) - 5*x
func = sympify(func)

domain_floor = float(input("enter domain floor : "))
domain_ceil = float(input("enter domain ceil : "))

roots_of_derivatives = solveset(diff(func) , x)

max_of_func = -(sympy.oo)
min_of_func = (sympy.oo)

boolean = False

for i in roots_of_derivatives:         #finding range of func
    result = func.evalf(subs = {x : i})
    if result > max_of_func :
        max_of_func = result
    if result < min_of_func :
        min_of_func = result
        
print("**************")

if max_of_func <= domain_ceil and max_of_func >= domain_floor and min_of_func >= domain_floor and max_of_func <= domain_ceil:
    print("this function contains at least one fixed point")
    boolean = True
else :
    print("We can't declare anything about the fixed points")


#creating serie

if boolean:
    serie = []
    x0 = int(input("enter the point you wanna start the serie from :"))
    x1 = func.evalf(subs = {x : x0})
    serie.append(x1)
    for i in range(1 , 10):
        serie.append(func.evalf(subs={x: serie[i - 1]}))
    print(serie)
    



