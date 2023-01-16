from module1 import*

#username=['username1','username2','username3']
#pass2=['use1','use2','use3']

pass1=password(6)
while True:
	password=input('password')
#	password2=input('password')
	a=True
	if len(password)<6:
		a=False
		break
		print('has to consost no less then 6 sym')
#	elif password!=password2:
#		print('different')
	user=username(3)
	while True:
		user_name=input('username:')
		print(f'username and paasword',user_name,password)
		loginpass=askPassword
		while True:
		  		login =    input('login')
		  		password = input('password')
		  		if login==user_name or password==password:
		  			print('success')
		  		else:
		  			print('failure')           


print('Enter or Registration!')
pass1=input('Enter/Registration: ')
if pass1==('Enter') or pass1==('Enter'):
    vh=input('Enter login and password: ')
elif pass1==('Registration') or pass1==('Registration'):
    reg=input('Creat login and password): ') 
    print(reg)
