import subprocess

def figlet():
    text = input(" \033[1;32m|--- \033[1;31m The Text: \033[1;32m")
    try:
        subprocess.run(["figlet", text,], check=True)
    except subprocess.CalledProcessError as e:

        print(f"Error: {e}")