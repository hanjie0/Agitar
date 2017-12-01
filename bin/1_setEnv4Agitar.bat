@echo off

IF %COMPUTERNAME% == AAECNPEK07280L ( 
		Goto AAECNPEK07280L
) ELSE (
		Goto AAECNBJ005785D
)
 
:AAECNPEK07280L
echo "setting for AAECNPEK07280L......"
@echo on

SET PROJECT_PATH=D:\01_ProgramFiles\Jenkins2.67\workspace\CIP_SrcUpdate\Isf
SET TOOLS_JAR=D:\01_ProgramFiles\Java\jdk1.8.0_131\lib\tools.jar
SET JACOCO_PATH=D:\01_ProgramFiles\jacoco
SET ANDROID_JAR=C:\Users\z00103yd\AppData\Local\Android\Sdk\platforms\android-21\android.jar
SET RANDOOP_JAR=D:\01_ProgramFiles\randoop-3.1.5\randoop-all-3.1.5.jar
SET JUNITPATH=%PROJECT_PATH%\..\maven_repo\junit\junit\4.12\junit-4.12.jar;%PROJECT_PATH%\..\maven_repo\org\hamcrest\hamcrest-core\1.3\hamcrest-core-1.3.jar
SET EXLIBRARY=%PROJECT_PATH%\..\maven_repo\org\eclipse\jetty\jetty-server\7.6.21.v20160908\jetty-server-7.6.21.v20160908.jar;%PROJECT_PATH%\..\maven_repo\org\eclipse\jetty\jetty-websocket\7.6.21.v20160908\jetty-websocket-7.6.21.v20160908.jar;%PROJECT_PATH%\..\maven_repo\org\eclipse\jetty\orbit\javax.servlet\2.5.0.v201103041518\javax.servlet-2.5.0.v201103041518.jar;%PROJECT_PATH%\..\maven_repo\net\sf\smc\statemap\6.6.0\statemap-6.6.0.jar;%PROJECT_PATH%\..\maven_repo\org\eclipse\jetty\jetty-util\7.6.21.v20160908\jetty-util-7.6.21.v20160908.jar;%PROJECT_PATH%\..\maven_repo\org\eclipse\jetty\orbit\javax.servlet\2.5.0.v201103041518\javax.servlet-2.5.0.v201103041518.jar
set ECLIPSE_HOME=D:\01_ProgramFiles\agitarOne\platforms\mswin\x86_64\eclipse
set AGITAR_HOME=D:\01_ProgramFiles\agitarOne\webapps\agitar-server\eclipse\plugins\com.agitar.eclipse.cmdline_6.2.0.000001\config
Goto END
 
 :AAECNBJ005785D
echo "setting for AAECNBJ005785D......"
echo on
SET PROJECT_PATH=D:\02_Workspace\jiehan_CIP\devISF03\Isf
SET TOOLS_JAR=D:\02_ProgramFiles\Java\JDK1.8.131\lib\tools.jar
SET JACOCO_PATH=D:\02_ProgramFiles\jacoco
SET ANDROID_JAR=C:\Users\z00103yd\AppData\Local\Android\Sdk\platforms\android-21\android.jar
SET RANDOOP_JAR=D:\02_ProgramFiles\randoop-3.1.5\randoop-all-3.1.5.jar
SET JUNITPATH=%PROJECT_PATH%\..\maven_repo\junit\junit\4.12\junit-4.12.jar;%PROJECT_PATH%\..\maven_repo\org\hamcrest\hamcrest-core\1.3\hamcrest-core-1.3.jar
SET EXLIBRARY=%PROJECT_PATH%\..\maven_repo\org\eclipse\jetty\jetty-server\7.6.21.v20160908\jetty-server-7.6.21.v20160908.jar;%PROJECT_PATH%\..\maven_repo\org\eclipse\jetty\jetty-websocket\7.6.21.v20160908\jetty-websocket-7.6.21.v20160908.jar;%PROJECT_PATH%\..\maven_repo\org\eclipse\jetty\orbit\javax.servlet\2.5.0.v201103041518\javax.servlet-2.5.0.v201103041518.jar;%PROJECT_PATH%\..\maven_repo\net\sf\smc\statemap\6.6.0\statemap-6.6.0.jar;%PROJECT_PATH%\..\maven_repo\org\eclipse\jetty\jetty-util\7.6.21.v20160908\jetty-util-7.6.21.v20160908.jar;%PROJECT_PATH%\..\maven_repo\org\eclipse\jetty\orbit\javax.servlet\2.5.0.v201103041518\javax.servlet-2.5.0.v201103041518.jar
Goto END

:END

