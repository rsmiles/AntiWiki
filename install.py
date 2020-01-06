import os, shutil
from config import *
from lib import *

print('Make directories needed by AntiWiki...')
os.mkdir(WEB_ROOT + 'cgi-bin')
os.mkdir(WEB_ROOT + 'odt')
os.mkdir(WEB_ROOT + 'odt/pages')
os.mkdir(WEB_ROOT + 'pages')

print('Change directory ownership to web-user...')
shutil.chown(WEB_ROOT + 'cgi-bin', WEB_USER, WEB_USER)
shutil.chown(WEB_ROOT + 'odt', WEB_USER, WEB_USER)
shutil.chown(WEB_ROOT + 'odt/pages', WEB_USER, WEB_USER)
shutil.chown(WEB_ROOT + 'pages', WEB_USER, WEB_USER)

print('Generate index.html for pages directory...')
gen_dir_page(WEB_ROOT + 'pages')

print('Copy default index.odt to it''s proper place...')
shutil.copy2('index.odt', WEB_ROOT + 'odt/index.odt')
shutil.chown(WEB_ROOT + 'odt/index.odt', WEB_USER, WEB_USER)

print('Convert index.odt into index.html...')
convert(WEB_ROOT + 'odt/index.odt', WEB_ROOT)
shutil.chown(WEB_ROOT + 'index.html', WEB_USER, WEB_USER)

print('Copy scripts over to cgi-bin...')
for script in os.listdir('.'):
	if os.path.splitext(script)[1] == 'py' and script != 'install.py':
	shutil.copy2(script, WEB_ROOT + 'cgi-bin')
	shutil.chown(WEB_ROOT + 'cgi-bin/' + script, WEB_USER, WEB_USER)

