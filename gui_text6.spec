# -*- mode: python -*-
a = Analysis(['gui_text6.py'],
             pathex=['/Users/zhengyangqiao/PycharmProjects/coin_toss_gui'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='gui_text6',
          debug=False,
          strip=None,
          upx=True,
          console=False )
app = BUNDLE(exe,
             name='gui_text6.app',
             icon=None)
