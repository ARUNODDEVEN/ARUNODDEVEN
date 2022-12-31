def sum_of_list(l):
    i=0
    summ=0
    while i<len(l):
        summ+=l[i]
        i+=1
    return summ

s=sum_of_list([1,2,3,4])
print(s)
    
