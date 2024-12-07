import os
import shutil

# Directory name
dir_name = "/home/runner/.snowcli/config"

# Remove the directory if it exists
if os.path.exists(dir_name):
    shutil.rmtree(dir_name)

# Create the directory
os.makedirs(dir_name)
