def funct():
    a=int(input("Enter the number of list"))
    list1=[]
    for i in range(a):
        x=int(input("Enter your element"))
        list1.append(x)
    print(list1)
    even_add=0
    odd_add=0
    for i in list1:
        if i%2==0:
            even_add=even_add+i
        else:
            odd_add=odd_add+i
    print([even_add,odd_add])
funct()