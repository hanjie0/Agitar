import argparse
import time
import os
import re
from pprint import pprint
'''
travers
'''
def travers(_rootDir):
	_fileList=[]
	_dirList=[]
	for _root, _dirs, _files in os.walk(_rootDir):
		for _dir in _dirs:
			_dirList.append(os.path.join(_root, _dir))  
		for _file in _files:  
			_fileList.append(os.path.join(_root, _file))
			
	return _fileList, _dirList
	

'''
------------------------------------------------------
Main Entry
------------------------------------------------------
'''
parser = argparse.ArgumentParser(description='Example for the traverse function')
parser = argparse.ArgumentParser(
	formatter_class=argparse.RawDescriptionHelpFormatter,
	description=('''\
	The script is used to !
	-----------------------------------------------
	The following parameters are MANDATORY: 
	
	1.The root directory for the searching action

	-----------------------------------------------
	'''))

parser.add_argument('-d', '--debug', dest="debug", action='store_true', default=False, help="parameter to enter the debug mode")
parser.add_argument('-r', '--rootDir', nargs='?', type=str, dest="rootDir", required=True, help="The root directory for the searching action")

args = parser.parse_args()

rootDir=args.rootDir
if not os.path.exists(rootDir):
	print ("Invalid root directory for searching, exiting...")
	exit(1)
else: 
	print ("Start searching from " + rootDir + "\n\n")
fileList, dirList = travers(rootDir)


t1=[]
t2=[]
classList=[]
for file in fileList:
	t1.append(file.replace(rootDir, '').replace('\\', '.'))
	
p0 = re.compile(".*\.src\.main\.java\.(com\.siemens.*)\.java") 
for file in t1:
	m=p0.match(file)
	if m:
		t2.append(m.group(1))
		
p1=re.compile("I[A-Z].*")
p2=re.compile("unittest.*")
for file in t2:
	if p1.match(file.split('.')[-1]) or p2.match(file.split('.')[5]):
		pass
	else:
		classList.append(file)

		
with open("classlist.txt", 'wt', encoding='utf-8') as w:
	for f in classList:
		w.write(f+"\n")
		w.write(f+"AgitarTest"+"\n")
