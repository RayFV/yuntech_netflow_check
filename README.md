# 雲科大宿網流量監測器
--只適用於國立雲林科技大學的宿舍

# 2017/09/18下午17:00 無法使用
由於宿網增加了驗證，所以這程式沒辦法使用了 <br>
作者很懶惰，就不更新了<br>
有需求和能力的人可以自己利用這殘廢的程式分支開發出自己需要的<br>

## Requirements
```
pip install -r requirement.txt
```
## Execute
Open without window
```
pythonw yuntech_netflow_check.py
``` 
## Close
Double click the shortcut "Close_Program" to kill python process <p>

## Convert to .exe
When convert .py to .exe with pyinstaller:
```
pyinstaller -F -w yuntech_netflow_check.pyw --additional-hooks-dir=.
```

## Setting
User can edit config.ini to modify default setting .

## Reference: 
http://www.cnblogs.com/ginponson/p/6079928.html   <br>
https://gist.github.com/phillipsm/0ed98b2585f0ada5a769  <br>
https://stackoverflow.com/questions/14845896/pygame-cannot-open-sound-file/41989994#41989994 <br>
https://github.com/jithurjacob/Windows-10-Toast-Notifications  
