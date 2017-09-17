pip install -r requirement.txt

open without window
pythonw yuntech_netflow_check.py

execute the shortcut "Close_Program" to kill python process

When convert .py to .exe with pyinstaller:
pyinstaller -F -w yuntech_netflow_check.pyw --additional-hooks-dir=.

User can edit config.ini to modify default setting .

Reference:
https://brennan.io/2016/03/02/logging-in-with-requests/
http://www.cnblogs.com/ginponson/p/6079928.html
https://gist.github.com/phillipsm/0ed98b2585f0ada5a769
https://stackoverflow.com/questions/14845896/pygame-cannot-open-sound-file/41989994#41989994