#!/usr/bin/env python3

import os, tarfile, sys
from datetime import datetime

# Get directory from command line
log_dir = sys.argv[1]

# Create "archives" folder
os.makedirs("archives", exist_ok=True)

# Create archive name with timestamp
name = "logs_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".tar.gz"
path = os.path.join("archives", name)

# Make tar.gz archive
with tarfile.open(path, "w:gz") as tar:
    tar.add(log_dir, arcname=os.path.basename(log_dir))

print("Saved archive:", path)

# Record in log file
with open("archive.log", "a") as f:
    f.write(f"{datetime.now()} -> {path}\n")

