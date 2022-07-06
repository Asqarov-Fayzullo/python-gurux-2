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
oyinchi='X'
while joy>0:
	qator = int(input(oyinchi+"_qator: "))
	ustun = int(input(oyinchi+"_ustun: "))
	oyin[qator-1][ustun-1] = oyinchi
	for qator in oyin:
		for i in qator:
			print(i.center(5,' '),end='')
		print('\n')
	if oyinchi=='X':
		oyinchi='0'
	else:
		oyinchi='X'
	joy-=1
