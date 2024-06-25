import os
import shutil
import sys

def organize_files(directory='.', recursive=False):
    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Get the file extension
            file_extension = os.path.splitext(file)[1][1:]  # Remove the dot
            if file_extension:
                subdirectory = os.path.join(directory, file_extension)
                try:
                    # Create the subdirectory if it doesn't exist
                    if not os.path.exists(subdirectory):
                        os.makedirs(subdirectory)
                        print(f"Created directory: {subdirectory}")
                    # Move the file to the corresponding subdirectory
                    shutil.move(os.path.join(root, file), os.path.join(subdirectory, file))
                    print(f"Moved file: {file} to {subdirectory}")
                except Exception as e:
                    print(f"Error moving file {file}: {e}")
            else:
                print(f"Ignored file without extension: {file}")

        # If not processing recursively, braek after the first directory
        if not recursive:
            break

if __name__ == "__main__":
    import argparse

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Organize files by their extension.')
    parser.add_argument('directory', nargs='?', default='.', help='The target directory to organize.')
    parser.add_argument('-r', '--recursive', action='store_true', help='Recursively organize files in all subdirectories.')
    args = parser.parse_args()

    # Run the organize_files function
    organize_files(args.directory, args.recursive)
