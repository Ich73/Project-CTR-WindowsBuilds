from os import makedirs, remove, rename
from os.path import join, exists
from subprocess import run
from zipfile import ZipFile
import re

# target-name :: (gcc, g++)
CONFIG = {
	'i686':   ('i686-w64-mingw32-gcc',   'i686-w64-mingw32-g++'),
	'x86_64': ('x86_64-w64-mingw32-gcc', 'x86_64-w64-mingw32-g++'),
	None: ('gcc', 'g++') # revert Makefile changes
}

# tool-name :: file containing version
TOOLS = {
	'ctrtool': 'main.c',
	'makerom': 'user_settings.c'
}

for type, (gcc, gpp) in CONFIG.items():
	print('='*100)
	print('>>', 'COMPILE', type)
	print('='*100)
	print()
	
	for tool, version_file in TOOLS.items():
		print('>>', 'COMPILE', type, tool)
		print()
		
		# change makefile
		with open(join(tool, 'Makefile'), 'r', encoding='UTF-8') as file: makefile = file.read().splitlines(True)
		def replace(line):
			if line.startswith('CC = '): return 'CC = %s\n' % gcc
			if line.startswith('CXX = '): return 'CXX = %s\n' % gpp
			return line
		makefile = [replace(line) for line in makefile]
		with open(join(tool, 'Makefile'), 'w', encoding='UTF-8') as file: file.write(''.join(makefile))
		
		# find version
		with open(join(tool, version_file), 'r', encoding='UTF-8') as file: srcfile = file.read()
		version = re.search('v\d(\.\d+)+', srcfile)[0]
		
		if type is not None:
			# clean
			zip = join('build', '%s-%s-win_%s.zip' % (tool, version, type))
			if exists(zip): remove(zip)
			
			# make
			run('make', cwd=tool)
			
			# copy
			makedirs('build', exist_ok=True)
			exe = join('build', tool+'.exe')
			if exists(exe): remove(exe)
			rename(join(tool, tool+'.exe'), exe)
			with ZipFile(zip, 'w') as zip: zip.write(exe, arcname=tool+'.exe')
			remove(exe)
		
		# clean
		run('make clean', cwd=tool)
		print()
