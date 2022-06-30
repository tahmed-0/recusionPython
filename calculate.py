def recusive_multiply(num1, num2):
    if num2 == 0:
        return 0
    else:
        return (num1 + recusive_multiply(num1, num2-1))

n1 = 2
n2 = 400

print(recusive_multiply(n1, n2))


def resurive_div(num1, num2):
    if num2 == 0:
        return -1
    if num1 == num2:
        return 1
    if num1 < num2:
        return 0
    else:
        return  1 + resurive_div(num1-num2, num2)

num1 = 7
num2 = 3

print (resurive_div(num1, num2))





