from pathlib import Path


path = Path("ecommerce") #if the Path is left empty Path(), it uses the current directory
print(path.exists()) #Check if a folder exists

#path.mkdir() - used for creating directories
#path.rmdir() - used for deleting directories
#path.glob('*.*') - returns all the files within the current directory
#path.glob('*') - returns all the files within the current directory including all the directories
#path.glob('*.py') - returns all the python files within the current directory

for file in path.glob('*.py'):
    print(file)

path = Path()

for file in path.glob('*'):
    print(file)