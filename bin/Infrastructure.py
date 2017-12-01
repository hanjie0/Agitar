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
if(not os.path.exists(classpathFile):
	print("classpathFile unavailable" + classpathFile )
	exit()

envVars=['JAVA_HOME', 'PROJECT_PATH', 'JACOCO_PATH', 'ANDROID_JAR', 'TOOLS_JAR','ECLIPSE_HOME', 'AGITAR_HOME'];
for var in envVars:
	value=os.getenv(var)
	if not value or value == "":
		print("Warning: " + var + " is missing\n")
	else: 
		if not os.path.exists(value):
			print("Error: the destination of environment variable " + var +" does not exist\n")
	conf['envVariables'][var]=value

writeConfig(conf, "..\ini\currentConf.ini")
	
for var in ('EXLIBRARY', 'JUNITPATH'):
	print("Checking " + var)
	value=os.getenv(var)
	if not value or value == "":
		print("Warning: " + var + " is missing\n")


	
	

	

	