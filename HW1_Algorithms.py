##1 Sum of 3 modified
def digit_sum(number):
    sum_digits = 0
    for digit in str(number):
        sum_digits += int(digit)
        return sum_digits

##2 Find Max Number
def find_max():
    input_list = []
    for i in range(3):
        input_value = input("Please enter values. We will need 3 numbers: ")
        input_list.append(input_value)
    input_list.sort(reverse=True)
    print(input_list[0])

##3 Count Odd and even numbers.
def odd_even_cut(number):
    even_count = 0
    odd_count = 0
    for digit in str(number):
        if int(digit) % 2 == 0:
            even_count+=1
        else:
            odd_count+=1
    print(f'Odd: {odd_count} Even: {even_count}')
