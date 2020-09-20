operator = input("Enter the operation (a-add, s-sub, m-multi, d-div): ")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print ("User Entered: Operator {} Number 1: {} Number 2: {}".format (operator,num1,num2)) 
if operator =='a':
    total = num1 + num2
    oper_sym = '+'
elif operator == 's':
    total = num1 - num2
    oper_sym = '-'
elif operator == 'm':
    total = num1 * num2
    oper_sym = '*'
elif operator == 'd':
    if num2 == 0:
        print ("You can't divide a number by zero")
        exit (1)
    total = num1 / num2
    oper_sym = '/'
else:
    print ("You have entered the wrong operator!")
    exit(1)

print ("Total of {} {} {} = {}".format(num1, oper_sym, num2,total))
exit (0)