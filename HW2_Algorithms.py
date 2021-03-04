##1 Fibonacci
def fibbonacci(number):
    if number < 0:
        return 'Not a valid value'
    if number == 0:
        return 0
    if number == 1:
        return [1]
    if number == 2:
        return [1]
    index = 3
    fib_1 = 1
    fib_2 = 1
    result = [fib_1, fib_2]
    while index < number:
        result.append(fib_1 +fib_2)
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        index += 1
    return result[-1]


##2 Zeros not for Heros
def no_zeros(number):
    if int(number) == 0:
        print("If you see just this number in your bank account, you are in trouble!")
    else:
        new = str(number).rstrip('0')
        print("Hero Number: " + str(new))

##3 Digital root is the recursive sum of all the digits in a number
def root_digit(number):
    digits = [digit for digit in str(number)]
    total = 0
    for i in digits:
        total+= int(i)
    while total > 9:
    ## This was the original iteration and the system never looks back to re-evaluate if the total is single digit
        new = [new_digit for new_digit in str(total)]
        print("This was previous total: " + str(total))
        total = 0
        for i in new:
            total+=int(i)
            print("This is underlying total:" + str(total))
    print("This final: " + str(total))
    return total
