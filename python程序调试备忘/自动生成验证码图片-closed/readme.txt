�ο�blog:
http://www.cnblogs.com/alex3714/articles/6662365.html

����
���������֤��


����1�� from PIL import Image,ImageDraw,ImageFont,ImageFilter
PIL ģ�鰲װ

�������£�
�� http://www.pythonware.com/products/pil/    ����Դ����� Python Imaging Library 1.1.7 Source Kit �� Imaging-1.1.7.tar.gz
��ͨ��Դ��ķ�ʽ���а�װ����python setup.py install��
remark: Դ��İ�װ��ʽ�����������е�ƽ̨ ��linux or windows,  python ��ͬ�İ汾��

��װ��ɺ�ȷ�Ͽ��Ե��룺
[root@localhost module_tiaoshi]# python
Python 2.6.6 (r266:84292, Sep  4 2013, 07:46:00) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-3)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from PIL import Image
>>> 


����2��linux ϵͳ������ⴴ����أ�

��linux��ִ�����²�����  
mkdir  /usr/share/fonts/arial
��windowsϵͳĿǰ��c:/windows/fonts�¿���arial��ֱ���ø�����arial�ļ��е������ļ��ϴ��� /usr/share/fonts/arial/�¡�
ִ�У� mkfontscale ���� ����������⣬���Բο���https://www.cnblogs.com/sqmlinux/archive/2012/08/20/2646993.html��
ֱ���ڴ��������ã�
font_path = '/usr/share/fonts/arial/arial.ttf' ���ɣ�

ֱ��ִ�нű����ɣ�
���ɵ�ͼƬ�� ������ɵ�ͼƬ���/tmp/test.png �¡�