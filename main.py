oyin = [
	['_','_','_'],
	['_','_','_'],
	['_','_','_']
]
for qator in oyin:
	for i in qator:
		print(i.center(5,' '),end='')
	print('\n')
joy = 9
while joy>=1:
	qator = int(input('X-Qator: '))
	ustun = int(input('X-Ustun: '))
	oyin[qator-1][ustun-1] = 'X'
	joy-=1
	for qator in oyin:
		for i in qator:
			print(i.center(5,' '),end='')
		print('\n')

	qator = int(input('0-Qator: '))
	ustun = int(input('0-Ustun: '))
	oyin[qator-1][ustun-1] = '0'
	joy-=1
	for qator in oyin:
		for i in qator:
			print(i.center(5,' '),end='')
		print('\n')
print("O'yin tugadi")