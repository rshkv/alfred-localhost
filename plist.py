import sys
from plistlib import readPlist, writePlist

query = sys.argv[1]

info = readPlist('info.plist')
info['variables']['last'] = query
writePlist(info, 'info.plist')
