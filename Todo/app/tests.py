l='"My name is Makad!"'

l1=l.split(' ')
# print(l1)
x=[]

for i in l1:
    if i.isalpha():
        x.append(i[::-1])
    else:
        t=''
        for j in i[::-1]:
            if j.isalpha():
                t+=j
            else:
                t+='1'
        s=''
        for j in range(len(i)):
            if t[j]=='1':
                s+=i[j]
            else:
                s+=t[j]

        x.append(t)
print(x)
# print(' '.join(x))


# s=list(i[::-1] for i in l1 )
# print(' '.join(s))