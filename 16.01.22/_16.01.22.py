from module1 import*

u=['user1','user2','user3']
#passwords=['user11','user22','user33']

pass1=password(6)
while True:
	m=random.choice(u)
	password=input('password')
	if password==password and password==password and password==password:
		print('succses')
	else:
		print('failure')
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
		  			message='succses'
		  		else:
		  			message='failure'
		  		print(message)
		  		break


print('Enter or Registration!')
pass1=input('Enter/Registration: ')
if pass1==('Enter') or pass1==('Enter'):
    vh=input('Enter login and password: ')
elif pass1==('Registration') or pass1==('Registration'):
    reg=input('Creat login and password): ') 
    print(reg)
