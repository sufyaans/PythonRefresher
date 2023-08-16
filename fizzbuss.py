'''
Write a program that returns the numbers from N to M both inclusive. 
But for multiples of three give "Fizz" instead of the number and for the multiples of five give "Buzz". 
For numbers which are multiples of both three and five, give "FizzBuzz".
'''
def run(N, M):
    sequence = []
    for num in range(N, M + 1):
        if num % 3 == 0 and num % 5 == 0:
            sequence.append("FizzBuzz")
        elif num % 3 == 0:
            sequence.append("Fizz")
        elif num % 5 == 0:
            sequence.append("Buzz")
        else:
            sequence.append(str(num))
    return ",".join(sequence)

print(run(3,20))