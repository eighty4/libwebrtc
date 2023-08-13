import os
import subprocess

if not os.path.isdir('depot_tools'):
    subprocess.call(["git", "clone", "https://chromium.googlesource.com/chromium/tools/depot_tools.git"])
else:
    subprocess.call(["git", "pull"], cwd='depot_tools')
