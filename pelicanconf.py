#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Nicolas L\u0153uillet'
SITENAME = u'wallabag'
SITEURL = 'https://www.wallabag.org'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'
DISPLAY_PAGES_ON_MENU = False
ARTICLE_URL = '{slug}'

# Social widget
SOCIAL = (('Github', 'https://github.com/wallabag/wallabag'),
          ('twitter', 'https://twitter.com/wallabagapp'),
          ('Facebook', 'https://facebook.com/wallabag'),
          ('Google+', 'https://plus.google.com/+WallabagOrg'),
          ('RSS', 'https://www.wallabag.org/feeds/all.atom.xml'),
          )

MENUITEMS = (('what is wallabag?', '/'),
             ('Features', '/pages/features.html'),
             ('Downloads', '/pages/download-wallabag.html'),
             ('Documentation', 'http://doc.wallabag.org'),
             ('Need help?', 'http://support.wallabag.org'),
             ('News', '/blog_index.html'),
             ('Help this project', '/pages/help-this-project.html'),
             ('Try wallabag', 'http://demo.wallabag.org'),
             ('Contact', '/pages/contact-us.html'),)

DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'sitemap')
SITEMAP_SAVE_AS = 'sitemap.xml'

DEFAULT_PAGINATION = 6
INDEX_SAVE_AS = 'blog_index.html'
SUMMARY_MAX_LENGTH = None
THEME = "pelican-bootstrap3"
BOOTSTRAP_THEME = 'yeti'

DISPLAY_CATEGORIES_ON_MENU = False

DISPLAY_TAGS_ON_SIDEBAR = True
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 10
DISPLAY_TAGS_INLINE = True

MIT_LICENSE = True

HIDE_SITENAME = True

DISPLAY_RECENT_POSTS_ON_SIDEBAR = True

WALLABAG_VERSION = "1.8.1"

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

STATIC_PATHS = [
    'extra',
    'images'
    ]

TEMPLATE_PAGES = {'extra/404.html': '404.html'}

EXTRA_PATH_METADATA = {
    'extra/c89a2a203e9a6045dd4df81b6ca20289.txt': {'path': 'c89a2a203e9a6045dd4df81b6ca20289.txt'},
    'extra/googlef9834aed73023328.html': {'path': 'googlef9834aed73023328.html'},
    'extra/CNAME': {'path': 'CNAME'},
}

READERS = {'html': None}