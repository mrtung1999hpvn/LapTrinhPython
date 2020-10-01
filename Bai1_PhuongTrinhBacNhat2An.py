# PT Bac nhat 2 an
# a1x+b1y=c1
# a2x+b2y=c2
a1=float(input('a1 : '))
b1=float(input('b1 : '))
c1=float(input('c1 : '))

a2=float(input('a2 : '))
b2=float(input('b2 : '))
c2=float(input('c2 : '))

D = a1 * b2 - a2 * b1
Dx = c1 * b2 - c2 * b1
Dy = a1 * c2 - a2 * c1

if (D == 0):
  if (Dx + Dy == 0):
    print("He phuong trinh co vo so nghiem")
  else:
    print("He phuong trinh vo nghiem")
else: 
  x = Dx / D
  y = Dy / D
  print("He phuong trinh co nghiem (x, y) = (",x,",",y,")")
    
