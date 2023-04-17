import colorama
from colorama import Fore
A=float(input('yi: '))
B=float(input('xi : '))
jj=1
list=[Fore.BLUE,Fore.RED,Fore.GREEN,Fore.YELLOW,Fore.WHITE,Fore.MAGENTA]
for i in range(5):

   C=float((B-4)**2+(A-4)**2-5)
   D=float(B**2+A**2-16)
   E=float(2*(B-4))
   X=float(2*(A-4))
   M=float(B-(((C*2*A)-(D*X))/((E*2*A)-(X*2*B))))
   F=float(A-(((D*E)-(C*2*B))/((E*2*A)-(X*2*B))))
   DIC={'ui':C,'vi':D,'dui/dx':E,'dvi/dx':(2*B),'dui/dy':X,'dvi/dy':(2*A),'x+1':M,'y+1':F,'ERROR X %: ':(((M-B)/M)*100),'ERROR Y %: ':(((F-A)/F)*100)}
   print('\n',list[jj]+f'{jj}- {DIC}')
   jj=jj+1
   A=F
   B=M
   #solving newton raphson non-linear method






