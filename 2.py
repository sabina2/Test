def largest(list1):
    list1=[2,3,4,692,10,90]
    max=0
    for i in list1:
        if i%2==0 and i>max:
            max=i
    if max==0:
        return -1
    return max
list_name=[2,1,312,534,665,342]
a=largest(list_name)
print("The largest even number is",max)

