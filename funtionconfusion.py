def compute(list_name):
    for items in list_name:
        print(items+2)

def addition(list_name):
    sum = 0
    print("This is addition section")
    for items in list_name:
        sum += items
    print(sum)

def list_prepn():
    b = []
    x = int(input("Enter the number of elements you want"))

    for i in range(0,x):
        a = int(input("Enter the numbers"))
        b.append(a)
    compute(b)
    addition(b)

if __name__ == "__main__":
    list_prepn()
