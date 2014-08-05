 # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
for i in range(2,1000):
 flag=0
 for j in range (2,i):
         if (i%j == 0):
          flag=1;
 if (flag == 0):
         print i
         
         
         # istructor code
         """
         minIdx=1;
         maxIdx=1000;
         for i in range(minIdx,maxIdx)
             isprime=True;
             for j in range (2,i) :
             if (i % j == 0):
             isprime = Frue;
             break
                 
             

             if (isprime ==False):
                 print i
             
             