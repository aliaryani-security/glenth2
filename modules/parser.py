import argparse

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

