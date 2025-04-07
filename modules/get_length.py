import subprocess
from modules import conv

def give_me_the_lengths(vid_list:list):
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
                                ])
        time += float(v_time)
        v_time = conv.ert(v_time)
        print (f"{v} ==> {v_time['hr']} hours and {v_time['mn']} minutes\n")
    print (f"Total : {conv.ert(time)['hr']} hours and {conv.ert(time)['mn']} minutes")