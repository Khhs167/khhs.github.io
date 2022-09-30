import os
from glob import glob
PATH = "./"
result = [y for x in os.walk(PATH) for y in glob(os.path.join(x[0], '*.*'))]

out ='''<?xml version="1.0" encoding="UTF-8"?><ListBucketResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/"><Name>MinecraftResources</Name><Prefix/><Marker/><MaxKeys>1000</MaxKeys><IsTruncated>false</IsTruncated>'''

for file_long in result:
    file = file_long[2:]

    if file == "autoxml.py"  or file == "index.xml" or file[0] == ".":
        continue

    file_stats = os.stat(file)
    out += '<Contents><Key>' + file + '</Key><Size>' + str(file_stats.st_size) + '</Size></Contents>';

out += '''</ListBucketResult>'''

o =  open("index.xml", "w+")
o.write(out)
o.close()
