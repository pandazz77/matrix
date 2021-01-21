class Matrix:
	def __init__(self,matrix):
		self.matrix = matrix
		for ar in range(len(matrix)):
			if len(matrix[ar]) != len(matrix[ar-1]):
				raise Exception('Bad size')

		if len(matrix) >1:
			self.size = (len(matrix),len(matrix[1]))
		else:
			self.size = 1

	def __str__(self): #Поведение объекта при вызове print()
		string = ''
		for i in self.matrix:
			string+=str(i)+'\n'
		return string

	def __iter__(self):
		return iter(self.matrix)

	def __mul__(self,other): #Поведение объекта при умножении
		if isinstance(other, int): #Умножение матрицы на число
			for i in range(len(self.matrix)):
				for k in range(len(self.matrix[0])):
					self.matrix[i][k]*=other
			return matrix
		elif isinstance(other,Matrix): #Умножение матрицы на матрицу
			if self.size[0] == other.size[1]:
				resultmatrix = [[0 for row in range(other.size[1])] for col in range(self.size[0])]
				for i in range(self.size[0]):
					for j in range(other.size[1]):
						for k in range(self.size[1]):
							resultmatrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
				return Matrix(resultmatrix)

	def __pow__(self, other): #Поведение объекта при вовзедении в степень
		if other == 1:
			return Matrix(self.matrix)
		pr = Matrix(self.matrix)*Matrix(self.matrix)
		for i in range(other-2):
			pr*=Matrix(self.matrix)
		return pr

	def __add__(self,other): #Поведение объекта при суммировании (суммирование матриц)
		if isinstance(other, Matrix):
			resultmatrix = []
			if self.size == other.size:
				for s in range(len(self.matrix)):
					tempmatrix=[]
					for k in range(len(self.matrix[0])):
						tempmatrix.append(self.matrix[s][k]+other.matrix[s][k])
					resultmatrix.append(tempmatrix)
				return Matrix(resultmatrix)
			else:
				raise Exception('Bad size')
		elif isinstance(other, int):
			return NotImplemented
		else:
			return NotImplemented

	def __sub__(self,other): #Поведение объекта при вычитании (вычитание матриц)
		if isinstance(other, Matrix):
			resultmatrix = []
			if self.size == other.size:
				for s in range(len(self.matrix)):
					tempmatrix=[]
					for k in range(len(self.matrix[0])):
						tempmatrix.append(self.matrix[s][k]-other.matrix[s][k])
					resultmatrix.append(tempmatrix)
				return Matrix(resultmatrix)
			else:
				raise Exception('Bad size')
		elif isinstance(other, int):
			return NotImplemented
		else:
			return NotImplemented
	def transp(self):
		return Matrix([list(i) for i in zip(*self.matrix)])
	def det(self):
		if self.size[0] != self.size[1]:
			raise Exception('Bad size')
		m = self.matrix
		def getMatrixMinor(m,i,j):
			return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]
		def getMatrixDeternminant(m):
			if len(m) == 2:
				return m[0][0]*m[1][1]-m[0][1]*m[1][0]

			determinant = 0
			for c in range(len(m)):
				determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
			return determinant
		return getMatrixDeternminant(m)
