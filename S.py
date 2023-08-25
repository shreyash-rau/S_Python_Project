# define all the function/opration that used in calculator

def add(n1 , n2):
    return n1 + n2
def sub(n1 , n2):
    return n1 - n2
def mul(n1 , n2):
    return n1 * n2
def div(n1 , n2):
    return n1 / n2

print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")

select = int(input('Select Operation Form Above as - 1 2 3 4 :'))
n1 = int(input('yur 1st number is : '))
n2 = int(input('yur 2nd number is : '))

if select == 1:
    print(n1, '+' , n2, '=', add(n1, n2))
elif select == 2:
    print(n1, '-' , n2, '=', sub(n1, n2)) 
elif select == 3:
    print(n1, '*' , n2, '=', mul(n1, n2))       
elif select == 4:
    print(n1, '/' , n2, '=', div(n1, n2))
else:
    print('Enter Valid Number and Operation Code ')    