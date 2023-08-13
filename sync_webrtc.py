import os
import subprocess
from sys import platform

if not os.path.isdir('src'):
    subprocess.call(['gclient', 'sync'])
    if platform == 'linux':
        subprocess.call(['build/install-build-deps.sh'], cwd='src')
        subprocess.call(['gclient', 'sync'])
else:
    subprocess.call(['git', 'checkout', 'main'], cwd='src')
    subprocess.call(['git', 'pull'], cwd='src')
    subprocess.call(['gclient', 'sync'])
