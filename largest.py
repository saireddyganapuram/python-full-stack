a = [1,2,8,5,9,3]
max = 0
for i in range(len(a)):
    if(a[i] > max):
        sec=max
        max = a[i]
print("maximum value is", sec)
