import os

def type2():
    extension = input("Enter extension: ")
    for filename in os.listdir('./'):
        if filename == 'file-type-changer.py':
            pass
        else:
            os.rename(filename, filename[:filename.find(".")]+extension)

def type1():
    file_list = input("Enter a list of files, separated by commas (Do not enter any spaces): ").split(",")
    extension = input("Enter an extension:\n")
    for file in file_list:
        if file == 'file-type-changer.py':
            pass
        else:
            try:
                os.rename(file, file[:file.find(".")]+extension)
            except FileNotFoundError:
                os.system("cls" and "clear")
                print("File not found, make sure not to enter spaces between the commas and files\n")
                type1()

def file_changer():
    type = input("Select an option [1/2]: \n1) Change filetype of specific files\n2) Change filetype of all files in directory\n")

    if type == '1':
        type1()
    elif type == '2':
        type2()
    else:
        file_changer()

file_changer()