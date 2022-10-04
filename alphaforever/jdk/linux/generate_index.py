import os
from glob import glob
PATH = "./"
result = [y for x in os.walk(PATH) for y in glob(os.path.join(x[0], '*.*'))]

out ='''{\n\t"files" : ['''

filelist = []

for file_long in result:
    file = file_long[2:]

    if file == "generate_index.py"  or file == "index.json" or file[0] == ".":
        continue

    file_stats = os.stat(file)
    filelist.append('\n\t\t{"name":"' + file + '", "size": ' + str(file_stats.st_size) + '}');
out += ','.join(filelist)
out += '''\n\t]\n}'''

o =  open("index.json", "w+")
o.write(out)
o.close()
