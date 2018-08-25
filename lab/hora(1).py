import math
s=int(input("Tempo de duração em segundos:"))
m=s//60
h=m//60
s1=s%60
m1=m%60
print("{}:{}:{}".format(h,m1,s1))