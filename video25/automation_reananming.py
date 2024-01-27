import os

os.chdir("fold")
os_dot_path_dir = ['__all__', '__builtins__', '__cached__', '__doc__', '__file__', 
                   '__loader__', '__name__', '__package__', '__spec__', '_get_sep',
                   '_joinrealpath', '_varprog', '_varprogb', 'abspath', 'altsep', 
                   'basename', 'commonpath', 'commonprefix', 'curdir', 'defpath', 
                   'devnull', 'dirname', 'exists', 'expanduser', 'expandvars', 
                   'extsep', 'genericpath', 'getatime', 'getctime', 'getmtime', 
                   'getsize', 'isabs', 'isdir', 'isfile', 'islink', 'ismount',
                   'join', 'lexists', 'normcase', 'normpath', 'os', 'pardir', 
                   'pathsep', 'realpath', 'relpath', 'samefile', 'sameopenfile',
                   'samestat', 'sep', 'split', 'splitdrive', 'splitext', 'stat', 
                   'supports_unicode_filenames', 'sys']
i = 1
for f in os.listdir():
    file_name, file_extention = os.path.splitext(f)
    new_content = f"{(i)}-{file_name.split()}{file_extention}"
    print(new_content)
    os.rename(f,new_content)
    i +=1
    os.remove(f)
    