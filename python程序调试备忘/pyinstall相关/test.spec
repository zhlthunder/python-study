# -*- mode: python -*-

block_cipher = None


a = Analysis(['..\\..\\..\\..\\..\\..\\..\\PycharmProjects\\python_study_1s\\python_study\\git-zhl\\python-study\\python\xb3\xcc\xd0\xf2\xb5\xf7\xca\xd4\xb1\xb8\xcd\xfc\\pyinstall\xcf\xe0\xb9\xd8\\test.py'],
             pathex=['C:\\Users\\lin\\PYCHAR~1\\PYTHON~1\\PYTHON~1\\git-zhl\\PYTHON~1\\PYTHON~3\\PYINST~1'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='test',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
