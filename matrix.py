def buildmatrix(array): #Вывод матрицы в виде строки
	string = ''
	for i in array:
		string+=str(i)+'\n'
	return(string)
def xMatrix(matrix1,matrix2): #Умножение матрицы на матрицу
	resultmatrix =[]
	resultmatrix1 = []
	if len(matrix1[0]) == len(matrix2):
		for s in range(len(matrix2[0])):
			for k in range(len(matrix2)):
				tempmatrix = []
				for i in range(len(matrix1[0])):
					tempmatrix.append(matrix1[k][i]*matrix2[i][s])
				resultmatrix.append(sum(tempmatrix))
		m=0
		while m<len(resultmatrix):
			resultmatrix1.append(resultmatrix[m:m+len(matrix1)])
			m+=3
		return(resultmatrix1)
	else:
		return('Error')
def xNum(matrix,number): #умножение матрицы на число
	for i in range(len(matrix)):
		for k in range(len(matrix[0])):
			matrix[i][k]*=number
	return(matrix)
def addMatrix(matrix1,matrix2): #суммирование матриц
	resultmatrix = []
	if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
		for s in range(len(matrix1)):
			tempmatrix=[]
			for k in range(len(matrix1[0])):
				tempmatrix.append(matrix1[s][k]+matrix2[s][k])
			resultmatrix.append(tempmatrix)
		return(resultmatrix)
	else:
		return('Error')
def transposition(matrix): #транспонирование матрицы
	resultmatrix = [list(i) for i in zip(*matrix)]
	return(resultmatrix)
