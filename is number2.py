num1= input("enter num 1")
num2 = input("enter num 2")
try:
    if num1.isnumeric() == False:
        raise("num1 is not number")
    elif num2.isnumeric() == False:
        raise("num2 is not number")
    else:
        res = int(num1)+int(num2)
        print(str(res))
except Exception as e:
    print(e)