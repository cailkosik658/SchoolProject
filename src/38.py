import os
import sys

def main():
    # Example usage: Replace this with actual file path
    file_path = "example.txt"
    
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    else:
        print("File does not exist.")
        
if __name__ == "__main__":
    main()
