#Newton-Rhapson Method using sympy
#https://devopslog.wordpress.com/2012/12/23/newton-raphson-method-using-python-sympy/


#!/usr/bin/env python
import argparse
import math
import sys
import time
import sympy
 
def get_parameters():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f", "--function",
        help="Define a function"
    )
    parser.add_argument("-s", "--starting", 
                        help="Starting point value", type = float, default = 0.0)
    parser.add_argument("-p", 
                        "--precision", 
                        help="Convergence precision", 
                        type = float, default = 5*10**(-6))
    return parser.parse_args()
 
if __name__ == "__main__":
    parameters = get_parameters()
 
    sym_x = sympy.Symbol('x')
    # convert the given function to a symbolic expression
    try:
        fx = sympy.S(args.function)
    except sympy.sympify.SympifyError:
        sys.exit('Unable to convert function to symbolic expression.')
 
    # calculate the differential of the function
    dfdx = diff(fx, Symbol('x'))
 
    # e is the relative error between 2 consecutive 
    # estimations of the root
    e = 1
    x0 = parameters.starting
    iterations = 0
start_time = time.time()
while e > args.precision:
        # new root estimation
        try:
            r = x0 - fx.subs({sym_x: x0}) / dfdx.subs({sym_x: x0})
        except ZeroDivisionError:
            print ("Function derivative is zero. Division by zero, program will terminate.")
            raise
        # relative error
        e = abs((r - x0) / r)
        iterations += 1
        x0 = r
 
total_time = time.time() - start_time
 
print ('Function:')
sympy.pprint(fx)
print ('Derivative:')
sympy.pprint(dfdx)
print ('Root %10.6f calculated after %d iterations' % (r, iterations))
print ('Function value at root %10.6f' % fx.subs({sym_x : r}))
print ('Finished in %10.6f seconds'% total_time)