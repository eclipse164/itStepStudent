print("Hello World")
print("fghg")
a = 5
print(a+4)
print("edited by another user")



def calc(num1, num2, operation):
    if operation == "+":
        return num1+num2
    elif operation == "-":
        return num1-num2
    elif operation == "/":
        return num1/num2
    elif operation == "*":
        return num1*num2


a = int(input())
b = int(input())
op = input()
print(calc(a,b,op))

print(calc(10, 15, "+"))
print(calc(10, 15, "-"))
print(calc(10, 15, "/"))
print(calc(10, 15, "*"))
