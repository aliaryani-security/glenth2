import argparse
from modules import print_ver
def get_args() -> dict:
    # parser defined here , 

    parser = argparse.ArgumentParser(
        prog='glenth2'
        , description='glenth2 helps you find out total length of videos'
        , usage='glenth2 [options]'
        , epilog='for more information visit : https://gtihub.com/thehannibalist/glenth2'
    )

    # custom directory option
    parser.add_argument(
        '-d'
        , '--target-directory'
        , default='.'
        , help='choose a directory to search for videos (default is current directory.)'
    )

    # show version option
    parser.add_argument(
        '-v'
        , '--version'
        , help='prints current version and exits'
        , action='store_true'
    )

    # choose types option
    parser.add_argument (
        '-t'
        , '--types'
        , default='all'
        , help='video extensions to search for (seperate with commas (e.g. mp4,mkv)) (default is all possible videos)'
    )

    # sub directories option
    parser.add_argument(
        '-s'
        , '--sub-directories'
        , help='will scan all sub directories for videos as well'
        , action='store_true'
    )

    args = parser.parse_args() # read arguments
    if args.version: # check if version is asked
        print_ver.show()
    target_dir = args.target_directory # target directory
    types = [] # empty list defined
    if args.types == 'all': # file types
        for item in ['mp4','mkv','mpg','mpeg','3gp','mov','avi','ts']:
            types.append(item)
    else:
        for t in args.types.split(','):
            types.append(t)
    sub_dir = args.sub_directories
    return {
        'target_dir' : target_dir
        , 'types' : types
        , 'sub_dir' : sub_dir
        }
