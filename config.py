import os

CONVERT_PARENT = '/tmp/Antiwiki/'

CONVERT_DIR=CONVERT_PARENT + str(os.getpid()) + '/'

WEB_ROOT = '/var/www/html/'

ODT = WEB_ROOT + 'odt/'

if not os.path.isdir(CONVERT_PARENT):
    os.mkdir(CONVERT_PARENT)

if not os.path.isdir(ODT):
    os.mkdir(ODT)

