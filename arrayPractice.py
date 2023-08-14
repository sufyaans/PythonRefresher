num = [2,3,4,5,5,6, 7]

#Write a Python program to calculate the sum of all elements in an array.
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

#Write a program that takes an array of numbers as input and removes any duplicate elements from the array.
def duplicates():
   
    new_list = set(num)
    print(list(new_list))
    #Finds duplicates
    # for i in range(len(num)):
    #     for j in range (i+1,len(num)):
    #         if num[i] == num[j]:
    #             num[j]


#Write a program that sorts the elements of an array in ascending order.
def sortArray():
    newList = [int(i) for i in num]
    newList.sort(reverse=True)
    print(newList)

#Write a program that takes two arrays as input and prints the elements that are common to both arrays.
def commonAttr():
    num2 = [2,8,1,3,7,0]
    sim = []
    for i in range(len(num)):
        for j in range(len(num2)):
            if num[i] == num2[j]:
               
                sim.append(num2[j])
    print(sim)
   
#Write a program that takes two arrays as input and prints the union of the two arrays (all unique elements from both arrays).
def diffAttr():
    num2 = [2,8,1,3,7,0]
    diff = list(set(num).symmetric_difference(num2))
    print(diff)



#Write a program that calculates and prints the average of the numbers in an array.
def findavg():
    x = sum(num)
    avg = x/len(num)
    print(avg)

#Implement a program that takes a sentence as input and returns the frequency of each word in the sentence using a dictionary.
sentence = "Hello how are you you look amazing are you good"
def freq():
    li = sentence.split()

    wordCount = dict()
    for i in li:
        if i in wordCount:
            wordCount[i] = wordCount[i] + 1
        else:
            wordCount[i] = 1
    print(wordCount)
   

#Implement a function that checks if a given array is a palindrome (reads the same forwards and backwards).
def palindrome():
    word = "racecar"
    
    wordRev = word[::-1]
    if (word!= wordRev):
        print(False)
    else:
        print(True)

#Implement a recursive function to calculate the nth Fibonacci number.

def Fibonacci(n):
    if n<= 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
    
def fibs(n):
    #n = 20
    if n<= 0:
        print("Incorrect input")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibs(n-1) + fibs(n-2)
    
print(fibs(10))

 
