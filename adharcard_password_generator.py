# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 00:30:28 2019
@author: ZICO /TANMAY
"""

alpha= ['A','B','D','E', 'F', 'G' ,'H' ,'I' ,'J' ,'K' ,'L' ,'M', 'N', 'O' ,'P' ,'Q' ,'R' ,'S' ,'T' ,'U' ,'V' ,'W' ,'X' ,'Y' ,'Z',' ']

# lists
chr_pass=[]
password=[]
for i in alpha:
    if(i==' '):
        break
    l_2char=''
    for j in alpha:
        l_2char=i+j
        for k in alpha:
            l_3char=l_2char+k
            for l in alpha:
                l_4char=l_3char+l
                chr_pass.append( l_4char)
for i in range (1900,2020):                
    for j in chr_pass:
        password.append(j+str(i))
