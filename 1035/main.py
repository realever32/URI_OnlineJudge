# -*- coding: utf-8 -*-
num = input().split(" ")
a,b,c,d = num
if int(b)>int(c) and int(d)>int(a):
    if int(c+d) > int(a+b):
        if int(c)>0 and int(d)>0:
            if int(a)%2 == 0:
                print("Valores aceitos")
            else:
                print("Valores nao aceitos")
        else:
            print("Valores nao aceitos")
    else:
        print("Valores nao aceitos")
else:
    print("Valores nao aceitos")
