import os
import shutil

# Create a new directory if it doesn't already exist
name_directory = 'my_new_directory'

# Check if the directory already exists
if not os.path.exists(name_directory):
    os.mkdir(name_directory)
    print(f"Directory '{name_directory}' created successfully.")
else:
    print(f"Directory '{name_directory}' already exists.")

# Get the current directory
print("Current Directory:", os.getcwd())

# Change to a new directory (make sure this path exists)
os.chdir('C:\\Users\\Nibedita Biswas\\Desktop\\Study Material\\Python\\Shell programming')
print("Directory Changed To:", os.getcwd())

# List files in the current directory
print("Files:", os.listdir("."))

# Define the source file and the destination directory
source_file = 'shell.py'  # Assuming this file exists in the current directory
destination_file = os.path.join(name_directory, 'shell.py')  # Path to where you want to copy the file

# Copy the file to the new directory
shutil.copy(source_file, destination_file)

print(f"File '{source_file}' copied to '{destination_file}' successfully.")
