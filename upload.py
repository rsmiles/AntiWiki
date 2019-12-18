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
    result = """<p>FILE "{0}" uploaded.</p>
    <a href="/{1}.html">click here to return to {1}</a>
    <p>convert src = {2}</p>
    <p>convert dest = {3}</p>""".format(filename, doc, ODT + doc + '.odt', WEB_ROOT + doc + '.html')
    convert(ODT + doc + '.odt', WEB_ROOT + os.path.dirname(doc))
else:
    result = '<p>No file was provided<\p>'


output = """HTTP/1.0 200 OK
Content-Type: text/html

<html>
<body>
    {0}
</body>
</html>\
""".format(result)

print(output)

