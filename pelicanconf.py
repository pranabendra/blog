#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Pranabendra Prasad Chandra'
SITENAME = 'Blog'
SITEURL = 'https://pranabendra.github.io/blog'

PATH = 'content'

USE_FOLDER_AS_CATEGORY = True
STATIC_PATH = ['images']

TIMEZONE = 'Asia/Calcutta'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (
#         ('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('Jadavpur University', 'http://www.jaduniv.edu.in/'),
#         ('My Website', 'https://pranabendra.github.io/')
#     )

# Social widget
SOCIAL = (('GitHub', 'https://github.com/pranabendra'),
          ('LinkedIn', 'https://in.linkedin.com/in/pranabendra-prasad-chandra-20794a12b'),
          ('Instagram', 'https://www.instagram.com/pranab_ppc'),
          ('500px', 'https://500px.com/pranabendrachandra'),
          ('Facebook', 'https://www.facebook.com/ppc.pranab'),
          ('Google Scholar', 'https://scholar.google.com/citations?user=fVbjLj4AAAAJ&hl=en'),
          ('YouTube', 'https://www.youtube.com/channel/UC3a-ZFiZ6K_cuJUn7Sb7vfQ'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Custom theme
THEME = 'theme'

# Website details
WEBSITE_URL = 'https://pranabendra.github.io/'
WEBSITE_TEXT = 'Home'