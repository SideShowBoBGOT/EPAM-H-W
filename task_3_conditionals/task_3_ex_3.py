import argparse
import os
from os.path import join
import fnmatch
import stat


def finder(paz, pattern):
    """
    Generator function searches for files by a given pattern
    in a given path returns an absolute path of a found file
    @param paz: path
    @param pattern: pattern to look for
    @return: file that resembles pattern
    """
    result = []
    tree = os.walk(paz)
    folder = []
    for i in tree:
        folder.append(i)
    for address, dirs, files in folder:
        for file in files:
            if fnmatch.fnmatch(file, pattern):
                pazz = join(address, file)
                result.append(pazz)
    for el in result:
        yield el


def permissions_to_unix_name(st_mode):
    """
    Function that converts permissions of
    unix file to str
    @param st_mode: encoded permissions of file
    @return: string of file permissions
    """
    permstr = ''
    usertypes = ['USR', 'GRP', 'OTH']
    for usertype in usertypes:
        perm_types = ['R', 'W', 'X']
        for permtype in perm_types:
            perm = getattr(stat, 'S_I%s%s' % (permtype, usertype))
            if st_mode & perm:
                permstr += permtype.lower()
            else:
                permstr += '-'
    return permstr


def display_result(file_paths):
    """
    Function that displays paths to file
    and its permissions
    @param file_paths: list of paths of files
    @return: None
    """
    count = 0
    if file_paths:
        for file in file_paths:
            count += 1
            print(file, '-' + permissions_to_unix_name(os.stat(file).st_mode))
    print(f'Found {count} file(s).')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    parser.add_argument('-p')
    args = parser.parse_args()
    display_result(finder(args.path, args.p))
