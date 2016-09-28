import os
import sys
from operator import itemgetter
from collections import Counter


def find_duplicates(files):
    filtered = list()
    duplicates = list()
    for file_info in files:
        file_stats = list(file_info.keys())[0]
        if file_stats in filtered:
            duplicates.append(file_info)
        else:
            filtered.append(file_stats)
    return duplicates


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
            file_size = os.stat(current_dir+'/'+file_name).st_size
            all_files.append({(file_name, file_size): current_dir})
    return all_files


def pprint_file(file):
    file_name = list(file.keys())[0][0]
    file_path = list(file.values())[0]
    print('/'.join((file_path, file_name)))


if __name__ == '__main__':
    dir_to_scan = sys.argv[1]
    all_files = get_all_files(dir_to_scan)
    duplicates = find_duplicates(all_files)
    if duplicates:
        print('These files are duplicates and can be deleted safely:')
        for file_info in duplicates:
            pprint_file(file_info)
    else:
        print('Duplicates not found.')
