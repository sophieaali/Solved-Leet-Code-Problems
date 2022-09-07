# Fizz Buzz

# Given an integer n, return a string array answer (1-indexed) where:
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.

# solution 1:
def fizzBuzz(n):
    newList = []
    for i in range(1, n+1):
        if (i%3 == 0) and (i%5 == 0):
            newList.append("FizzBuzz")
        elif i%3 == 0:
            newList.append("Fizz")
        elif i%5 == 0:
            newList.append("Buzz")
        else:
            newList.append(str(i))
    return newList
 
# Example 1:
print(fizzBuzz(3))
# Output: ["1","2","Fizz"]

# Example 2:
print(fizzBuzz(5))
# Output: ["1","2","Fizz","4","Buzz"]

# Example 3:
print(fizzBuzz(15))
# Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]



# solution 2:
def fizzBuzz(n):
    ansList = []
    for i in range(1, n+1):
        ansItem = ''
        if i%3 == 0:
            ansItem += 'Fizz'
        if i%5 == 0:
            ansItem += 'Buzz'
        if not (i%5 == 0) and not (i%3 == 0):
            ansItem += str(i)
        ansList.append(ansItem)

    return ansList



# Example 1:
print(fizzBuzz(3))
# Output: ["1","2","Fizz"]

# Example 2:
print(fizzBuzz(5))
# Output: ["1","2","Fizz","4","Buzz"]

# Example 3:
print(fizzBuzz(15))
# Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

 