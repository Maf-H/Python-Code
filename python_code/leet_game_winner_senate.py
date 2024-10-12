def winer(senator):
	qr = []
	qd = []
	length = len(senator)
	for i in range(len(senator)):
		if senator[i] == 'D':
			qd.append(i)
		else:
			qr.append(i)
	print(qr, qd)
	
	while qr and qd:
		pr, pd = qr.pop(0), qd.pop(0)
		if pr < pd:
			qr.append(length + pr)
		else:
			qd.append(length + pr)
			
	if qr:
		return 'Raymond'
	else:
		return 'Dire'
		
print(winer('DDRRR'))