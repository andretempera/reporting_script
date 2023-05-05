# This script is just practice from a Coursera certificate. 
# Basically it will print local files / directories in different ways

# Importing required library
import os

# Using os.walk() to find files (replace _file/files with _directory/directories to find directories)
print("\nUSING OS.WALK")
print("Finding files:")
for root, directories, files in os.walk('.'):
    for _file in files:
        print(f"File found: {_file}")

input("""
---> This used os.walk() to find files

Press ENTER to continue...
""")

# Updating the loop so that it shows the absolute path of a file
print("\nFinding files with full path:")
for root, directories, files in os.walk('.'):
    for _file in files:
        full_path = os.path.join(root, _file)
        print(f"File found: {full_path}")

input("""
---> This showed updated loop to include file paths

Press ENTER to continue...
""")

# Updating the loop once again, this time to include the file size
print("\nFinding files with full path and file size:")
for root, directories, files in os.walk('.'):
    for _file in files:
        full_path = os.path.join(root, _file)
        size = os.path.getsize(full_path)
        print(f"File: {full_path} | Size: {size}b")

input("""
---> This showed updated loop to include file paths AND file size

Press ENTER to continue...
""")

# Persisting the data into a dictionary, using file paths as dictionary keys
print("\nFile data into dictionary:")
file_metadata = {}
for root, directories, files in os.walk('.'):
    for _file in files:
        full_path = os.path.join(root, _file)
        size = os.path.getsize(full_path)
        file_metadata[full_path] = size
print(file_metadata)

input("""
---> This is the file data that was appended to a dictionary

Press ENTER to continue...
""")

# Using the dictionary to query files by file size
print("\nQuerying 3 largest files from dictionary:") 
items_shown = 0
for path, size in sorted(file_metadata.items(), key=lambda x:x[1], reverse=True):
    if items_shown == 3:
        break
    print(f"Size: {size} Path: {path}")
    items_shown += 1

input("""
---> This used the dictionary to identify the 3 largest files

Press ENTER to continue...
""")

# Using os.listdir instead of os.walk
print("\nUSING OS.LISTDIR")
print("Identifying local files/directories:") 
for item in os.listdir('.'):
  if os.path.isdir(item):
    print("This is a directory {0}".format(item))
  else:
    print("This is a file: {0}".format(item))

input("""
---> This used os.listdir() to find files

Press ENTER to continue...
""")

# Capturing results in a new variable
print("\nResults into list:") 
important_directories = []
for item in os.listdir('.'):
  if os.path.isdir(item):
    important_directories.append(item)
print(important_directories)

input("""
---> This captured directories in a variable

Press ENTER to continue...
""")

# Capturing results in a new variable
print("\nFiltered files into list:") 
important_files = []
for item in os.listdir('.'):
  if item.endswith('.py'):
    continue   # flow control - excludes file that meets condition(e.g ".py")
  if os.path.isfile(item):
    important_files.append(item)
print(important_files)

input("""
---> This captured filtered files in a variable

THE END
""")

