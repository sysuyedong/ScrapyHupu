import json

f = file("../film.json")
s = json.load(f)
s = json.dumps(s)
s = json.loads(s)
name = s["films"][1]["name"]
for n in name:
	print n
print ''.join(name)
print s
f.close