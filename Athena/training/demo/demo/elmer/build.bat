@echo off
setlocal
REM
REM This batch file builds the "vette" elmer example
REM
REM Type: "build" to build,
REM Type: "build clean" to remove generated files
REM


REM
REM Set paths and commands for use in this batch file
REM
set ERRORLEVEL=
set PYTHON_INCDIR=c:\python23\include
set PYTHON_LIBDIR=c:\python23\libs
set ELMER_CMD=elmer -int vette.elm
set GCC_CMD=gcc -I. -I%PYTHON_INCDIR% -o vette vette_main.c vette.c -L%PYTHON_LIBDIR% -lelmer -lpython23
set DEL_CMD=del vette.c vette.h vette.exe *.pyc


REM
REM Jump to clean if clean given
REM
if "%1"=="clean" goto clean


REM
REM Run elmer, check for success, then gcc if elmer successful
REM
echo RUNNING ELMER...
echo %ELMER_CMD%
call %ELMER_CMD%
if %ERRORLEVEL% NEQ 0 goto done

echo.

echo CALLING GCC...
echo %GCC_CMD%
%GCC_CMD%
goto done


REM
REM remove all generated files
REM
:clean
echo %DEL_CMD%
%DEL_CMD%

:done
endlocal
