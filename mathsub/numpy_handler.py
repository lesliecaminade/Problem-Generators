import numpy as np

def sysLin2(a1, b1, c1, a2, b2, c2):
    a = np.array([[a1, b1],[a2,b2]])
    b = np.array([c1, c2])
    x = np.linalg.solve(a,b)
    return tuple(x)
    
def sysLin3(a1, b1, c1, d1, a2, b2, c2, d2, a3, b3, c3, d3):
    a = np.array([[a1, b1, c1], [a2, b2, c2], [a3, b3, c3]])
    b = np.array([d1, d2, d3])
    x = np.linalg.solve(a, b)
    return tuple(x)