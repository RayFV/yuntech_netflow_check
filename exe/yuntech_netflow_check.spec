# -*- mode: python -*-

block_cipher = None


a = Analysis(['yuntech_netflow_check.pyw'],
             pathex=['D:\\PyCharm\\Project\\auto_check_netflow'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['.'],
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
          name='yuntech_netflow_check',
          debug=False,
          strip=False,
          upx=True,
          console=False )
