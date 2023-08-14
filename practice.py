#Given a matrix (2D array), write a function to calculate the sum of each row and each column and return the results as two separate lists

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


def sumOfRows(matrix):
    rowLen = len(matrix)

    rowSums = []
    for row in matrix:
        rowSum = 0
        for num in row:
            rowSum += num
        rowSums.append(rowSum)
    print(rowSums)


#Create a program that finds and prints the index of the first occurrence of a specific element in an array.
sentence = "hello my name is sufyaan"

def listSearch():
    arr = sentence.split()
    arr[3]

listSearch()