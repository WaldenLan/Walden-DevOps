#! /usr/bin/python3
#
# Script applied to update the "origin" and
# push the git commits without inputing username & password 

import subprocess

# Github Username
username = "WaldenLan"
# Repository Name 
repository = "Walden-DevOps"
# Update git command
remove = "git remote rm origin"
update = "git remote add origin git@github.com:" + username + "/" + repository + ".git"

# Check whether push is based on http/https request
subprocess.call("git remote -v", shell=True)

# Modification
subprocess.call(remove, shell=True)
subprocess.call(update, shell=True)

# Check whether push is based on git request
subprocess.call("git remote -v", shell=True)