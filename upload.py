#!/usr/bin/env python3

import cgi, cgitb, os

cgit.enable()

form = cgi.FieldStorage()
fileitem=form['filename']
if fileitem.filename:
    filename = os.path.basename(fileitem.filename.replace('\\', '/'))
    with open('/tmp/' + filename, 'wb') as f:
        f.write(fileitem.file.read())

    result = 'File "' + filename + ' uploaded'
else:
    result = 'No file was provided'

output = """\
Content-Type: text/html
<html>
<body>
    <p>{}</p>
</body>
</html>
""".format(result)

print(output)

