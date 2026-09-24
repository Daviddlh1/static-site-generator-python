import os
import shutil

def main():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    public_directory_path = os.path.join(project_root, "public")
    static_directory_path = os.path.join(project_root, "static")
    
    if os.path.exists(public_directory_path):
        shutil.rmtree(public_directory_path)
    # if os.path.exists(static_directory_path):
    #     shutil.rmtree(static_directory_path)

    os.makedirs(public_directory_path)
    # os.makedirs(static_directory_path)
    
    files_to_copy = os.listdir(static_directory_path)
    print(files_to_copy)
    for f in files_to_copy:
        if "png" in f:
            os.mkdir(f"{public_directory_path}/images")
            shutil.copy(os.path.join(static_directory_path, f),os.path.join(public_directory_path, "images"))
        else:
            shutil.copy(os.path.join(static_directory_path, f), os.path.join(public_directory_path))
    
    
main()