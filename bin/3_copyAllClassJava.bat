echo off
if exist d:\tmp\agitarDO rm -Rf d:\tmp\agitarDO
if not exist d:\tmp\agitarDO mkdir d:\tmp\agitarDO
if exist B: subst b: /D
subst B: %PROJECT_PATH%
dir /s /b /AD B:|findstr /V ".gradle"|findstr -E "src\\main\\java" > d:\tmp\agitarDO\allJavaFiles.txt
dir /s /b /AD B:|findstr /V ".gradle"|findstr -E "build\\generated\\source\\thrift" >> d:\tmp\agitarDO\allJavaFiles.txt
FOR /F %%i IN (d:\tmp\agitarDO\allJavaFiles.txt) do xcopy /Y /E /D /I %%i d:\tmp\agitarDO\allJavaFiles\


dir /s /b /AD B:|findstr -E "build\\intermediates\\classes\\debug" > d:\tmp\agitarDO\allClasses.txt
FOR /F %%i IN (d:\tmp\agitarDO\allClasses.txt) do xcopy /Y /E /D /I %%i d:\tmp\agitarDO\allClasses\

rem ROBOCOPY %PROJECT_PATH% d:\tmp\agitarDO\classes\ *.class /s /xd test androidTest .gradle .idea agitar
REM walk the folders, find a folder that named with (com, org, net), add it to 'list'
rem dir d:\tmp\agitarDO\classes /s /b | findstr -e \\com > d:\tmp\agitarDO\allClassDir.txt
rem dir d:\tmp\agitarDO\classes /s /b | findstr -e \\org >> d:\tmp\agitarDO\allClassDir.txt
REM move the file listed in 'list' to src folder so it will mimic java src directory
rem FOR /F %%i IN (d:\tmp\agitarDO\allClassDir.txt) do robocopy %%i\.. d:\tmp\agitarDO\allClasses\ /S /move 
