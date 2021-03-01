def func():
    list1=['Aadil','Sabina','Python','Aadil']
    count=0
    list2=[]
    for i in range(len(list1)):
        if i in list2:
            count=count+1
            if count>1:
                print(list1[i]+'s')
        else:
            print(list1[i])
func()