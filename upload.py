#!/usr/bin/env python3

import cgi, cgitb, os
from lib import *

cgitb.enable()
form = cgi.FieldStorage()

qstring = os.environ['QUERY_STRING']
doc = os.path.splitext(qstring.split('=')[1])[0]

result = ''

fileitem=form['filename']
if fileitem.filename:
    filename = os.path.basename(fileitem.filename.replace('\\', '/'))
    with open(ODT + doc + '.odt', 'wb') as f:
        f.write(fileitem.file.read())
    result = """<p>FILE "{0}.odt" uploaded.<\p>
<a href="/doc{0}.html">click here<\\a>""".format(doc)
else:
    result = '<p>No file was provided<\p>'

convert(ODT + doc + '.odt', WEB_ROOT + doc + 'html')

output = """HTTP/1.0 200 OK
Content-Type: text/html

<html>
<body>
    <p>{}</p>
</body>
</html>\
""".format(result)

print(output)

