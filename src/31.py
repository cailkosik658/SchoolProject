import os

def process_directory(directory):
    """
    Process a directory by listing files and directories.
    
    Parameters:
    - directory: str, the path of the directory to be processed
    
    Returns:
    - list: A list containing all file names in the specified directory.
    """

    # Initialize an empty list for directory content
    contents = []

    # Iterate through each file in the specified directory
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            contents.append(filename)

    return contents

# Example usage
directory_path = '/path/to/your/directory'
file_list = process_directory(directory_path)
print(file_list)
