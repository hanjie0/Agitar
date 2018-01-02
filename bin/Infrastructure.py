import argparse
import time
import os
import re
from pprint import pprint
	
'''		
------------------------------------------------------
Main Entry
------------------------------------------------------
'''
parser = argparse.ArgumentParser(description='Example for the traverse function')
parser = argparse.ArgumentParser(
	formatter_class=argparse.RawDescriptionHelpFormatter,
	description=('''\
	The script is used to check the environment for Agitar!
	'''))

parser.add_argument('-d', '--debug', dest="debug", action='store_true', default=False, help="parameter to enter the debug mode")
parser.add_argument('-c', '--classpathFile', nargs='?', type=str, dest="classpathFile", required=True, help=".classpath for eclipse")
args = parser.parse_args()

classpathFile=args.classpathFile
if(not os.path.exists(classpathFile)):
	print("classpathFile unavailable" + classpathFile )
	exit()

fileContent=""
with open(classpathFile, 'r') as f:
	fileContent=f.read()
	f.close()
fileLines=[]
fileLines=fileContent.split('\n')

srcStructure={'xx':'yy'}
for i in fileLines:
	if i.strip()!='':
		t= i.replace(r'com.siemens.hc.poc.isf.', '').split('.')
		if srcStructure.has_key('.'.join(t[0:-1])):		
			pass
			#srcStructure['.'.join(t[0:-1])].append(t[-1])
		else:
			pass
			#srcStructure['.'.join(t[0:-1])].append(t[-1])=[]
pprint(packageList)	