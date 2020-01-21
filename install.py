#!/usr/bin/env python3

import os, shutil
from config import *
from lib import *

print('Make directories needed by AntiWiki...')
os.mkdir(CONVERT_ROOT)
os.mkdir(CGI_BIN)
os.mkdir(PAGES)
os.mkdir(ODT)
os.mkdir(ODT_PAGES)

#print('Change directory ownership to web-user...')
shutil.chown(CONVERT_ROOT, WEB_USER, WEB_USER)
shutil.chown(CGI_BIN, WEB_USER, WEB_USER)
shutil.chown(PAGES, WEB_USER, WEB_USER)
shutil.chown(ODT, WEB_USER, WEB_USER)
shutil.chown(ODT_PAGES, WEB_USER, WEB_USER)

print('Generate index.html for pages directory...')
gen_dir_page(PAGES)

print('Copy default index.odt to it''s proper place...')
shutil.copy2('index.odt', ODT + 'index.odt')
shutil.chown(ODT + 'index.odt', WEB_USER, WEB_USER)

print('Convert index.odt into index.html...')
convert(ODT + 'index.odt', WEB_ROOT)
shutil.chown(WEB_ROOT + 'index.html', WEB_USER, WEB_USER)

print('Copy scripts over to cgi-bin...')
for script in os.listdir('.'):
	if os.path.splitext(script)[1] == 'py' and script != 'install.py':
		shutil.copy2(script, WEB_ROOT + 'cgi-bin')
		shutil.chown(WEB_ROOT + 'cgi-bin/' + script, WEB_USER, WEB_USER)

