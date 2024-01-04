import shutil

#make a copy of the invoice to work with
src="cry.py"
dst="delete.py"
shutil.copy(src,dst)


try:
    with open(dst, 'r') as file:
        script_contents = file.read()
        exec(script_contents)
except FileNotFoundError:
    print(f"File '{dst}' not found.")
except Exception as e:
    print(f"An error occurred while executing '{dst}': {e}")