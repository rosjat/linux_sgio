# coding: utf-8

from sys import platform
from setuptools import setup, Extension

#
# SGIO is linux specific
#
if platform[:5] == 'linux':
    linux_sgio_module = Extension('linux_sgio.linux_sgio',
                                  sources=['linux_sgio/sgiomodule.c'])

    setup(name='LINUX_SGIO',
          version='1.1',
          license='LGPLv2.1',
          author='Ronnie Sahlberg',
          author_email='ronniesahlberg@gmail.com',
          description='Module for calling Linux SG_IO devices',
          packages=['linux_sgio'],
          ext_modules=[linux_sgio_module])
