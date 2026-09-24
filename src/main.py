import os
import shutil

def main():
    public_directory_path = os.path.abspath("../public")
    static_directory_path = os.path.abspath("../static")
    
    if os.path.exists(public_directory_path):
        shutil.rmtree(public_directory_path)
    if os.path.exists(static_directory_path):
        shutil.rmtree(static_directory_path)
    
main()