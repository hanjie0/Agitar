if exist d:\tmp\DO rm -Rf d:\tmp\DO
if not exist d:\tmp\DO mkdir d:\tmp\DO
if exist B: subst b: /D
subst B: %PROJECT_PATH%
dir /s /b /AD B:|findstr /V ".gradle"|findstr -E "src\\main\\java" > d:\tmp\DO\allJavaFiles.txt


set TFS=D:\01_ProgramFiles\MSVS2012\Common7\IDE\tf.exe
for /F %%i in (d:\tmp\DO\allJavaFiles.txt) do %TFS% history -collection:"https://usmlva3005vstf.ww005.siemens.net/tfs/POC1" "$/CIP/devISF03/Isf%%~pi" -noprompt -recursive -sort:descending 
rem -stopafter:1