# -*- coding: utf-8 -*-
name = "pyfory"
version = "999.0-py3.12"
description = "PyFury (pyfory) - High-performance serialization library"
authors = ["PyFury Team", "Lugwit Team"]

requires = ["python-3.12+<3.13"]

build_command = False
cachable = True
relocatable = True

def commands():
    import platform
    if platform.system() == "Windows":
        env.PYFORY_ROOT = "{root}\\.pyfory"
        env.PYTHONPATH.prepend("{root}\\.pyfory")
    else:
        env.PYFORY_ROOT = "{root}/.pyfory"
        env.PYTHONPATH.prepend("{root}/.pyfory")
