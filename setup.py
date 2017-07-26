from distutils.core import setup
import py2exe, sys, os
sys.argv.append('py2exe')
setup(
	name='TAPbase64encoder',
	description='Encode Image, Video into Base64',
	author='Thien An Dang Thanh',
	author_email='thienandangthanh@gmail.com',
	url="http://github.com/tadt1909/TAPbase64encoder",
	version='1.3.1',
    license="MIT",
	console = [{
            "script": "TAPbase64encoder.py",
            "icon_resources": [(0, "icon.ico")],
            "dest_base":"TAPbase64encoder"
            }],
	options = {'py2exe': {'bundle_files': 1, 'compressed': True, "includes":["sip"],  'dist_dir': "export"}},
	zipfile = None,

	)