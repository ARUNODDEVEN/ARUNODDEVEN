
def maxi(l):
    i = 0
    maximum = l[0]
    while i < len(l):
        if l[i] >= maximum:
            maximum = l[i]
        i += 1
    return maximum


k = maxi([12, 23, 3, 4, 54, 65, 65, 100,6])
print(k)
