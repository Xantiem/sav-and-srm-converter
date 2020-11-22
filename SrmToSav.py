def convert(file_name):

        with open(file_name, 'rb') as srm_file:
                conv = srm_file.read()

        with open(file_name[:-3]+'sav', 'wb') as sav_file:
                sav_file.write(conv[:-16384])
