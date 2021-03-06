#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://clepyladies.github.io/pyladies-official'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
TWITTER_USERNAME = 'clepyladies'
GITHUB_URL = 'https://www.github.com/clepyladies/pyladies-official'

MENUITEMS = [('Home', 'https://clepyladies.github.io/pyladies-official'),
            ('Upcoming Events', 'https://www.meetup.com/cle-pyladies')]
