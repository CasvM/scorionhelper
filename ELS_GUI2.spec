# -*- mode: python -*-

block_cipher = None


a = Analysis(["ELS_GUI.py"],
             pathex=["H:\\My Documents\\Python\\Files"],
             binaries=[("chromedriver.exe","."), ("elslogo.ico", ".")],
             datas=[("manual.docx", ".")],
             hiddenimports=["tkinter"],
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
          exclude_binaries=True,
          name='Scorionhelper',
          debug=True,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='Scorionhelper')
