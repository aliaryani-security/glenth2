from time import sleep

def show():
    logo =[
        '    █ ▗▞▀▚▖▄▄▄▄     ■  ▐▌   ▄▄▄▄ '
        , '    █ ▐▛▀▀▘█   █ ▗▄▟▙▄▖▐▌      █ '
        , '    █ ▝▚▄▄▖█   █   ▐▌  ▐▛▀▚▖█▀▀▀ '
        , ' ▗▄▖█              ▐▌  ▐▌ ▐▌█▄▄▄ '
        , '▐▌ ▐▌   By:        ▐▌            '
        , ' ▝▀▜▌       Ali Aryani (Hannibal)'
        , '▐▙▄▞▘   github.com/thehannibalist'
    ]
    for line in logo :
        print ('\033[36m',line)
    print('\033[39m')
    sleep (1)
    