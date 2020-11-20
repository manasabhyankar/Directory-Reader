from pathlib import Path
import os, sys, time

def file_helper(directory_path, space_length):
    p = Path(directory_path)
    for x in p.iterdir():
        if(x.is_file()):
            print((' ' * (space_length-1)) + '| ' + '- ' + str(x).split('\\')[-1])
        elif(x.is_dir()):
            print(' ' * space_length + '+ ' + str(x))
            if(os.listdir(x)):
                print(' ' * space_length + '|__v')
                file_helper(x, space_length + 4)


if __name__ == "__main__":
    cmd = sys.argv
    if(Path(cmd[1]).exists()):
        file_helper(Path(cmd[1]), 0)
    else:
        print("Invalid path!")
    
