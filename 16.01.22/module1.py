from math import*
import random
from random import choice
from re import*
import string
def password(a:int):
    """enter a password 
    """

    pass1= ""
    for i in range(a):
        t=choice(string.ascii_letters) #AA...zz
        num=choice([1,2,3,4,5,6,7,8,9])
        
        t_num=[t,str(num)]
        pass1+=choice(t_num)
    return pass1



username=['username1','username2','username3']
pass2=['use1','use2','use3']
def username(b:str):
    user_name=" "
    for i in range(b):
        user_name=input('username:')
        if user_name==username:
            print('OKI')




    #str0=".,:;!_*-+()/#¤%&"
    #str1 = '0123456789'
    #str2 = 'qwertyuiopasdfghjklzxcvbnm'
    #str3 = str2.upper()
    #print(str3) # 'QWERTYUIOPASDFGHJKLZXCVBNM'
    #str4 = str0+str1+str2+str3
    #print(str4)
    #ls = list(str4)
    #print(ls)
    #random.shuffle(ls)
    #print(ls)
    ## Извлекаем из списка 12 произвольных значений
    #psword = '12345'.join([random.choice(ls) for x in range(12)])
    ## Пароль готов
    #print(psword)
  # Option 1
