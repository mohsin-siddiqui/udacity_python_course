import os


def rename_files():
    # (1) get file names from a folder
    file_list = os.listdir("/home/mohsin/Desktop/udacity/prank")
    # info on pwd or cwd
    saved_path = os.getcwd()
    print("current working directory is: ", saved_path)
    # changing to the argumented dir
    os.chdir("/home/mohsin/Desktop/udacity/prank")
    # (2) for each file, rename filename
    for file_name in file_list:
        print("old name of the file: ", file_name)
        os.rename(file_name, file_name.translate(None, "0123456789"))
        print("New name of the file: ", file_name)
    os.chdir(saved_path)


rename_files()
