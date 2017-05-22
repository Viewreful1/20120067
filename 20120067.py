n,m,v=map(int,input().split());o=[[]for _ in range(n+1)];exec('a,b=map(int,input().split());o[a]+=[b];o[b]+=[a];'*m);o=list(map(sorted,o));s=[]
def D(n):
 global s
 if n in s:return
 s+=[n]
 for i in o[n]:D(i)
D(v);print(' '.join(map(str,s)));s=[v];q=[v]
while q:
 for i in o[q.pop(0)]:
  if i not in s:s+=[i];q+=[i]
print(' '.join(map(str,s)))