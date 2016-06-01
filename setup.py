#!/usr/bin/env python

'''
    This program is free software; you can redistribute it and/or modify
    it under the terms of the Revised BSD License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Revised BSD License for more details.

    Copyright 2016 Cool Dude 2k - http://idb.berlios.de/
    Copyright 2016 Game Maker 2k - http://intdb.sourceforge.net/
    Copyright 2016 Kazuki Przyborowski - https://github.com/KazukiPrzyborowski

    $FileInfo: setup.py - Last Update: 6/1/2016 Ver. 0.4.6 RC 1 - Author: cooldude2k $
'''

import re, os, sys, time, datetime, platform, pkg_resources;
from setuptools import setup, find_packages;

verinfofilename = os.path.realpath("."+os.path.sep+os.path.sep+"pymotherless.py");
''' verinfofilename = os.path.abspath("."+os.path.sep+os.path.sep+"pymotherless.py"); '''
verinfofile = open(verinfofilename, "r");
verinfodata = verinfofile.read();
verinfofile.close();
setuppy_verinfo_esc = re.escape("__version_info__ = (")+"(.*)"+re.escape(");");
setuppy_verinfo = re.findall(setuppy_verinfo_esc, verinfodata)[0];
setuppy_verinfo_exp = [vergetspt.strip().replace("\"", "") for vergetspt in setuppy_verinfo.split(',')];
pymotherless_version = str(setuppy_verinfo_exp[0])+"."+str(setuppy_verinfo_exp[1])+"."+str(setuppy_verinfo_exp[2]);
'''
setuppy_verinfo = re.findall("Ver\. ([0-9]+)\.([0-9]+)\.([0-9]+) RC ([0-9]+)", verinfodata)[0];
pymotherless_version = str(setuppy_verinfo[0])+"."+str(setuppy_verinfo[1])+"."+str(setuppy_verinfo[2]);
'''

setup(
 name = 'PyMotherless',
 version = pymotherless_version,
 author = 'Kazuki Przyborowski',
 author_email = 'kazuki.przyborowski@gmail.com',
 maintainer = 'Kazuki Przyborowski',
 maintainer_email = 'kazuki.przyborowski@gmail.com',
 description = 'Get urls of images/videos from motherless.',
 license = 'Revised BSD License',
 keywords = 'motherless pymotherless python python-motherless',
 url = 'https://github.com/GameMaker2k/PyMotherless',
 download_url = 'https://github.com/GameMaker2k/PyMotherless/archive/master.tar.gz',
 long_description = 'Get urls of images/videos from motherless.',
 platforms = 'OS Independent',
 zip_safe = True,
 py_modules = ['pymotherless'],
 classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Developers',
  'Intended Audience :: Other Audience',
  'License :: OSI Approved',
  'License :: OSI Approved :: BSD License',
  'Natural Language :: English',
  'Operating System :: MacOS',
  'Operating System :: MacOS :: MacOS X',
  'Operating System :: Microsoft',
  'Operating System :: Microsoft :: Windows',
  'Operating System :: OS/2',
  'Operating System :: OS Independent',
  'Operating System :: POSIX',
  'Operating System :: Unix',
  'Programming Language :: Python',
  'Topic :: Utilities',
  'Topic :: Software Development',
  'Topic :: Software Development :: Libraries',
  'Topic :: Software Development :: Libraries :: Python Modules',
 ],
)
