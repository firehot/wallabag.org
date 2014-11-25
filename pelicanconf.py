#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Nicolas L\u0153uillet'
SITENAME = u'wallabag'
#SITEURL = 'http://www.cdetc.fr/v2'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'
DISPLAY_PAGES_ON_MENU = False
ARTICLE_URL = '{slug}'

# Social widget
SOCIAL = (('Github', 'https://github.com/wallabag/wallabag'),
          ('twitter', 'https://twitter.com/wallabagapp'),
          ('Facebook', 'https://facebook.com/wallabag'),
          ('Google+', 'https://plus.google.com/+WallabagOrg'),)

MENUITEMS = (('what is wallabag?', '/'),
             ('Features', '/pages/features.html'),
             ('Downloads', '/pages/download-wallabag.html'),
             ('Documentation', 'http://doc.wallabag.org'),
             ('News', '/blog_index.html'),
             ('Help this project', '/pages/help-this-project.html'),)

DEFAULT_PAGINATION = 6
INDEX_SAVE_AS = 'blog_index.html'
SUMMARY_MAX_LENGTH = None
THEME = "/Users/loeuilletnicolas/pelican-themes/pelican-bootstrap3"
BOOTSTRAP_THEME = 'yeti'

DISPLAY_CATEGORIES_ON_MENU = False

DISPLAY_TAGS_ON_SIDEBAR = True
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 10
DISPLAY_TAGS_INLINE = True

GITHUB_URL = 'https://github.com/wallabag/wallabag'
GITHUB_USER = 'wallabag'
GITHUB_REPO_COUNT = 3

MIT_LICENSE = True

SITELOGO = 'plop.png'

DISPLAY_RECENT_POSTS_ON_SIDEBAR = True

