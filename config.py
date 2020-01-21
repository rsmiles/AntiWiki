import os

WEB_USER = 'www-data'

CONVERT_ROOT = '/tmp/AntiWiki/'

CONVERT_DIR=CONVERT_ROOT + str(os.getpid()) + '/'

WEB_ROOT = '/var/www/html/'

CGI_BIN = WEB_ROOT + 'cgi_bin/'

PAGES = WEB_ROOT + 'pages/'

ODT = WEB_ROOT + 'odt/'

ODT_PAGES = ODT + 'pages/'

