import subprocess
from modules import conv
from modules import bottom_line

def give_me_the_lengths(vid_list:list, verbose=False):
    time = 0.0
    for v in vid_list:
        v_time = subprocess.run([""
        "ffprobe"
        , "-v"
        , "error"
        ,"-show_entries"
        , "format=duration"
        , "-of"
        , "default=noprint_wrappers=1:nokey=1"
        , v
                                ]
        , stdout=subprocess.PIPE
        , stderr=subprocess.STDOUT
                                )
        try:
            time += float(v_time.stdout)
        except:
            continue
        if verbose:
            v_time = conv.ert(v_time.stdout)
            print (f"👉 \033[33m[{v}]\033[39m ==> \033[34m{v_time['hr']} hours and {v_time['mn']} minutes\033[39m\n")
        bottom_line.update_bottom_line ("💠 Total : \033[32m{} hours and {} minutes\033[39m".format(conv.ert(time)['hr'],conv.ert(time)['mn']))
    print (f"💠 Total : \033[32m{conv.ert(time)['hr']} hours and {conv.ert(time)['mn']} minutes\033[39m")
    