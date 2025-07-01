a = [1,2,8,5,9,3]
max = a[0]
for i in range(len(a)):
    if(a[i] > max):
        max = a[i]
print("maximum value is", max)