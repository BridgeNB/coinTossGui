# -*- mode: python -*-
a = Analysis(['gui_text6.py'],
             pathex=['/Users/zhengyangqiao/PycharmProjects/coin_toss_gui'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='gui_text6',
          debug=False,
          strip=None,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='gui_text6')
app = BUNDLE(coll,
             name='gui_text6.app',
             icon=None)
