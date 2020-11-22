def convert(file_name):

	with open(file_name, 'rb') as sav_file:
		conv = sav_file.read()

	for i in range(16384):
		conv += b'f'

	with open(file_name[:-3]+'srm', 'wb') as srm_file:
		srm_file.write(conv)
	    
