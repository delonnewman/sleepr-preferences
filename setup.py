#!/usr/bin/env python

from distutils.core import setup

setup(name='Sleepr Preferences',
      version='1.0',
      description='Stop hacking and get some sleep',
      author='Delon Newman',
      author_email='delon.newman@gmail.com',
      url='https://github.com/delonnewman/sleepr-preferences',
      scripts=['bin/sleepr-preferences'],
      data_files=[('share/sleepr', ['share/sleepr/preferences-window.glade',
                                    'share/sleepr/sleepr-indicator-icon.png'])], 
     )
