# -*- coding: cp1250 -*-

f=open('D://programy/pyton/AH2.txt','r')
n=f.readlines()[0]
N=int(n)
f=open('D://programy/pyton/AH2.txt','r')
m=f.readlines()[1]
M=int(m)
f=open('D://programy/pyton/AH2.txt','r')
a=f.readlines()[2]
f=open('D://programy/pyton/AH2.txt','r')
k=f.readlines()[3]
a1=a.split()
k1=k.split()
A=[]
K=[]
for i in range(len(a1)):
    A.append(int(a1[i]))
for j in range(len(k1)):
    K.append(int(k1[j]))


#print 'N=',N,'\n','M=',M,'\n','A=',A,'\n','K=',K,'\n'

#Do tego momentu mam pobrane macierze z pliku(bo to mog� by� du�e wektory)
#oraz ograniczniki oraz mo�na je �adnie wypisa�. Pierwsza linijka to sprucie si�
#Pythona, �e nie da�em �adnych zmiennych liczbowych tylko wszystko jest z pliku,
#ale bangla jak powinno.


