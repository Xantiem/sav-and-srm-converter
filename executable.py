import SavToSrm
import SrmToSav

import sys
import os

try:
    file = sys.argv[1]
except IndexError:
    file = input('File path from dictionary ['+os.getcwd()+']: ')

if file[-4:] == '.srm':
    print('Identified as .SRM file\nConverting')
    SrmToSav.convert(file)
    print('Converted to .SAV file')

elif file[-4:] == '.sav':
    print('Identified as .SAV file\nConverting')
    SavToSrm.convert(file)
    print('Converted to .SRM file')

else:
    print('File type not recognised')

