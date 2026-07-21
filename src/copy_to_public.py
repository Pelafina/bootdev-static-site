import os
import shutil

def copy_static_to_public(public_path):
    path_to_public_dir = os.path.abspath(public_path)
    path_static_dir = os.path.abspath(os.path.join(".", "static"))
    if os.path.exists(path_to_public_dir):
        shutil.rmtree(path_to_public_dir) 
    os.mkdir(path_to_public_dir)
    if not os.path.exists(path_static_dir):
        raise Exception("No static directory from which to copy exists.")
    else:
        copy_file_contents(path_static_dir, path_to_public_dir)

def copy_file_contents(src_path, dst_path):
        files_to_copy = os.listdir(src_path)
        for file in files_to_copy:
            file_path = os.path.join(src_path, file)
            if os.path.isfile(file_path):
                shutil.copy(file_path, dst_path)
            else:
                os.mkdir(os.path.join(dst_path, file))
                copy_file_contents(file_path, os.path.join(dst_path, file))
