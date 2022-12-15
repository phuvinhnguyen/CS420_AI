a = [10,2,5,3,1,7]
indexs = sorted(range(len(a)), key=lambda i: a[i])[-3:]
print(indexs)