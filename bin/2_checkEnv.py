import argparse
import time
import os
import re
from pprint import pprint
from configparser import RawConfigParser
CONFIG_EXAMPLE = r'''
[global]
	encoding = utf-8
	debugMode = true	
	basePath = .
[envVariables]
	JAVA_HOME="" 
	PROJECT_PATH=""
	JACOCO_PATH=""
	ANDROID_JAR=""
	TOOLS_JAR="'
	JUNITPATH=""
'''
def writeTemplateFile(config, filename):
	'''Create a template configuration file.'''
	with open(filename, 'wt', encoding='utf-8') as configFile:
		configFile.write(config)
		
def readConfig(filename):
	'''
	Read the configuration file and return a pythonic configuration dict.
	'''
	confParser = RawConfigParser(defaults={})
	parsedFiles = confParser.read(filename)
	if not parsedFiles:
		msg = "Configuration file {} could not be read.".format(filename)
		raise Exception(msg)
	conf = {
			'global':{},	
			'envVariables': {},
    		}
	if confParser.has_section('global'):
		conf['global']['encoding'] = confParser.get('global', 'encoding')
	if confParser.has_section('envVariables'):
		conf['envVariables']['JAVA_HOME'] = confParser.get('envVariables', 'JAVA_HOME')
		conf['envVariables']['PROJECT_PATH'] = confParser.get('envVariables','PROJECT_PATH')
		conf['envVariables']['ANDROID_JAR'] = confParser.get('envVariables','ANDROID_JAR')
		conf['envVariables']['JACOCO_PATH'] = confParser.get('envVariables','JACOCO_PATH')
		conf['envVariables']['JUNITPATH'] = confParser.get('envVariables','JUNITPATH')
		conf['envVariables']['TOOLS_JAR'] = confParser.get('envVariables','TOOLS_JAR')
	return conf		

def writeConfig(conf, fileName):
	'''
	Write the configuration file.
	'''
	confParser = RawConfigParser()
	for k1, v1 in conf.items():
		if confParser.has_section(k1):
			pass
		else:
			confParser.add_section(k1)
		if len(v1) != 0:
			for k2, v2 in v1.items():
				confParser.set(k1, k2, conf[k1][k2])

	pprint(conf)
	print("Update config to: " + fileName)
	print(confParser.options('envVariables'))
	with open(fileName, 'wt', encoding='utf-8') as configFile:
		confParser.write(configFile)
		
	
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
args = parser.parse_args()

if(not os.path.exists("../ini")):
	os.makedirs("..\ini")
if(not os.path.exists("..\ini\defaultConf.ini")):
	writeTemplateFile(CONFIG_EXAMPLE, "..\ini\defaultConf.ini")
	
conf=readConfig("..\ini\defaultConf.ini")


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


	
	

	

	