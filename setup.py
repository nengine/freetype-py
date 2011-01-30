#!/usr/bin/env python
# -----------------------------------------------------------------------------
#  FreeType high-level python API - copyright 2011 Nicolas P. Rougier
#  Distributed under the terms of the new BSD license.
# -----------------------------------------------------------------------------
from distutils.core import setup

setup( name        = 'Freetype',
       version     = '0.1',
       description = 'Freetype python bindings',
       author      = 'Nicolas P. Rougier',
       author_email='Nicolas.Rougier@inria.fr',
       #      url='http://www.python.org/sigs/distutils-sig/',
       packages=['freetype'],
       classifiers = [
          'Development Status :: 3 - Alpha',
          'Environment :: X11 Applications',
          'Environment :: MacOS X',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License (GPL)'
          'Operating System :: MacOS',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Operating System :: Unix',
          'Programming Language :: Python',
          'Topic :: Multimedia :: Graphics',
          ],
     )
