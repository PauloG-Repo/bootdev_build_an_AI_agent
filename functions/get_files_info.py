import os

def get_files_info(working_directory, directory="."):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_working_dir, directory))

        valid_target_dir = os.path.commonpath([abs_working_dir, target_dir]) 
        
        if valid_target_dir != abs_working_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        

        target_dir_list = []
        for filename in os.listdir(target_dir):
            filepath = os.path.join(target_dir, filename)
            is_dir = os.path.isdir(filepath)
            file_size = os.path.getsize(filepath)
            info = f'- {filename}: file_size={file_size} bytes, is_dir={is_dir}'
            target_dir_list.append(info)
        return '\n'.join(target_dir_list)
    except Exception as e:
        return f'Error: {e}'

