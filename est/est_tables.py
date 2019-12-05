#common EST tables interpolated
import sympy as sympy
spa, spb, spc, spd, spx, spy, spz = sympy.symbols('a b c d x y z', real = True)
spn = sympy.symbols('n', real = True)

#This uses the RAYLEIGH TABLE to find the reliability from the appropriate fademargin using linear interpolation. 
def reliability(fademargin):
    if fademargin >= 0 and fademargin < 8:
        x1 = 0
        x2 = 8
        y1 = 0
        y2 = 90
    if fademargin >= 8 and fademargin < 18:
        x1 = 8
        x2 = 18
        y1 = 90
        y2 = 99
    if fademargin >= 18 and fademargin < 28:
        x1 = 18
        x2 = 28
        y1 = 99
        y2 = 99.9
    if fademargin >= 28 and fademargin < 38:
        x1 = 28
        x2 = 38
        y1 = 99.9
        y2 = 99.99
    if fademargin >= 38 and fademargin < 48:
        x1 = 38
        x2 = 48
        y1 = 99.99
        y2 = 99.999
    if fademargin >= 48 and fademargin < 58:
        x1 = 48
        x2 = 58
        y1 = 99.999
        y2 = 99.9999    
    m = (y2 - y1)/(x2-x1)
    exp = m*(spx - x1) + y1
    y = exp.subs(spx,fademargin)
    y = float(y)
    return y

def fademargin(reliability):
    if reliability >= 0 and reliability < 90:
        x1 = 0
        x2 = 90
        y1 = 0
        y2 = 8
    if reliability >= 90 and reliability < 99:
        x1 = 90
        x2 = 99
        y1 = 8
        y2 = 18
    if reliability >= 99 and reliability < 99.9:
        x1 = 99
        x2 = 99.9
        y1 = 18
        y2 = 28
    if reliability >= 99.9 and reliability < 99.99:
        x1 = 99.9
        x2 = 99.99
        y1 = 28
        y2 = 38
    if reliability >= 99.99 and reliability < 99.999:
        x1 = 99.99
        x2 = 99.999
        y1 = 38
        y2 = 48
    if reliability >= 99.999 and reliability < 99.9999:
        x1 = 99.999
        x2 = 99.9999
        y1 = 48
        y2 = 58        
    m = (y2 - y1)/(x2-x1)
    exp = m*(spx - x1) + y1
    y = exp.subs(spx,reliability)
    y = float(y)
    return y        