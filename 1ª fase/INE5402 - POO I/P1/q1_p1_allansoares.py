h = int(input('H: '))
p = int(input('P: '))
f = int(input('f: '))
d = int(input('D: '))

if 0 <= h <= 15 and 0 <= p <= 15 and 0 <= f <= 15 and h != p or h != f:
	if d == 1:
		while f != p or f != h:
			f += 1
			if f == 16:
				f = 0

			if f == p:
				print('N')
				break
			elif f == h:
				print('S')
				break
	else:
		while f != p or f != h:
			f -= 1

			if f == -1:
				f = 15

			if f == p:
				print('N')
				break
			elif f == h:
				print('S')
				break