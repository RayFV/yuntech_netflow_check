# 雲科大宿網流量監測器
--只適用於國立雲林科技大學的宿舍

```
pip install -r requirement.txt
```

open without window
```
pythonw yuntech_netflow_check.py
``` 
<p>
execute the shortcut "Close_Program" to kill python process <p>

When convert .py to .exe with pyinstaller:
```
pyinstaller -F -w yuntech_netflow_check.pyw --additional-hooks-dir=.
```
<p>
User can edit config.ini to modify default setting .
<p>
Reference:  <p>
https://brennan.io/2016/03/02/logging-in-with-requests/   <p>
http://www.cnblogs.com/ginponson/p/6079928.html   <p>
https://gist.github.com/phillipsm/0ed98b2585f0ada5a769  <p>
https://stackoverflow.com/questions/14845896/pygame-cannot-open-sound-file/41989994#41989994  <p>
https://github.com/jithurjacob/Windows-10-Toast-Notifications  
