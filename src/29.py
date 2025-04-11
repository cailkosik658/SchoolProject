import os
import subprocess

def execute_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if error:
        print(f"Error: {error.decode('utf-8')}")
        return None
    else:
        return output

if __name__ == "__main__":
    # Execute a command and get the output
    result = execute_command(["ls", "-l"])
    
    if result is not None:
        for line in result.stdout.strip().split('\n'):
            print(f"{line.decode('utf-8')}")
