http://www.cnblogs.com/yufeihlf/p/5945102.html

Robot Framework�Ļ����
1.Robot framework�İ�װ
���ã�web�Զ������Կ�ܡ�
RF����ǻ���python �ģ�����һ��Ҫ��python���������Ͽ������в��ҡ�
���ص�ַ��https://pypi.python.org/pypi/robotframework/2.8.5#downloads
robotframework-2.8.5.win-amd64.exe
ֱ��˫����һ�����ɡ�
 
2.wxPython �İ�װ
���ã�Wxpython ��python �ǳ�������һ��GUI�⣬��ΪRIDE �ǻ�������⿪���ģ�����������밲װ��
���ص�ַ��http://sourceforge.net/projects/wxpython/files/wxPython/2.8.12.1/
wxPython2.8-win64-unicode-2.8.12.1-py27.exe
ֱ��˫����һ�����ɡ�
 
3.Robot framework-ride
���ã�RIDE����һ��ͼ�ν�������ڴ�������֯�����в��Ե������
���ص�ַ��https://pypi.python.org/pypi/robotframework-ride
robotframework-ride-1.5.1.tar.gz
�����ѹ��C�̣��Ժ�Ļ���ý���Ŀ¼���ö�python��Ҫ��ѹ��C:\Python27\Scripts�Ͽ��Բ鿴����
cd C:\robotframework-ride-1.5.1
python  setup.py install
 
4.Robot framework-selenium2library
���ã�RF-seleniumlibrary ���Կ���RF���selenium �⣬selenium ��webdriver��������Ϊ��һ�׻���web�Ĺ淶��API�������ԣ�RF ��appium �Ȳ��Թ��߶����Ի�������API����ҳ��Ķ�λ�������
���ص�ַ��https://github.com/robotframework/Selenium2Library#readme
Selenium2Library-master.zip
�����ѹ��C�̣��Ժ�Ļ���ý���Ŀ¼���ö�python�����Ҫ��ѹ��C:\Python27\Scripts�Ͽ��Բ鿴����
cd C:\Selenium2Library-master
python setup.py install
 
���ϰ�װ���֮���������RIDE��
1.ͨ���ļ�������˫��[dirPath]\python\Lib\site-packages\robotide�µ�__init__.py�ļ���
2.ͨ����������������->ride.py�س�/ȷ�ϣ�
cd C:\Python27\Scripts\
python ride.py
3.��C:\Python27\Scripts\ride.py������ݼ���
��ride.py�ļ�֮����python��ʽ�򿪣�����������У�start������ť��
 
�鿴pybot�汾
cd C:\Python27\Scripts
pybot --version