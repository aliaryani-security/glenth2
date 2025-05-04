from time import sleep

def show():
    logo =[
        '\033[36m    █ ▗▞▀▚▖▄▄▄▄     ■  ▐▌   ▄▄▄▄ '
        , '    █ ▐▛▀▀▘█   █ ▗▄▟▙▄▖▐▌      █ '
        , '    █ ▝▚▄▄▖█   █   ▐▌  ▐▛▀▚▖█▀▀▀ '
        , ' ▗▄▖█              ▐▌  ▐▌ ▐▌█▄▄▄ '
        , '▐▌ ▐▌   \033[32mBy:\033[36m        ▐▌            '
        , ' ▝▀▜▌       \033[32mAli Aryani\033[36m'
        , '▐▙▄▞▘  \033[32mgithub: aliaryani-security\033[36m'
    ]
    for line in logo :
        print ('\033[36m',line)
        sleep(.2)
    print('\033[39m')
    sleep (1)
    
