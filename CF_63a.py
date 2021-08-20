#my attempt
l=list(map(int,input().split()))
c=0
for i in range(l[4],l[5]+1):
  for k in range(4):
    z=i%l[0]
    for j in range(1,3):
      z=z%l[j]
      for m in range(2,4):
        z=z%l[m]
        z=z%l[5-m]
  if z==i:
    c+=1
print(c)



#efficent soutions to learn from

#1
*P, a, b = map(int, input().split())
 
print(max(0, min(b-a+1, min(P)-a)))






#2
a,b,c,d,e,f=map(int,input().split())
b=min(a,b,c,d)
if b>f:
    b=f+1
print(len([1 for i in range(e,b)]))




#3
p,q,r,s,a,b = input().split()
p,q,r,s,a,b = [int(p),int(q),int(r),int(s),int(a),int(b)]
i = a
answer = 0
for j in range(a,b+1):
    if (j<p and j<q and j<r and j<s):
        answer = answer+1
    else:
        j=j+1
print(answer)
