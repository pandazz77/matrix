matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[11],[12],[13]]

def multiplymatrix(matrix1,matrix2):
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
def multiplymatrixnum(matrix,number):
	for i in range(len(matrix)):
		for k in range(len(matrix[0])):
			matrix[i][k]*=number
	return(matrix)
def addmatrix(matrix1,matrix2):
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
def transpmatrix(matrix):
	tempmatrix=[]
	resultmatrix=[]
	for i in range(len(matrix)):
		for k in range(len(matrix[0])):
			tempmatrix.append(matrix[k][i])
	m=0
	while m<len(tempmatrix):
		resultmatrix.append(tempmatrix[m:m+3])
		m+=3
	return(resultmatrix)
print(multiplymatrix(matrix1,matrix2))
print(addmatrix(matrix1,matrix2))
print(transpmatrix(matrix1))
print(multiplymatrixnum(matrix1,2))
