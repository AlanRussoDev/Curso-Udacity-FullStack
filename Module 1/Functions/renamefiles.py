import os

def rename_files():
    file_list = os.listdir(r"/home/alan/Documents/study/Curso-Udacity-FullStack/Module 1/Functions/prank")
    print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is" + saved_path)
    os.chdir(r"/home/alan/Documents/study/Curso-Udacity-FullStack/Module 1/Functions/prank")
    
    for file_name in file_list:
        print("Old name" + file_name)
        print("New name" + file_name.translate(None,"0123456789"))
        os.rename(file_name,file_name.translate(None,"0123456789"))
    os.chdir(saved_path)
    
rename_files()
