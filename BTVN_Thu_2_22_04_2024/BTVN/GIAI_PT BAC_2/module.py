#bài xaay dựng các module các viến sau

#def bac_nhat(a,b):
 #   if a==0:
  #      if b==0:
   #         print("phương trình đã cho có vô số nghiệm :")
    #    else:
     #       print("phuong trình đã cho có vô nghiệm ")
    #else:
     # x=-b/a
    #return x
from math import sqrt
def bac_nhat_2_an(a,b,c):
    delta=b*b-4*a*c
    if delta<0:
        return "phương trình đã cho vô nghiệm !"
    elif delta==0:
        print("phương trình đã cho có nghiem kép")
        x=-b/2*a
        return x
    else:
     x1 = (-b + sqrt) / 2 * a
     x2 = (-b - sqrt) / 2 * a
     return x1, x2

