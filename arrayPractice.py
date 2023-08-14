#Write a Python program to calculate the sum of all elements in an array.

num = [2,3,4,5,6]

def calcSum():
    #num = [2,3,4,5,6]
    sum = 0

    for i in range(len(num)):
        sum = sum + num[i]

    print(sum)

def calcSum2():
    #num = [5,2,7,4,6,9,2]
    total = 0

    for i in range(len(num)):
        total = total - num[i]

    print(total)


#Given an array, write a program to find the maximum and minimum values in the array.
def arrMax():
    print(max(num))

def arrMin():
    print(min(num))

#Write a program to reverse an array in-place (without using any additional memory).
def reverse():
    print(list(reversed(num)))


#Create a program that takes a list of numbers as input and returns a new list containing only the even numbers from the input list.
def evenOut():
    val = input("Please enter a list of values separated by ',' ")
    li = list(val.split(","))
    newList = [int(i) for i in li]
    newList2 = []
    
    for x in newList:
        if x % 2 == 0:
            newList2.append(x)
    print(newList2)

#Write a program that takes an array and a number as input and checks if the number is present in the array.
def arraySearch():
    val = int(input("Enter a digit to search for in the list: "))
    if val in num:
        print(f"{val} found in the list")
    else:
        print(f"{val} not found in the list")

arraySearch()