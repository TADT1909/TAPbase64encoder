from distutils.core import setup
import py2exe

setup(
	console = [{
            "script": "TAPbase64encoder.py",
            "icon_resources": [(0, "icon.ico")],
            "dest_base":"TAPbase64encoder"
            }],
	)