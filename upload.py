#!/usr/bin/env python3

import cgi, cgitb, os

cgitb.enable()
form = cgi.FieldStorage()

result = ''

fileitem=form['filename']
if fileitem.filename:
    filename = os.path.basename(fileitem.filename.replace('\\', '/'))
    with open('/tmp/' + filename, 'wb') as f:
        f.write(fileitem.file.read())
    result = 'File "' + filename + '" uploaded'
else:
    result = 'No file was provided'

output = """\
HTTP/1.0 200 OK
Content-Type: text/html

<html>
<body>
    <p>{}</p>
</body>
</html>\
""".format(result)

print(output)

