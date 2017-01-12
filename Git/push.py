#! /usr/bin/python3

import sys
import subprocess

# Commit content
commit = "git commit -m '" + sys.argv[1] + "'"

# Git push procedures
subprocess.call("git add .", shell=True)
subprocess.call(commit, shell=True)
subprocess.call("git push -u origin master", shell=True)