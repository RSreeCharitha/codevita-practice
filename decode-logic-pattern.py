##Decode the logic and print the pattern that corresponds to the given input
#SI 1 - 3
#SO 1 
# 10203010011012
# **4050809
# ****607

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
  fin-=k
  k-=1
  print()
