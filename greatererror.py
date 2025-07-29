num1= input("enter num 1")
try:
    if num1 > 100:
        raise("num1 is  greater than 100")
    else:
        res = int(num1)
        print(int(res))
except Exception as e:
    print(e)