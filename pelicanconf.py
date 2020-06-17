#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'hawerner'
SITENAME = 'Dark Penguin'
SITEURL = ''
INDEX_SAVE_AS = 'blog/index.html'

PATH = 'content'

#  INDEX_SAVE_AS=blog/index.html
DELETE_OUTPUT_DIRECTORY = True

TIMEZONE = 'Europe/Belgrade'

DEFAULT_LANG = 'en'

THEME='/theme'

MENUITEMS = (
        ("Blog", "/blog"),
        ("Resume", "/resume"),
        )


DISPLAY_PAGES_ON_MENU=False
DISPLAY_MENU=True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
        ('Instagram', 'https://instagram.com/nature_232'),
        ('Another social link', '#'),
        )

FOOTERITEMS = (
        ("GitHub", "https://github.com/hwrnr"),
        )
FOOTERITEMS += SOCIAL

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
