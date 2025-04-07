import pathlib

def search(path:str,sub_dir:bool,file_types:list) -> list :
    p = pathlib.Path(path) #path to scan
    files = [] # empty list defined
    for t in file_types: # scan for different file types
        if sub_dir : # to scan sub directories as well
            for file in p.glob(f"**/*.{t}"):
                files.append(file) # append file to the list
        else : # do not scan sub directories
            for file in p.glob(f"*.{t}"):
                files.append(file)
    return files
