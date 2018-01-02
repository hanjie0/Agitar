echo off
if exist d:\tmp\agitarDO rm -Rf d:\tmp\agitarDO
if not exist d:\tmp\agitarDO mkdir d:\tmp\agitarDO
if exist B: subst b: /D
subst B: %PROJECT_PATH%
dir /s /b /AD B:|findstr /V ".gradle"|findstr -E "src\\main\\java" > d:\tmp\agitarDO\allJavaFiles.txt
rem dir /s /b /AD B:|findstr /V ".gradle"|findstr -E "build\\generated\\source\\thrift" >> d:\tmp\agitarDO\allJavaFiles.txt
FOR /F %%i IN (d:\tmp\agitarDO\allJavaFiles.txt) do xcopy /Y /E /D /I %%i d:\tmp\agitarDO\allJavaFiles\


dir /s /b /AD B:|findstr -E "build\\intermediates\\classes\\debug" > d:\tmp\agitarDO\allClasses.txt
FOR /F %%i IN (d:\tmp\agitarDO\allClasses.txt) do xcopy /Y /E /D /I %%i d:\tmp\agitarDO\allClasses\

