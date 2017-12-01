import argparse
import time
import os
import re
from pathlib import Path
from pprint import pprint
import xml.etree.ElementTree
import xml.dom.minidom

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
	'''))

parser.add_argument('-d', '--debug', dest="debug", action='store_true', default=False, help="parameter to enter the debug mode")
parser.add_argument('-c', '--classpath', nargs='?', type=str, dest="classpathFile", required=True, help=".classpath for eclipse")

args = parser.parse_args()
projectRoot=os.getenv('PROJECT_PATH')
if not projectRoot or projectRoot == "":
		print("Error: PROJECT_PATH is missing\n")
		
else: 
	if not os.path.exists(projectRoot):
		print("Error: project root " + projectRoot +" does not exist\n")
		


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
jarsAbs.append('/'.join((os.path.dirname(args.classpathFile).replace("\\", '/'), r'allClasses')))

if args.debug:
	pprint(jarsAbs)

for jar in jarsAbs:
	if not os.path.exists(jar):
		print("Error: " + jar + " does not exist\n")
src=['src', 'agitar/test']
output=['bin']
varPath=['AGITATOR_LIB','JUNIT_HOME/junit.jar', 'AGITAR_MOCK_OBJECTS','AGITAR_TEST_LIB']
con=[r'org.eclipse.jdt.launching.JRE_CONTAINER/org.eclipse.jdt.internal.debug.ui.launcher.StandardVMType/JavaSE-1.8']

impl = xml.dom.minidom.getDOMImplementation()
dom = impl.createDocument(None, 'classpath', None)
root = dom.documentElement  

for jar in jarsAbs:
	classpathEntry = dom.createElement('classpathentry')
	classpathEntry.setAttribute('kind', 'lib')
	classpathEntry.setAttribute('path', jar)
	root.appendChild(classpathEntry)
for s in src:
	classpathEntry = dom.createElement('classpathentry')
	classpathEntry.setAttribute('kind', 'src')
	classpathEntry.setAttribute('path', s)
	root.appendChild(classpathEntry)
for o in output:
	classpathEntry = dom.createElement('classpathentry')
	classpathEntry.setAttribute('kind', 'output')
	classpathEntry.setAttribute('path', o)
	root.appendChild(classpathEntry)
for v in varPath:
	classpathEntry = dom.createElement('classpathentry')
	classpathEntry.setAttribute('kind', 'var')
	classpathEntry.setAttribute('path', v)
	root.appendChild(classpathEntry)
for c in con:
	classpathEntry = dom.createElement('classpathentry')
	classpathEntry.setAttribute('kind', 'con')
	classpathEntry.setAttribute('path', c)
	root.appendChild(classpathEntry)
	
f= open(args.classpathFile, 'w', encoding='utf-8')
dom.writexml(f, addindent='  ', newl='\n',encoding='utf-8')
f.close()  
		
'''		
classpathFile = xml.etree.ElementTree.parse('.classpath')
root = classpathFile.getroot()
for c in root:
	print(c.tag)
	print(c.attrib)
	exit()


for c in jarsAbs:
	newLib = xml.etree.ElementTree.SubElement(classpathFile.getroot(), 'classpathentry')
	newLib.text = ''
	newLib.attrib['kind'] = 'lib' 
	newLib.attrib['path'] = c	
	classpathFile.write('.classpath')
		
		
	
defaultPath=[]		
classpathFile = xml.etree.ElementTree.parse('.classpath')
root = classpathFile.getroot()
classpathEntrys=root.findall('classpathentry')
for c in classpathEntrys:
	defaultPath.append(c.attrib['path'])
if args.debug:
	pprint(defaultPath)	
	
	
jarTobeAdded=[]
for jar in jarsAbs:
	if jar not in defaultPath:
		jarTobeAdded.append(jar)
	else:
		print(jar)
		
		
pprint(jarTobeAdded)		
	

newLib = xml.etree.ElementTree.SubElement(classpathFile.getroot(), 'classpathentry')
new_tag.text = ''
new_tag.attrib['kind'] = '1' # must be str; cannot be an int
new_tag.attrib['path'] = 'abc'	
classpathFile.write('.classpath')
'''