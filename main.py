#!/bin/env python3
from modules import find_vid,get_length,parser,banner
banner.show()

parser_arguments = parser.get_args()

files_list = find_vid.search(
    parser_arguments['target_dir']
    , parser_arguments['sub_dir']
    , parser_arguments['types']
    )

get_length.give_me_the_lengths(files_list,parser_arguments['verbose'])