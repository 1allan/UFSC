h = int(input('H: '))
p = int(input('P: '))
f = int(input('F: '))
d = int(input('D: '))

if 0 <= h <= 15 and 0 <= p <= 15 and 0 <= f <= 15 and h != p or h != f:
	step = 1 if d == 1 else -1
	
	while True:
		f += step
		
		if f == 16:
			f = 0
			
		elif f == -1:
			f = 15

		if f == p:
			print('N')
			break
		
		elif f == h:
			print('S')
			break