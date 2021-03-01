def function_name(num):
    result=False
    if num>0:
        result=False
    a=str(num)
    for i in a:
        if i==a[0]:
            result=True
        else:
            result=False
            break
    return result
a=function_name(11)
print(a)