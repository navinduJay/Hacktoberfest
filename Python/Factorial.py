def factorial(number):
    if number < 1:
        return 1
    else:
        return number * factorial(number-1)


userInput = int(input('Enter a number: '))
result = factorial(userInput)

print('Factorial of ' + str(userInput) + ' is ' + str(result))
