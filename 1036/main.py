# -*- coding: utf-8 -*-
import math
num = input().split(" ")
puta,putb,putc = num
if float(putb)*float(putb)-4*float(puta)*float(putc) >=0:
      if 2*float(puta)>0:
            R1 = (-float(putb)+math.sqrt(float(putb)*float(putb)-4*float(puta)*float(putc)))/(2*float(puta))
            R2 = (-float(putb)-math.sqrt(float(putb)*float(putb)-4*float(puta)*float(putc)))/(2*float(puta))
            print("R1 = %.5f"%(R1))
            print("R2 = %.5f"%(R2))
      else:
            print("Impossivel calcular")
else:
      print("Impossivel calcular")