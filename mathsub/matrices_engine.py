from generator import random_handler as ran
from generator import constants_conversions as c
import sympy
import numpy
import math
import random

x, y, z = sympy.symbols('x y z', real = True)#generic variables

def element():
	return random.randint(-9, 9)

def row_echelon(A):
    """ Return Row Echelon Form of matrix A """

    # if matrix A has no columns or rows,
    # it is already in REF, so we return itself
    r, c = A.shape
    if r == 0 or c == 0:
        return A

    # we search for non-zero element in the first column
    for i in range(len(A)):
        if A[i,0] != 0:
            break
    else:
        # if all elements in the first column is zero,
        # we perform REF on matrix from second column
        B = row_echelon(A[:,1:])
        # and then add the first zero-column back
        return numpy.hstack([A[:,:1], B])

    # if non-zero element happens not in the first row,
    # we switch rows
    if i > 0:
        ith_row = A[i].copy()
        A[i] = A[0]
        A[0] = ith_row

    # we divide first row by first element in it
    A[0] = A[0] / A[0,0]
    # we subtract all subsequent rows with first row (it has 1 now as first element)
    # multiplied by the corresponding element in the first column
    A[1:] -= A[0] * A[1:,0:1]

    # we perform REF on matrix from second row, from second column
    B = row_echelon(A[1:,1:])

    # we add first row and first (zero) column, and return
    return numpy.vstack([A[:1], numpy.hstack([A[1:,:1], B]) ])

class Matrix():
	def __init__(self, *args):
		try:
			matrix = args[0]
			self.matrix = numpy.array(matrix)
		except:
			pass

	def init_random(self, *args, **kwargs):
		try:
			rows = kwargs['rows']
			cols = kwargs['cols']
		except:
			rows = 3
			cols = 3

		array = [[element() for i in range(cols)] for j in range(rows)]
		self.matrix = numpy.array(array)
		self.rows = rows
		self.cols = cols

	def addition(self, object):
		return Matrix(self.matrix + object.matrix)

	def multiply(self, object):
		return Matrix(self.matrix.dot(object.matrix))

	def transpose(self):
		return Matrix(self.matrix.transpose())

	def submatrix(self, row, col):
		#note that row and col in the arguments are math version. (starts at 1)
		#and that row col for numpy starts at 0.

		return Matrix(numpy.delete(numpy.delete(self.matrix, row - 1, axis = 0), col - 1, axis = 1))

	def minor(self, row, col):
		sub = self.submatrix(row, col)
		return numpy.linalg.det(sub.matrix)

	def cofactor(self, row, col):
		return self.minor(row, col) * (-1)**(row + col)

	def cofactor_matrix(self):
		return Matrix([[round(self.cofactor(i, j),4) for j in range(self.cols)] for i in range(self.rows)])

	def adjugate(self):
		return self.cofactor_matrix().transpose()

	def determinant(self):
		return numpy.linalg.det(self.matrix)

	def inverse(self):
		return Matrix(numpy.linalg.inv(self.matrix))

	def ref(self):
		data = self.matrix
		return Matrix(row_echelon(data))




class Addition():
	def __init__(self):

		rows = random.randint(2,4)
		cols = random.randint(2,4)

		mat_a = Matrix()
		mat_a.init_random()
		mat_b = Matrix()
		mat_b.init_random()

		result = mat_a.addition(mat_b)

		self.question = f"""Calculate 
{mat_a.matrix}
+
{mat_b.matrix}
"""

		self.answer = f"""{result.matrix}"""

class Multiplication():
	def __init__(self, *args, **kwargs):

		common = random.randint(2,4)
		rows = random.randint(2, 4)
		cols = random.randint(2, 4)

		mat_a = Matrix()
		mat_a.init_random(rows = rows, cols = common)
		mat_b = Matrix()
		mat_b.init_random(rows = common, cols = cols)

		result = mat_a.multiply(mat_b)

		self.question = f"""Calculate
{mat_a.matrix} 
x
{mat_b.matrix}"""

		self.answer = f"""{result.matrix}"""

		
class Transpose():
	def __init__(self, *args, **kwargs):

		mat_a = Matrix()
		mat_a.init_random()

		result = mat_a.transpose()

		self.question = f"""Determine the transpose of 
{mat_a.matrix}."""
		self.answer = f"""{result.matrix}"""


class Submatrix():
	def __init__(self, *args, **kwargs):
		mat_a = Matrix()
		mat_a.init_random()
		row = random.randint(1, mat_a.rows)
		col = random.randint(1, mat_a.cols)
		result = mat_a.submatrix(row, col)

		self.question = f"""Determine the submatrix({row}, {col}) of the matrix 
{mat_a.matrix}"""
		self.answer = f"""{result.matrix}"""

class Minor():
	def __init__(self, *args, **kwargs):
		mat_a = Matrix()
		mat_a.init_random()
		row = random.randint(1, mat_a.rows)
		col = random.randint(1, mat_a.cols)
		result = mat_a.minor(row, col)

		self.question = f"""Determine the minor({row}, {col}) of the matrix 
{mat_a.matrix}"""
		self.answer = f"""{round(result,4)}"""

class Cofactor():
	def __init__(self, *args, **kwargs):
		mat_a = Matrix()
		mat_a.init_random()
		row = random.randint(1, mat_a.rows)
		col = random.randint(1, mat_a.cols)
		result = mat_a.cofactor(row, col)

		self.question = f"""Determine the cofactor({row}, {col}) of the matrix 
{mat_a.matrix}"""
		self.answer = f"""{round(result,4)}"""

class Cofactor_Matrix():
	def __init__(self, *args, **kwargs):
		mat_a = Matrix()
		mat_a.init_random()
		result = mat_a.cofactor_matrix()

		self.question = f"""Determine the cofactor matrix of the matrix
{mat_a.matrix}"""
		self.answer = f"""{result.matrix}"""

class Adjugate():
	def __init__(self, *args, **kwargs):

		mat_a = Matrix()
		mat_a.init_random()
		result = mat_a.adjugate()

		self.question = f"""Determine the adjugate matrix of the matrix
{mat_a.matrix}"""
		self.answer = f"""{result.matrix}"""	

class Determinant():
	def __init__(self, *args, **kwargs):

		mat_a = Matrix()
		dim = random.randint(2,4)
		mat_a.init_random(rows = dim, cols = dim )
		result = mat_a.determinant()

		self.question = f"""Determine the determinant of the matrix
{mat_a.matrix}"""
		self.answer = f"""{round(result, 4)}"""	

class Inverse():
	def __init__(self, *args, **kwargs):
		mat_a = Matrix()
		dim = random.randint(2,3)
		mat_a.init_random(rows = dim, cols = dim )
		result = mat_a.inverse()

		self.question = f"""Determine the inverse of the matrix
{mat_a.matrix}"""
		self.answer = f"""{result.matrix}"""	

class Row_Echelon_Form():
	def __init__(self, *args, **kwargs):
		mat_a = Matrix()


		dim = random.randint(2,3)
		mat_a.init_random(rows = dim, cols = dim )
		before = numpy.copy(mat_a.matrix)
		result = mat_a.ref()

		self.question = f"""Determine the reduced row echelon form of the matrix
{before}"""
		self.answer = f"""{result.matrix}"""




		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		