n = int(input())
line = 0
k=n
start=1
fin = n*(n+1)+1
for i in range(n):
  print('**'*line, end='')
  line+=1
  for _ in range(k):
    print(start,end='0')
    start+=1
  
  for j in range(k,0,-1):
    print(fin-j, end='')
    if j!=1:
      print(0,end='')
  final-=k
  k-=1
  print()
