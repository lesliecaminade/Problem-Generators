import numpy as np

# Solving following system of linear equation
# 1a + 1b = 35
# 2a + 4b = 94
def sysLin2(a1, b1, c1, a2, b2, c2):
    a = np.array([[a1, b1],[a2,b2]])
    b = np.array([c1, c2])

    return np.linalg.solve(a,b)