n=1
i=0
f=[]
while i<=25:
    if i==0:
        f.append(0)
    elif i==1:
        f.append(1)
    elif i>1:
        f.append(f[i-1]+f[i-2])
    i=i+1
print f[n]
