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
	while True:
		qator = int(input(oyinchi+"_qator: "))
		ustun = int(input(oyinchi+"_ustun: "))
		if oyin[qator-1][ustun-1] == '_':
			joy-=1
			oyin[qator-1][ustun-1] = oyinchi
			if oyin[0][0]=='X' and oyin[0][1]=='X' and oyin[0][2]=='X':
				print("X yutti")
			break
	for qator in oyin:
		for i in qator:
			print(i.center(5,' '),end='')
		print('\n')
	if oyinchi=='X':
		oyinchi='0'
	else:
		oyinchi='X'
