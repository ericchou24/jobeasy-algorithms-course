##1 Fibonacci - Recursive
def fibbonacci(number):
    if number < 0:
        return 'Not a valid value'
    elif number == 0:
        return 0
    elif number == 1 or number == 2:
        return 1
    else:
        return fibbonacci(number-1) + fibbonacci(number-2)

##2 Zeroes not heros - Recursive
def no_zeros(number):
    if number == 0:
        return 0
    if number % 10 == 0:
        return no_zeros(number // 10)
    return number

##3 Digital Root 0 Recursive
def root_digit(number):
    digits = [digit for digit in str(number)]
    total = 0
    for i in digits:
        total+= int(i)
    if total < 9:
        return total
    else:
        return root_digit(total)

## Divisors used for #5 and #6
def divisors(number):
    result = []
    for item in range(1, number):
        if number % item == 0:
            result.append(item)
    return result

##5 Perfect Number
def perfect_number(number):
    x = divisors(number)
    if sum(x) == number:
        return f'{number} is a perfect number'
    else:
        return f'{number} is not a perfect number'

##6 Amicable numbers
def amicable_number(num1, num2):
    x = divisors(num1)
    y = divisors(num2)
    if sum(x) == num2 or sum(y) == num1:
        ##print(f'{num1} is an amicable number with {num2}')
        return f'{num1} is an amicable number with {num2}'
    else:
        ##print(f'{num1} and {num2} are not ammicable numbers')
        return f'{num1} and {num2} are not ammicable numbers'

##print(divisors(10))
##print(perfect_number(6))
##print(amicable_number(284,221))
##no_zeros(960000)
##print(fibbonacci(5))
##print(root_digit(16))
##print(root_digit(942))
##print(root_digit(132189))
##print(root_digit(493193))