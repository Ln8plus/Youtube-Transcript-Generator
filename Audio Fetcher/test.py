import sys,os
target = '' 
files = next(os.walk('Audio Fetcher'), (None, None, []))[2]  
for file in files:
    if file.endswith('.mp3'):
        target = file
print(files)
print(target)

key = ''
print(os.path.dirname(os.path.abspath(sys.argv[0])))
where = os.path.dirname(os.path.abspath(sys.argv[0]))  + '\\' + target
print(where)

with open(os.path.join(sys.path[0], 'api_key.txt'), 'r') as f:
    while True:
       key = ''.join(str(f.readlines()))
       if not f.readlines():
           break

print(key)
