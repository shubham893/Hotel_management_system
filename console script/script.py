import subprocess
while True:
	subprocess.Popen(['ecpg','code.ecpg']).communicate()
	subprocess.Popen(['gcc', '-I/usr/include/postgresql' ,'-L/usr/lib/postgresql', 'code.c','-lecpg']).communicate()
	subprocess.Popen(['./a.out']).communicate()