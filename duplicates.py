import os
import sys
from itertools import count


def are_files_duplicates(file_1, file_2):
    pass


def get_all_files(folder):
    walktree = os.walk(folder)
    all_files = list()
    for step in walktree:
        try:
            files_in_dir = step[2]
        except IndexError:
            continue
        current_dir = step[0]
        for file_name in files_in_dir:
            file_size = os.stat(current_dir+'\\'+file_name).st_size
            all_files.append({'file_dir': current_dir,
                              'file_name': file_name,
                              'file_size': file_size})
    for file in all_files:
        print(file)
    return all_files


if __name__ == '__main__':
    #dir_to_scan = sys.argv[1]
    get_all_files(os.getcwd())
