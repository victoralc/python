import os

def rename_files():
    file_list = os.listdir("/home/victor/Desktop/victor/projects/python/prank/prank")
    saved_path = os.getcwd()

    print("Current directory " + saved_path)
    os.chdir("/home/victor/Desktop/victor/projects/python/prank/prank")

    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)
rename_files()
