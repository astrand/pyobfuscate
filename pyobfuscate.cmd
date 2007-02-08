@echo off
rem
rem Windows wrapper for Python scripts. Allows you to invoke a Python
rem script as "myscript" instead of "myscript.py". 
rem Author: Peter Astrand <astrand@cendio.se>
rem
%~dpn0.py %*
