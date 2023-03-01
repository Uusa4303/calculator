# define the function to perform calculations
def calculate(numbers, operators):
    result = numbers[0]
    for i in range(1, len(numbers)):
        if operators[i-1] == '+':
            result += numbers[i]
        elif operators[i-1] == '-':
            result -= numbers[i]
        elif operators[i-1] == '*':
            result *= numbers[i]
        elif operators[i-1] == '/':
            if numbers[i] == 0:
                result = 'infinity'
            else:
                result /= numbers[i]
        else:
            result = 'invalid operator'
            break
    return result

# get user input
numbers = []
operators = []
while True:
    try:
        num = float(input("Enter a number: "))
    except ValueError:
        break
    numbers.append(num)
    if len(numbers) > 1:
        op = input("Enter an operator (+, -, *, /) or '=' to calculate: ")
        if op == '=':
            break
        operators.append(op)
        
# perform the calculation and display the result
result = calculate(numbers, operators)
print("Result: ", result)