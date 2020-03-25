from pathlib import Path

#Absolute path #we start from the root of our hard disk
#/user/local/bin
#Relative path #it means a path starting from the current directory

'''path = Path("ecommerce")
print(path.exist())'''#it checks if the directory exist

'''path = Path("emails")
print(path.mkdir())''' #it creates a new directory

'''path = Path("emails")
print(path.rmdir())''' #it removes the directory

path = Path()
for file in path.glob("*.py"): #whit this method we can search for files and directories in the current path
    print(file)
