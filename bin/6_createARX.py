import argparse
import time
import os
import re
from pathlib import Path
from pprint import pprint
import xml.etree.ElementTree
import xml.dom.minidom


def xmlAppendChild(dom, root, tag, content):
	_child = dom.createElement(tag)
	_content = dom.createTextNode(content)  
	_child.appendChild(_content)
	root.appendChild(_child)

'''
------------------------------------------------------
Main Entry
------------------------------------------------------
'''
parser = argparse.ArgumentParser(description='Create ARX file')
parser = argparse.ArgumentParser(
	formatter_class=argparse.RawDescriptionHelpFormatter,
	description=('''\
	The script is used to creat the .arx file for agitar project!
	'''))

parser.add_argument('-d', '--debug', dest="debug", action='store_true', default=False, help="parameter to enter the debug mode")
parser.add_argument('-p', '--projectfile', nargs='?', type=str, dest="projectFile", required=True, help=".arx: agitar project file")

args = parser.parse_args()
projectRoot=os.getenv('PROJECT_PATH')
if not projectRoot or projectRoot == "":
		print("Error: PROJECT_PATH is missing\n")
		exit()
else: 
	if not os.path.exists(projectRoot):
		print("Error: project root " + projectRoot +" does not exist\n")
		exit()


jars= []
jars.append(r'org/eclipse/jetty/jetty-server/7.6.21.v20160908/jetty-server-7.6.21.v20160908.jar')
jars.append(r'org/eclipse/jetty/jetty-websocket/7.6.21.v20160908/jetty-websocket-7.6.21.v20160908.jar')
jars.append(r'org/eclipse/jetty/jetty-util/7.6.21.v20160908/jetty-util-7.6.21.v20160908.jar')
jars.append(r'org/apache/thrift/libthrift/0.9.3/libthrift-0.9.3.jar')
jars.append(r'org/slf4j/slf4j-api/1.7.25/slf4j-api-1.7.25.jar')
jars.append(r'net/sf/smc/statemap/6.6.0/statemap-6.6.0.jar')
jars.append(r'javax/servlet/servlet-api/2.5/servlet-api-2.5.jar')

jarsAbs=[]
for jar in jars:
	jarsAbs.append('/'.join((projectRoot.replace("\\",'/'), r'../maven_repo', jar)))
	
jarsAbs.append(os.getenv('ANDROID_JAR').replace("\\", '/'))
jarsAbs.append(os.getenv('TOOLS_JAR').replace("\\", '/'))
jarsAbs.append('/'.join((os.getenv('JAVA_HOME').replace("\\", '/'), r'jre/lib/ext/jfxrt.jar')))	
jarsAbs.append('/'.join((os.path.dirname(args.projectFile).replace("\\", '/'), r'allClasses')))
if args.debug:
	pprint(jarsAbs)

for jar in jarsAbs:
	if not os.path.exists(jar):
		print("Error: " + jar + " does not exist\n")

libraryPath=";".join(jarsAbs) 		
impl = xml.dom.minidom.getDOMImplementation()
dom = impl.createDocument(None, 'Agitator', None)
root = dom.documentElement  
root.setAttribute('type', "j2ee")
xmlAppendChild(dom, root, 'AgitarDirectory', 'agitar')
xmlAppendChild(dom, root, 'ResultDirectory', 'agitar\.results')
xmlAppendChild(dom, root, 'ConfigDirectory', 'agitar\config')
xmlAppendChild(dom, root, 'ImportedCoverageDirectory', 'agitar\imports')
xmlAppendChild(dom, root, 'SourcePath', 'src;agitar\\test')
xmlAppendChild(dom, root, 'ClassPath', 'allClasses')
xmlAppendChild(dom, root, 'LibraryPath', libraryPath)
xmlAppendChild(dom, root, 'Version', '2')
xmlAppendChild(dom, root, 'JavaArgs', '-Xms128m -Xmx512m')
f= open(args.projectFile, 'w', encoding='utf-8')
dom.writexml(f, addindent='  ', newl='\n',encoding='utf-8')
f.close()  
