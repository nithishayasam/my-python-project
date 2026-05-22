from pathlib import Path
import os
def readfileandfolder():
    path = Path('1')
    items = list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f"{i+1} : {items}")

def createfile():
    try:
        readfileandfolder()
        name = input("Enter the name of the file you want to create: ")
        p = Path(name)
        if not p.exists():
            with open(p, 'w') as fs:
                data = input("Enter the data you want to write in the file: ")
                fs.write(data)
                print(f"File '{name}' created successfully.")
        else:
            print(f"File '{name}' already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

def readfile():
    try:
        readfileandfolder()
        name = input("Enter the name of the file you want to read: ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, 'r') as fs:
                data = fs.read()
                print(data)
        else:
            print(f"File '{name}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")        

def updatefile():
    try:
        readfileandfolder()
        name = input("Enter the name of the file you want to update: ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("1. Change the file name")
            print("2. Overwrite the data in the file")
            print("3. Append to the file")
        response = int(input("Enter your choice: "))
        if response == 1:
               name2 = input("Enter the new name of the file: ")
               p2= Path(name2)
               p.rename(p2)
               print(f"File renamed to '{name2}' successfully.")
        if response == 2:
            with open(p,'w') as fs:
                data = input("Enter the new data you want to write in the file: ")
                fs.write(data)
                print(f"File '{name}' updated successfully.")   
        if response == 3:
            with open(p,'a') as fs:
                data = input("Enter the data you want to append to the file: ")
                fs.write(""+data)
                print(f"Data appended to file '{name}' successfully.")                  
    except Exception as e:
        print(f"An error occurred: {e}")

def deletefile():
    try:
        readfileandfolder()
        name = input("Enter the name of the file you want to delete: ")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(name)
            print(f"File '{name}' deleted successfully.")
        else:
            print(f"File '{name}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

print("1. Create a file")
print("2. Read a file")
print("3. Update a file")
print("4. Delete a file")        
response = int(input("Enter your choice: "))
if response == 1:
    createfile()            
if response == 2:
    readfile()  
if response == 3:
    updatefile()    
if response == 4:        
    deletefile()