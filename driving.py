contry = input('請問你是哪個國家: ')
age = input('你輸入年齡: ')
age = int(age)
if contry == '台灣':
	if age >= 18:
		print('你可以考駕照')
	else:
		print('你還不能考駕照')
elif contry == '美國':
	if age >= 16:
		print('你可以考駕照')
	else:
		print('你還不能考駕照')
else:
	print('你只能輸入台灣/美國')