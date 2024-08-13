@echo off
rem START or STOP Services
rem ----------------------------------
rem Check if argument is STOP or START

if not ""%1"" == ""START"" goto stop

if exist C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\hypersonic\scripts\ctl.bat (start /MIN /B C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\server\hsql-sample-database\scripts\ctl.bat START)
if exist C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\ingres\scripts\ctl.bat (start /MIN /B C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\ingres\scripts\ctl.bat START)
if exist C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\mysql\scripts\ctl.bat (start /MIN /B C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\mysql\scripts\ctl.bat START)
if exist C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\postgresql\scripts\ctl.bat (start /MIN /B C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\postgresql\scripts\ctl.bat START)
if exist C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\apache\scripts\ctl.bat (start /MIN /B C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\apache\scripts\ctl.bat START)
if exist C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\openoffice\scripts\ctl.bat (start /MIN /B C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\openoffice\scripts\ctl.bat START)
if exist C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\apache-tomcat\scripts\ctl.bat (start /MIN /B C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\apache-tomcat\scripts\ctl.bat START)
if exist C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\resin\scripts\ctl.bat (start /MIN /B C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\resin\scripts\ctl.bat START)
if exist C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\jetty\scripts\ctl.bat (start /MIN /B C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\jetty\scripts\ctl.bat START)
if exist C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\subversion\scripts\ctl.bat (start /MIN /B C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\subversion\scripts\ctl.bat START)
rem RUBY_APPLICATION_START
if exist C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\lucene\scripts\ctl.bat (start /MIN /B C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\lucene\scripts\ctl.bat START)
if exist C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\third_application\scripts\ctl.bat (start /MIN /B C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\third_application\scripts\ctl.bat START)
goto end

:stop
echo "Stopping services ..."
if exist C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\third_application\scripts\ctl.bat (start /MIN /B C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\third_application\scripts\ctl.bat STOP)
if exist C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\lucene\scripts\ctl.bat (start /MIN /B C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\lucene\scripts\ctl.bat STOP)
rem RUBY_APPLICATION_STOP
if exist C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\subversion\scripts\ctl.bat (start /MIN /B C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\subversion\scripts\ctl.bat STOP)
if exist C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\jetty\scripts\ctl.bat (start /MIN /B C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\jetty\scripts\ctl.bat STOP)
if exist C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\hypersonic\scripts\ctl.bat (start /MIN /B C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\server\hsql-sample-database\scripts\ctl.bat STOP)
if exist C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\resin\scripts\ctl.bat (start /MIN /B C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\resin\scripts\ctl.bat STOP)
if exist C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\apache-tomcat\scripts\ctl.bat (start /MIN /B /WAIT C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\apache-tomcat\scripts\ctl.bat STOP)
if exist C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\openoffice\scripts\ctl.bat (start /MIN /B C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\openoffice\scripts\ctl.bat STOP)
if exist C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\apache\scripts\ctl.bat (start /MIN /B C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\apache\scripts\ctl.bat STOP)
if exist C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\ingres\scripts\ctl.bat (start /MIN /B C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\ingres\scripts\ctl.bat STOP)
if exist C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\mysql\scripts\ctl.bat (start /MIN /B C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\mysql\scripts\ctl.bat STOP)
if exist C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\postgresql\scripts\ctl.bat (start /MIN /B C:\Users\mshiv\OneDrive\Desktop\phpmyadmin\postgresql\scripts\ctl.bat STOP)

:end

